from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.forms import RegistrationForm,LoginForm,MovieForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from myapp.models import Movie
from django.contrib import messages
from django.utils.decorators import method_decorator



def sign_required(fn):
    def wrapper(request,*args,**kwargs):
        if  not request.user.is_authenticated:
            messages.success(request,"Please Login!!")
            return redirect("signin")
        return fn(request,*args,**kwargs)
    return wrapper


class SignUpView(View):
    
    model=User
    form_class=RegistrationForm
    template_name="register.html"

    def get(self,request,*args,**kwargs):
        form=self.form_class
        return render(request,self.template_name,{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request," Registered succesfully ")
            return redirect("signin")
        messages.error(request,"Try again")
        return render(request,"register.html")
    


class SignInView(View):

    model=User
    form_class=LoginForm
    template_name="login.html"

    def get(self,request,*args,**kwargs):
        form=self.form_class
        return render(request,self.template_name,{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"Login succesfully")
                return redirect("index")
            messages.error(request,"Invalid credentials")
            return render(request,self.template_name,{"form":form})


@method_decorator(sign_required,name="dispatch")
class IndexView(View):

    template_name="index.html"

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name) 
    

@method_decorator(sign_required,name="dispatch")
class MovieCreateView(View):

    model=Movie
    form_class=MovieForm
    template_name="movie-add.html"

    def get(self,request,*args,**kwargs):
        form=self.form_class
        return render(request,self.template_name,{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Movie has been created")
            return redirect("index")
        messages.error(request,"movie can not created")
        return render(request,self.template_name,{"form":form})
    
@method_decorator(sign_required,name="dispatch")
class MovieListView(View):

    model=Movie
    template_name="movie-list.html"

    def get(self,request,*args,**kwargs):
        qs=Movie.objects.all()  
        return render(request,self.template_name,{"movies":qs})      
    

@method_decorator(sign_required,name="dispatch")
class MovieDetailView(View):

    model=Movie
    template_name="movie-detail.html"

    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Movie.objects.get(id=id)
        return render(request,self.template_name,{"movie":qs})
    

@method_decorator(sign_required,name="dispatch")
class MovieEditView(View):
    model=Movie
    form_class=MovieForm
    template_name="movie-edit.html"


    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        movie=Movie.objects.get(id=id)
        form=self.form_class(instance=movie)
        return render(request,self.template_name,{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        movie=Movie.objects.get(id=id)
        form=self.form_class(data=request.POST,instance=movie,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Movie details has been updated")
            return redirect("movie-detail",pk=id)
        messages.error(request,"Failed to update")
        return render(request,self.template_name)

@sign_required
def movie_delete_view(request,*args,**kwargs):
    id=kwargs.get("pk")
    qs=Movie.objects.get(id=id).delete()
    messages.success(request,"Movie deleted")
    return redirect("movie-list")


def signout_view(request,*args,**kwargs):
    logout(request)
    messages.success(request,"logged out")
    return redirect("signin")
    

