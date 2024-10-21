from django.shortcuts import render,redirect
from . forms import RegistrationForm,PostForm
from django.contrib.auth import login
from . models import Post
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    posts=Post.objects.all()
    context={"posts":posts}
    return render(request,"app/index.html",context)

def signup(request):
    if request.method == "POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/')
    else:
        form=RegistrationForm()

    return render(request,"registration/signup.html",{'form':form})

@login_required(login_url="/login")
def create_post(request):
    if request.method == "POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect("/")
    else:
        form=PostForm()

    return render(request,"app/create_post.html",{"form":form})
