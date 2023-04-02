from django.shortcuts import render
from django.views.generic import View
 
from geopy.geocoders import Nominatim
 
def get_address(place):
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(place)
    return getLoc.address

def get_addr(latitude,longitude):
    geoLoc = Nominatim(user_agent="GetLoc")
    locname = geoLoc.reverse(latitude,longitude)
    print(locname.address)





from django import forms

class OperationForm(forms.Form):
    num1=forms.IntegerField()
    num2=forms.IntegerField()

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class RegistrationForm(forms.Form):
    firstname=forms.CharField()
    Lastname=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField()

class GeoForm(forms.Form):
    place=forms.CharField()

class GeooForm(forms.Form):
    latitude=forms.IntegerField()
    longitude=forms.IntegerField()

class AdditionView(View):
    def get(self,request,*args,**kwrgs):
        return render(request,"add.html")
    def post(self,request,*args,**kwrgs):
            n1=int(request.POST.get("num1"))
            n2=int(request.POST.get("num2"))
            res=n1+n2
            print(res)
            return render(request,"add.html",{"result":res})
    
    
class SubtractionView(View):
    def get(self,request,*args,**kwrgs):
        return render(request,"sub.html")
    def post(self,request,*args,**kwrgs):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        res=n1-n2
        print(res)
        return render(request,"sub.html",{"result":res})
    
class MultiplicationView(View):
    def get(self,request,*args,**kwrgs):
        return render(request,"mul.html")
    def post(self,request,*args,**kwrgs):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        res=n1*n2
        print(res)
        return render(request,"mul.html",{"result":res})
    
class DivisionView(View):
    def get(self,request,*args,**kwrgs):
        return render(request,"div.html")
    def post(self,request,*args,**kwrgs):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        res=n1/n2
        print(res)
        return render(request,"div.html",{"result":res})
    
class FactorialView(View):
    def get(self,request,*args,**kwrgs):
        return render(request,"fact.html")
    def post(self,request,*args,**kwrgs):
        n=int(request.POST.get("num"))
        fact=1
        for i in range(1,(n+1)):
            fact=fact*i
        return render(request,"fact.html",{"result":fact})
    
class PrimeView(View):
    def get(self,request,*args,**kwrgs):
        return render(request,"prime.html")
    def post(self,request,*args,**kwrgs):
        n=int(request.POST.get("num"))
        f=0
        if n==1:
            print("is not defined")
        else:
            for i in range(1,n+1):
                if n%i==0:
                    f=f+1
            if f==2:
                res=("prime")
            else:
                res=("not prime")
        return render(request,"prime.html",{"result":res})
    

class ArmstrongView(View):
    def get(self,request,*args,**kwrgs):
        return render(request,"armstrong.html")
    def post(self,request,*args,**kwrgs):
        n=int(request.POST.get("num"))
        sum=0
        temp=n
        order=len(str(n))
        while temp>0:
            r=temp%10
            sum=sum+r**order
            temp=temp//10
        res=n==sum
        
        return render(request,"prime.html",{"result":res})
    


class PalindromeView(View):
    def get(self,request,*args,**kwrgs):
        return render(request,"palindrome.html")
    def post(self,request,*args,**kwrgs):
        n=int(request.POST.get("num"))
        rev=0
        temp=n
        while temp>0:
            r=temp%10
            rev=rev*10+r
            temp=temp//10
        res=n==rev

        return render(request,"palindrome.html",{"result":res})
    
class EvenView(View):
    def get(self,request,*args,**kwrgs):
        return render(request,"even.html")
    def post(self,request,*args,**kwrgs):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        evens=[n for n in range(n1,n2) if n%2==0]
        return render(request,"even.html",{"result":evens})
    


class HomeView(View):
    def get(self,request,*args,**kwrgs):
        return render(request,"home.html")
    

class HealthView(View):
    def get(self,request,*args,**kwrgs):
        return render(request,"health.html")
    def post(self,request,*args,**kwrgs):

        tsize=int(request.POST.get("tummy"))
        bsize=int(request.POST.get("buttock"))
        gender=request.POST.get("gender")
        print(tsize,bsize,gender)
        bmi=tsize/bsize
        bmi=round(bmi,2)
        print(bmi)

        context={"gender":"","risk":"","shape":"","bmi":bmi}

        if gender=="male":
            if bmi<=.95:
                context["gender"]="male"
                context["risk"]="low"
                context["shape"]="pear"
            elif bmi>=.96 and bmi<=1:
                context["gender"]="male"
                context["risk"]="moderate"
                context["shape"]="avacado"
            elif bmi>1:
                context["gender"]="male"
                context["risk"]="high"
                context["shape"]="apple"
        else:
            if bmi<=.80:
                context["gender"]="female"
                context["risk"]="low"
                context["shape"]="pear"
            elif bmi>=0.81 and bmi<=0.85:
                context["gender"]="female"
                context["risk"]="moderate"
                context["shape"]="avacado"
            elif bmi>.85:
                context["gender"]="female"
                context["risk"]="high"
                context["shape"]="aapple"
        return render(request,"health.html",context)   
    

class TemperatureView(View):
    def get(self,request,*args,**kwrgs):
        return render(request,"temp.html")
    def post(self,request,*args,**kwrgs):
        dc=float(request.POST.get("degree"))
        fh=(dc * 9/5) + 32
        fh=round(fh,3) 
        print(fh)
        return render(request,"temp.html",{"result":fh})
    
class ExponentView(View):
    def get(self,request,*args,**kwargs):
        form=OperationForm()
        return render(request,"exponent.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=OperationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            result=n1**n2
        return render(request,"exponent.html",{"result":result,"form":form})
       


class LoginView(View):
    def get(self,request,*args,**kwargs):
        login=LoginForm()

        return render(request,"login.html",{"login":login})
    
class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        register=RegistrationForm()
        return render(request,"register.html",{"register":register})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            print("form is invalid")
        return render(request,"register.html")

class GeoView(View):
    def get(self,request,*args,**kwargs):
        form=GeoForm()
        return render(request,"geo.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=GeoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            place=form.cleaned_data.get("place")
            address=get_address(place)
            print(address)
        return render(request,"geo.html",{"form":form})
    
class GeooView(View):
    def get(self,request,*args,**kwargs):
        form=GeooForm()
        return render(request,"geoo.html")
    def post(self,request,*args,**kwargs):
        form=GeooForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            l1=form.cleaned_data.get("latitude")
            l2=form.cleaned_data.get("logitude")
            address=(get_addr.address)
            return render(request,"geoo.html")            




        
    
       


        
    

            




        

        