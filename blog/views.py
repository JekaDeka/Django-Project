from django.shortcuts import redirect, render

from .models import BlogPost


def blog_post_list(request):
    posts = BlogPost.objects.filter(is_publish=True)
    context = {"posts": posts}
    return render(request, "blog/blog_list.html", context)


def blog_post_detail(request, pk):
    try:
        post = BlogPost.objects.get(pk=pk)
    except BlogPost.DoesNotExist:
        return redirect("/")
    context = {"post": post}
    return render(request, "blog/blog_detail.html", context)
