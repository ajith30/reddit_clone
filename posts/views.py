from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from django.views.generic import ListView # -->CBV
from django.utils import timezone

# Create your views here.

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url']:
            post = Post()
            post.title = request.POST['title']
            if request.POST['url'].startswith('http://') or  request.POST['url'].startswith('https://'):
                post.url = request.POST['url']
            else:
                post.url ='http://' + request.POST['url']
            post.pub_date = timezone.datetime.now()
            post.author = request.user
            post.save()
            return redirect('home')
        else:
            return render(request, 'posts/create.html',{'error':'ERROR:You must include TITLE and URL to create a post.'})

    else:
        return render(request, 'posts/create.html')

"""
def home(request):
    posts = Post.objects.order_by('-votes_total')
    return render(request,'posts/home.html', {'posts':posts})
"""
class HomePage(ListView):
    model = Post
    template_name = 'posts/home.html'

    def get_queryset(self):
        return Post.objects.order_by('-votes_total')

def upvote(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.votes_total += 1
        post.save()
        return redirect('home')

def downvote(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.votes_total -= 1
        post.save()
        return redirect('home')
# you can name pk as anything.But you need to specify the same name in url

def userposts(request, pk):
    posts = Post.objects.filter(author__id=pk ).order_by('-votes_total')
    author = User.objects.get(pk=pk)
    return render(request,'posts/user.html',{'posts':posts, 'author':author})
    #return render(request, 'posts/user.html', {'posts':posts})
