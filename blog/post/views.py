
from django.shortcuts import render
from .models import Post

# Create your views here.      

def posts_list(request):
    queryset = Post.objects.all()
    return render(request, 'listing.html', {'posts':queryset})