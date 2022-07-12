from django.urls import path
from django.urls import reverse

from . import views
urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("", views.posts, name="post-page" ),
    path("posts/<slug>/", views.post_detail, name="post-detail-page")#/ post/my-first-post
    

]
