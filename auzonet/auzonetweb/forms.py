from django import forms
from django.forms import ModelForm
from .models import Category, Community, Request, Offer, CommunityMessage

GENDERS = (
    ('M','Male'),
    ('F', 'Female')
)

ACCESS_TYPES = (
    ('PU', 'Public'),
    ('PR', 'Private'),
)

SCOPE = (
    ('COM', 'Community'),
    ('CIT', 'City'),
    ('PRO', 'Province'),
    ('COU', 'Country'),
)

STATUS = (
    ('A', 'Active'),
    ('F', 'Finished'),
)

class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Username', max_length=100)
    password = forms.CharField(required=True, label='Password', max_length=100, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(required=True, label='Username', max_length=100)
    first_name = forms.CharField(required=True, label='Name', max_length=100)
    last_name = forms.CharField(required=True, label='Surname', max_length=100)
    email = forms.EmailField(required=True, label='Email', max_length=100)
    password = forms.CharField(required=True, label='Password', max_length=100, widget=forms.PasswordInput)
    birthdate = forms.DateField(required=True, label='Birthday')
    gender = forms.ChoiceField(required=True, label='Gender', choices=GENDERS)
    avatar = forms.ImageField(required=True, label='Avatar', max_length=100)

class JoinCommunityForm(forms.Form):
    community = forms.ModelChoiceField(queryset=Community.objects.all())

class NewCommunityMsgModelForm(ModelForm):
    class Meta:
        model = CommunityMessage
        fields = ['message_type', 'message_text']

class NewCommunityModelForm(ModelForm):
    class Meta:
        model = Community
        fields = ['address', 'coordinates', 'access_type', 'password', 'welcome_message']

class NewOfferModelForm(ModelForm):
    class Meta:
        model = Offer
        fields = ['category','title','detail','scope','status','price','image']

class NewRequestModelForm(ModelForm):
    class Meta:
        model = Request
        fields = ['category','title','detail','scope','status', 'due_date','reward','image']
