from datetime import date 
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.urls import reverse
from django.template import Template
from .models import Post
from .models import New

from django.views.generic import ListView
from .forms import CommentForm
from django.views import View








# Create your views here.

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data= queryset[:3]
        return data


# def starting_page(request):
#     latest_posts= Post.objects.all().order_by("-date")[:3]
  
#     return render(request, "blog/index.html", {
#         "posts" : latest_posts
#     })


class AllPostsView(ListView):
    model =Post
    template_name = "blog/all-posts.html"
    ordering =["-data"]
    context_object_name="all_posts"


# def posts(request):
#     all_posts= Post.objects.all().order_by("-date")
#     return render(request, "blog/all-post.html", {
#         "all_posts": all_posts
#     })


class SinglePostView(View):
    model = Post
    template_name = "blog/post-detail.html"

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments":post.comments.all().order_by("-id")
        }
        return render(request, "blog/post-detail.html", context)


    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post= Post.objects.get(slug=slug)

        if comment_form.is_valid():
           comment = comment_form.save( commit=False)
           comment.post= post
           comment.save()



           return HttpResponsePermanentRedirect(reverse("post-detail-page", args=[slug]))

        
 
        context = {
                "post": post,
                "post_tags": post.tags.all(),
                "comment_form": Comment_Form(),
                "comments":post.comments.all().order_by("-id")
            }
        return render(request, "blog/post-detail.html", context)

class ReadLaterView(View):
    def get(self, request):
        stored_post = request.session.get("stored_post")

        context = {}

        if stored_post is None or len(stored_post) == 0:
            context["posts"] =[]
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in = stored_post)
            context["posts"] = posts
            context["has_posts"] = True
        
        return render(request, "blog/stored_post.html", context)

    def post(self, request):
        stored_post = request.session.get("stored_post")

        if stored_post is   None:
            stored_post = []
        
        post_id = int(request.POST["post_id"])

        if post_id not in stored_post:
            stored_post.append(post_id)
            request.session["stored_post"] = stored_post

        return HttpResponseRedirect("/")

class New(ListView):
   template_name = "blog/New.html"
   model = New
   context_object_name = "New"
   


        
































        
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["post_tags"] = self.object.tags.all()
    #     context["comment_form"] = CommentForm()
    #     return context


# def post_detail(request,slug):
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post-detail.html",{
#         "post": identified_post,
#         "post_tags": identified_post.tags.all()
       
        
        

#     })