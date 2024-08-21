from typing import Any

from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from posts.models import BlogPost


class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"

    def get_queryset(self) -> QuerySet[Any]:
        QuerySet = super().get_queryset()
        if self.request.user.is_authenticated:
            return QuerySet
        return QuerySet.filter(published=True)


class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "posts/blogpost_create.html"
    fields = [
        "title",
        "content",
        "thumbnail",
    ]


class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "posts/blogpost_edit.html"
    fields = [
        "title",
        "content",
        "published",
        "thumbnail",
    ]


class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "post"


class BlogPostDelete(DeleteView):
    model = BlogPost
    context_object_name = "post"
    success_url = reverse_lazy("posts:home")
