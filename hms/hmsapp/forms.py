from django import forms
from .models import User,Booking,Feedback,Payment,Staff,RoomFee
from django.contrib.auth.forms import UserCreationForm
from datetime import date

class UserForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Confirm Password"}))
    class Meta:
        model=User
        fields=["username","email"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Username"}),
            "email":forms.EmailInput(attrs={"class":"form-control my-2","placeholder":"Email Id"}),
        }

class AdUserForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Confirm Password"}))
    class Meta:
        model=User
        fields=["username","role1","role2","email"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Username"}),
            "role1":forms.Select(attrs={"class":"form-control mt-2"}),
            "role2":forms.Select(attrs={"class":"form-control my-2"}),
            "email":forms.EmailInput(attrs={"class":"form-control my-2","placeholder":"Email Id"}),
        }


class AdupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","role1","role2","email"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Username","readonly":"true"}),
            "role1":forms.Select(attrs={"class":"form-control my-2"}),
            "role2":forms.Select(attrs={"class":"form-control my-2"}),
            "email":forms.EmailInput(attrs={"class":"form-control my-2","placeholder":"Email Id","readonly":"true"}),
        }


class UPForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","mbl","gndr","pfimag","adrs","dob"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control my-2","readonly":"true"}),
            "first_name":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"First Name"}),
            "last_name":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Last Name"}),
            "email":forms.EmailInput(attrs={"class":"form-control my-2","readonly":"true"}),
            "mbl":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Mobile Number"}),
            "adrs":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Permanent Address"}),
            "dob":forms.DateInput(attrs={"class":"form-control my-2","type":"date"}),
            "gndr":forms.Select(attrs={"class":"form-control my-2"}),
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=["rbtype","startdate","enddate","idproof","idatch"]
        widgets={
            "rbtype":forms.Select(attrs={"class":"form-control my-3"}),
            "startdate":forms.DateInput(attrs={"class":"form-control my-3","type":"date","min":date.today()}),
            "enddate":forms.DateInput(attrs={"class":"form-control my-3","type":"date","min":date.today()}),
            "idproof":forms.Select(attrs={"class":"form-control my-3"}),
        }

class UpbookForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=["rbstatus","mgdesc"]
        widgets={
            "rbstatus":forms.Select(attrs={"class":"form-control my-3"}),
            "mgdesc":forms.Textarea(attrs={"class":"form-control my-3","rows":3})
        }

class ChangePassForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-3","placeholder":"Password"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-3","placeholder":"Confirm Password"}))
    class Meta:
        model=User
        fields=[]

class FBForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=["fdtp","fd"]
        widgets={
            "fdtp":forms.Select(attrs={"class":"form-control my-3"}),
            "fd":forms.Textarea(attrs={"class":"form-control my-2","rows":3,"placeholder":"write your feedback here..."})
        }

class PayForm(forms.ModelForm):
    class Meta:
        model =Payment
        fields=["payatch"]

class StsalForm(forms.ModelForm):
    class Meta:
        model=Staff
        fields=["stn","sttp","salary","status"]
        widgets={
            "stn":forms.TextInput(attrs={"class":"form-control my-2","readonly":"true"}),
            "sttp":forms.TextInput(attrs={"class":"form-control my-2","readonly":"true"}),
            "salary":forms.TextInput(attrs={"class":"form-control my-2"}),
            "status":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Status"})
        }

class FeeForm(forms.ModelForm):
    class Meta:
        model=RoomFee
        fields=["rtp","rfee"]
        widgets={
            "rtp":forms.Select(attrs={"class":"form-control my-3"}),
            "rfee":forms.TextInput(attrs={"class":"form-control my-3","placeholder":"amount.."})
        }