from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(visibleYn=True).order_by('created_date')
    return render(request, './index.html', {'posts': posts})