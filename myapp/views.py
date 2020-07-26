from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone

# Create your views here
def main(request):
    blog = Blog.objects.all().order_by("-id")
    return render(request, "main.html", {"blog": blog})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, "detail.html", {"blog_detail": blog})


def google_move(request):
    return redirect("https://www.naver.com/")


def new(request):
    if request.method == "POST":
        blog = Blog()
        blog.title = request.POST["title"]
        blog.body = request.POST["body"]
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect("/myapp/detail/" + str(blog.id))
    else:
        return render(request, "new.html")


def renew(request, blog_id):
    if request.method == "POST":
        blog = get_object_or_404(Blog, pk=blog_id)
        blog.title = request.POST["title"]
        blog.body = request.POST["body"]
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect("/myapp/detail/" + str(blog_id))
    else:
        blog = get_object_or_404(Blog, pk=blog_id)
        return render(request, "renew.html", {"renew_blog": blog})


def remove(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect("/myapp/")
