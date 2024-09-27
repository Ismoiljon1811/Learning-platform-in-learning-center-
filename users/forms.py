from django import forms
from .models import User, Student, Teacher


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Username"}))
    password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", "placeholder": "Password"}))


class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Name"}))
    phone_number = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Phone Number"}))
    first_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Last Name"}))
    password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", "placeholder": "Password"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", "placeholder": "Confirm Password"}))
    user_role = forms.Select(attrs={'class': "form-control"})

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'first_name', 'last_name', 'password', 'confirm_password', 'user_role')

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return password


class ProfileEditForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    first_name = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    last_name = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput({"class": "form-control"}))
    address = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    phone_number = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    image = forms.ImageField(widget=forms.FileInput({"class": "form-control"}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'address', 'phone_number', 'image')


class StudentEditForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput({"class": "form-control"}))
    class Meta:
        model = Student
        fields = ('date_of_birth', 'team')


class ResetPasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", 'placeholder': 'Old Password'}))
    new_password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", 'placeholder': 'New Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", 'placeholder': 'Confirm Password'}))

    def clean_confirm_password(self):
        new_password = self.cleaned_data['new_password']
        confirm_password = self.cleaned_data['confirm_password']

        if new_password!= confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return new_password
    

class TeacherEditForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = ('user',)