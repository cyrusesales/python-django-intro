from django.shortcuts import render, redirect # after successfully submitted it will  redirect to post list
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # importing a form
from django.contrib.auth import login # contrib.auth to log user in

# Create your views here.
def register_view(request):
    # if the form has been submitted, this function will handle this request
    if request.method == "POST":
        form = UserCreationForm(request.POST) #form validation
        if form.is_valid(): # will validate if true
                login(request, form.save()) # this will return user value
                return redirect("posts:list")
    else:
         form = UserCreationForm()
    form = UserCreationForm()
    return render(request, "users/register.html", { "form": form })

def login_view(request):
    if request.method == "POST":
          form = AuthenticationForm(data=request.POST)
          if form.is_valid():
               login(request, form.get_user()) # login to request and it will return user
               return redirect("posts:list")
    else: # GET request
         form = AuthenticationForm()
    return render(request, "users/login.html", { "form": form })