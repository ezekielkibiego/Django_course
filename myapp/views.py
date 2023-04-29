from django.shortcuts import render,redirect
from .models import Blog
from .forms import BlogForm


def index(request):
    # ctx = {"message": "Hello, Good Evening!"}
    
    return render(request, "index.html")

def contact(request):
    # ctx = {"message": "Hello, Good Evening!"}
    
    return render(request, "contact.html")

def blog_list(request):
    blogs = Blog.objects.all()
    
    context = {'blogs': blogs }
    return render(request, 'blog_list.html', context)

def add_blog(request):
    
    if request.method == 'POST':

        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            

            form.save()
           
            form = BlogForm()


            return redirect('/blog')

    else:

        form = BlogForm()
        
    context = {'form': form }
    return render(request, 'addblog.html', context)
        

def error_404(request, exception):
    return render(request, '404.html')