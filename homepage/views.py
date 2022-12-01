from django.shortcuts import render

from blog.models import Post

def index(request):
    posts = Post.objects.order_by('-created_date')[:3]
    context = {
        'posts': posts,
    }
    return render(request, 'homepage/index.html', context)