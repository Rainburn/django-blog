from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_list, name="blog_list"),
    path("blog/<int:pk>", views.blog_entries, name="blog_entries"),
    path("entry/new", views.entry_new, name="entry_new"),
    path("entry/<int:pk>/edit", views.entry_edit, name="entry_edit"),
    path("user/add", views.add_new_user, name="add_user")
]
