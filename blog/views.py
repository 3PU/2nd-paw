from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm

def get_blog_posts(request):
    """
    Creates a view that will return a list of all blog posts,
    published prior to now and render them to 'blogposts.html' template
    """

    blog_post = BlogPost.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "blogposts.html", {'blog_post': blog_post})


@login_required
def create_blog_post(request):
    """Creates a view that allows the user to create a blog post"""
    if request.method == "POST":
        blog_form = BlogPostForm(request.POST, request.FILES)

        if blog_form.is_valid():
            blog_post = blog_form.save(commit=False)            
            blog_post.author = request.user
            blog_post.save()
            return redirect("get_blog_posts")
        
        else:
            blog_form = BlogPostForm()
    
    else:
        blog_form = BlogPostForm()
    
    return render(request, "create_blogpost.html", {'blog_form': blog_form})