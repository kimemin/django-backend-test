from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.core import serializers
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(visibleYn=True).order_by('created_date')
    return render(request, './index.html', {'posts': posts})

def post_list_byJson(request):
    posts = Post.objects.filter(visibleYn=True).order_by('created_date')
    return HttpResponse(serializers.serialize('json', posts))