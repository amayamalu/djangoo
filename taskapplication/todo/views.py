from django.shortcuts import render,redirect
from django.views.generic import View
from todo.forms import RegsitrationForm,LoginForm,TaskForm,TaskEditForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from todo.models import Task
from django.utils.decorators import method_decorator


def sign_required(fn):

    def wrapper(request,*args,**kwargs):
        if  not request.user.is_authenticated:
            messages.error(request,"Please Login!!")
            return redirect("signin")
        return fn(request,*args,**kwargs)
    return wrapper




class SignUpView(View):
    model=User
    template_name="register.html"
    form_class=RegsitrationForm

    def get(self,request,*args,**kwargs):
        form=self.form_class
        return render(request,self.template_name,{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"account has beeen created")
            return redirect("signin")
        messages.error(request,"failed")
        return render(request,self.template_name,{"form":form})

class SignInView(View):
    model=User
    template_name="login.html"
    form_class=LoginForm
     
    def get(self,requst,*args,**kwargs):
        form=self.form_class
        return render(requst,self.template_name,{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login succesffully")
                return redirect("index")
        messages.error(request,"Invalid credential")
        return render(request,self.template_name,{"form":form})
        

#Template inheritance

@method_decorator(sign_required,name="dispatch")
class IndexView(View):
    template_name="index.html"

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
    
@method_decorator(sign_required,name="dispatch")
class TaskCreateView(View):
    model=Task
    form_class=TaskForm
    template_name="task-add.html"

    def get(self,request,*args,**kwargs):
        form=self.form_class
        return render(request,self.template_name,{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            messages.success(request,"Task has been created ")
            return redirect("task-list")
        messages.error(request,"failed to create task")
        return render(request,self.template_name,{"form":form})
        

@method_decorator(sign_required,name="dispatch")
class TaskListView(View):
    model=Task
    template_name="task-list.html"

    def get(self,request,*args,**kwargs):
        qs=Task.objects.filter(user=request.user).order_by("-created_date")
        return render(request,self.template_name,{"tasks":qs})
    
@method_decorator(sign_required,name="dispatch")
class TaskDetailView(View):
    model=Task
    template_name="task-detail.html"

    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Task.objects.get(id=id)
        return render(request,self.template_name,{"task":qs})
    
@method_decorator(sign_required,name="dispatch")
class TaskEditView(View):

    model=Task
    form_class=TaskEditForm
    template_name="task-edit.html"

    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Task.objects.get(id=id)
        form=self.form_class(instance=qs)
        return render(request,self.template_name,{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Task.objects.get(id=id)
        form=self.form_class(instance=qs,data=request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            messages.success(request,"Task details has been updated")
            return redirect("task-detail",pk=id)
        messages.error(request,"failed to update")
        return render(request,self.template_name)
        

# class TaskDeleteView(View):
#      model=Task
#      template_name="task-list"


#      def get(self,request,*args,**kwargs):
#          id=kwargs.get("pk")
#          qs=Task.objects.get(id=id).delete()
#          messages.success(request,"task has been deleted")
#          return redirect(self.template_name)

@sign_required    
def taskdelete_view(request,*args,**kwargs):
         id=kwargs.get("pk")
         qs=Task.objects.get(id=id).delete()
         messages.success(request,"task has been deleted")
         return redirect("task-list")

     

def signoutview(request,*args,**kwargs):
    logout(request)
    messages.success(request,"logged out")
    return redirect("signin")
    
   




    
