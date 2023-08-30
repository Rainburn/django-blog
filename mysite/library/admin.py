from django.contrib import admin
from .models import Blog, Author, Entry

# Register your models here.
class AuthorInline(admin.TabularInline):
    model = Entry.authors.through
    extra = 1

class EntryInLine(admin.TabularInline):
    model = Entry
    extra = 1

class BlogAdmin(admin.ModelAdmin):
    list_display = ["name", "tagline"]
    fields = ["name", "tagline"]
    inlines = [EntryInLine]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
    fields = ["name", "email"]


class EntryAdmin(admin.ModelAdmin):
    fields = ["headline", "body_text", "pub_date", "number_of_comments", "number_of_pingbacks", "rating"]
    inlines = [AuthorInline]

admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Entry, EntryAdmin)
