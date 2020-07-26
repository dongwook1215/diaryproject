from django.shortcuts import render, redirect
from .models import Profile

# Create your views here.


def index(request):
    return render(request, "index.html")


def upload(request):
    if request.method == "POST":
        form = Profile()
        form.title = request.POST["title"]
        try:
            form.image = request.FILES["image"]
        except:
            pass
        form.save()
        return redirect("/upload_result/")
    else:
        return render(request, "upload.html")


def upload_result(request):
    profile = Profile.objects.all()
    return render(request, "upload_result.html", {"profile": profile})

