from django import forms
class login_form(forms.Form):
    username=forms.CharField(max_length=12,label="enter your username")
    password=forms.CharField(label="enter your password",widget=forms.PasswordInput())
class register_form(forms.Form):
    username=forms.CharField(max_length=12,label="enter the username")
    email=forms.CharField(label="enter your email make sure that its valid",widget=forms.EmailInput())
    password=forms.CharField(label="enter the password make sure that's strong",widget=forms.PasswordInput())
class new_comment_form(forms.Form):
    content=forms.CharField(label="enter your comment..",widget=forms.Textarea())
class new_postForm(forms.Form):
    title=forms.CharField(max_length=250,label="enter post title")
    body=forms.CharField(label="enter post content",widget=forms.Textarea())