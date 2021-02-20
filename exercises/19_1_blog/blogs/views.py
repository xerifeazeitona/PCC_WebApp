from django.shortcuts import render, redirect

from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    """The home page for blogs."""
    blog_posts = BlogPost.objects.order_by('date_added')
    context = {'blog_posts': blog_posts}
    return render(request, 'blogs/index.html', context)

def post(request, post_id):
    """Show a single post."""
    post = BlogPost.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'blogs/post.html', context)

def new_post(request):
    """Add a new blog post."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogPostForm()
    else:
        # POST data submitted; process data.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

def edit_post(request, post_id):
    """Edit an existing blog post."""
    post = BlogPost.objects.get(id=post_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogPostForm(instance=post)
    else:
        # POST data submitted; process data.
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:post', post_id=post.id)

    # Display a blank or invalid form.
    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)
