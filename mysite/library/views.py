from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse

from .models import Blog, Author, Entry
from .forms import EntryForm, AuthorForm

# Create your views here.
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, "library/blog_list.html", {"blogs": blogs})

def blog_entries(request, pk):
    entries = Entry.objects.filter(blog_id=pk).prefetch_related("authors").all()
    authors = {}
    for entry in entries:
        authors[entry.id] = entry.authors

    return render(request, "library/entry_list.html", {"entries": entries, "authors": authors})


def entry_new(request):
    if (request.method == "POST"):
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.pub_date = timezone.now()

            blog_id = request.POST["blog"]
            entry.save()
            form.save_m2m()

            if (blog_id != ""):
                return redirect("blog_entries", pk=blog_id)
            else:
                return redirect("blog_list")
    else:
        form = EntryForm()

    return render(request, "library/entry_edit.html", {"form": form})


def entry_edit(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if (request.method == "POST"):
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.pub_date = timezone.now()

            blog_id = request.POST["blog"]
            entry.save()
            form.save_m2m()

            if (blog_id != ""):
                return redirect("blog_entries", pk=blog_id)
            else:
                return redirect("blog_list")

    else:
        form = EntryForm(instance=entry)

    return render(request, "library/entry_edit.html", {"form": form})


def add_new_user(request):
    if (request.method == "POST"):
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.save()

            return redirect("blog_list")
    else:
        form = AuthorForm()

    return render(request, "library/author_edit.html", {"form": form})