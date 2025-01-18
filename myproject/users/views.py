from django.shortcuts import render, redirect # after successfully submitted it will  redirect to post list
from django.contrib.auth.forms import UserCreationForm # importing a form

# Create your views here.
def register_view(request):
    # if the form has been submitted, this function will handle this request
    if request.method == "POST":
        form = UserCreationForm(request.POST) #form validation
        if form.is_valid(): # will validate if true
                form.save()
                return redirect("posts:list")
    else:
         form = UserCreationForm()
    form = UserCreationForm()
    return render(request, "users/register.html", { "form": form })