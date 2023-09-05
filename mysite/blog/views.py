from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm, PostModelForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).select_related('author')
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})


def post_new(request):
    if (request.method == "POST"):
        form = PostModelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("post_detail", pk=post.pk)

    else:
        form = PostModelForm()

    return render(request, "blog/post_edit.html", {"form": form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if (request.method == "POST"):
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("post_detail", pk=pk)

    else:
        form = PostModelForm(instance=post)

    return render(request, "blog/post_edit.html", {"form": form})



def post_edit_nonmodel(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if (request.method == "POST"):
        data = {
            "title": request.POST["title"],
            "text": request.POST["text"]
        }
        form = PostModelForm(data)
        if form.is_valid():
            post.title = form.cleaned_data["title"]
            post.text = form.cleaned_data["text"]
            post.published_date = timezone.now()
            post.save()
            return redirect("post_detail", pk=pk)

    else:
        data = {
            "title": post.title,
            "text": post.text
        }
        form = PostForm(data)

    return render(request, "blog/post_edit.html", {"form": form})