from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .forms import BlogForm, CommentForm
# Create your views here.


def home(request):
    blogs = Blog.objects
    return render(request, 'blog/home.html', {'blogs': blogs})


def hello(request):
    return render(request, 'blog/hello.html')


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        comment_form.instance.blog_id = blog_id
        if comment_form.is_valid():
            comment = comment_form.save()



    comment_form = CommentForm()
    comments = blog.comments.all()

    return render(request, 'blog/detail.html', {'blog':blog, 'comments':comments, 'comment_form':comment_form})

def new(request):
    return render(request, 'blog/new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)  
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit = False)
            blog.update_date=timezone.now()
            blog.save()
            return redirect('show')
    else:
        form = BlogForm(instance=blog)
    return render(request,'create.html',{'form':form})

def delete(request, pk):
    blog = Blog.objects.get(Blog, pk=pk)
    blog.delete()
    return redirect('show')

def slidebanner(request):
    return render(request, 'blog/slidebanner.html')

