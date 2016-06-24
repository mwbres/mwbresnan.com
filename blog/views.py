from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import BlogPost, Quote, Comment
from rest_framework import generics, viewsets
from .serializers import BlogSerializer
from django.core import serializers
from django.db.models import Max
from mwbresnan.contactcontroller import send_new_comment_message


def main_posts(req):
    return render(req, 'main/post.html')


def post_detail(req, pk):
    try:
        BlogPost.objects.get(pk=pk)
        return render(req, 'main/post.html')
    except BlogPost.DoesNotExist:
        return render(req, 'masters/404.html')


def not_found(req):
    return render(req, 'masters/404.html')


def recent(req):
    data = BlogPost.objects.all().order_by('-date')[:3]
    data = serializers.serialize("json", data)
    return HttpResponse(data)


def all(req):
    data = BlogPost.objects.all().order_by('-date')
    data = serializers.serialize("json", data)
    return HttpResponse(data)


def quote(req):
    random_quote = [Quote.objects.order_by('?').first()]
    quote = serializers.serialize("json", random_quote)
    return HttpResponse(quote)


def single(req, pk):
    post = BlogPost.objects.get(pk=pk)
    post = serializers.serialize("json", [post])
    return HttpResponse(post)


def get_comments(req, pk):
    selectedPost = get_object_or_404(BlogPost, pk=pk)
    data = Comment.objects.filter(post_id=selectedPost).order_by('-date')
    data = serializers.serialize("json", data)
    return HttpResponse(data)


def add_comment(req, pk):
    selectedPost = get_object_or_404(BlogPost, pk=pk)
    send_new_comment_message(selectedPost.title)
    Comment.objects.create(post_id=selectedPost, name=req.POST['name'], text=req.POST['text'])
    return HttpResponse()
