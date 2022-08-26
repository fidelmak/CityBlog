from django.urls import path
from django.urls import reverse

from . import views
urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("", views.AllPostsView.as_view(), name="post-page" ),
    path("posts/<slug>/", views.SinglePostView.as_view(), name="post-detail-page"),#/ post/my-first-post
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),
    path("new", views.New.as_view(), name="new")

    
    

]
