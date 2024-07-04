from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DeleteView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse
from .forms import CommentForm
from django.views.generic.edit import (
    UpdateView, 
    DeleteView,
    CreateView,)

from django.urls import reverse_lazy
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name='article_list.html'

class ArticleDetailView(DeleteView):
    model = Article
    template_name='article_detail.html'

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = (
        "title",
        "body",
    )
    template_name='article_update.html'
    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name='article_delete.html'
    success_url = reverse_lazy("article_list")
    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_create.html'
    fields = (
        "title",
        "body",
    )
    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)
    
# class CommentPost(LoginRequiredMixin, SingleObjectMixin, FormView):
#     model = Article
#     template_name = "article_detail.html"
#     form_class = CommentForm

#     def get_object(self, queryset=None):
#         return super().get_object(queryset=queryset)

#     def form_valid(self, form):
#         self.object = self.get_object()
#         form.instance.article = self.object
#         # Set the author of the comment to the current user
#         form.save(author=self.request.user)
#         return super().form_valid(form)

#     def get_success_url(self):
#         # Redirect to the article detail page after successfully posting a comment
#         return reverse("article_detail", kwargs={"pk": self.object.pk})

#     def test_func(self):
#         obj = self.get_object()
#         return obj.author == self.request.user

class CommentPost(LoginRequiredMixin, SingleObjectMixin, FormView):
    model = Article
    template_name = "article_detail.html"
    form_class = CommentForm

    def get_object(self, queryset=None):
        return super().get_object(queryset=queryset)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.article = self.object
        form.save(author=self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("article_detail", kwargs={"pk": self.object.pk})

    def test_func(self):
        return self.get_object().author != self.request.user



