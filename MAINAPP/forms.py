from django import forms
from django.contrib.auth.models import User
from MAINAPP.models import UserProfileInfo , Subscriber ,UserFeedback ,WorkshopEnrollment

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email' , 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields =('name','phone',)

class  SubscriberForm(forms.ModelForm):
    class Meta():
        model =  Subscriber
        fields =('name','email',)

class  UserFeedbackForm(forms.ModelForm):
    class Meta():
        model =  UserFeedback
        fields =('reviewer_name','reviewer_email','reviewer_message',)

class Workshop_EnrollmentForm(forms.ModelForm):
    class Meta():
        model =  WorkshopEnrollment
        fields =('participant_name','participant_email','participant_phone',)
