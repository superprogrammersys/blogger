from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from . import forms
from .models import post,User
# Create your views here.
def index(r):
    return render(r,"main/index.html")
def login(r):
    if r.method=="POST":
        frm=forms.login_form(r.POST)
        if frm.is_valid():
            username=frm.cleaned_data["username"]
            password=frm.cleaned_data["password"]
            user=auth.authenticate(r,username=username,password=password)
            if user:
                auth.login(r,user)
                return redirect("index")
    frm=forms.login_form()
    return render(r,"main/login.html",{"form":frm})
@login_required
def logout(r):
    auth.logout(r)
    return redirect("index")
def register(r):
    if r.method=="POST":
        frm=forms.register_form(r.POST)
        if frm.is_valid():
            username=frm.cleaned_data["username"]
            email=frm.cleaned_data["email".lower()]
            password=frm.cleaned_data["password"]
            if not User.objects.filter(username=username).exists() and not User.objects.filter(email=email).exists():
                user=User.objects.create_user(username,email,password)
                auth.login(r,user)
                return redirect("index")
    frm=forms.register_form()
    return render(r,"main/register.html",{"form":frm})
def posts(r):
    ps=post.objects.all().order_by("-publish_date")
    return render(r,"main/posts.html",{"posts":ps})
def show_post(r,pk):
    if r.method=="POST":
        frm=forms.new_comment_form(r.POST)
        if frm.is_valid():
            content=frm.cleaned_data["content"]
            p=post.objects.get(pk=pk)
            p.comments.create(user=r.user,content=content)
            return redirect("post",pk)
    p=get_object_or_404(post,pk=pk)
    comments=p.comments.all()
    frm=forms.new_comment_form()
    return render(r,"main/post.html",{"post":p,"form":frm,"comments":comments})
@login_required
def new_post(r):
    if r.method=="POST":
        frm=forms.new_postForm(r.POST)
        if frm.is_valid():
            title=frm.cleaned_data["title"]
            body=frm.cleaned_data["body"]
            p=post.objects.create(user=r.user,title=title,body=body)
        return redirect("post",p.pk)
    frm=forms.new_postForm()
    return render(r,"main/new_post.html",{"form":frm})