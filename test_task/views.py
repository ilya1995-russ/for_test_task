from django.shortcuts import render, redirect
from test_task.models import Article, AuthorUser
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


def index(req):
    return render(req, 'index.html')


class RegisterForm(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('index')


class ArticleView(ListView):
    model = Article
    template_name = 'index.html'


class DetailArticleView(DetailView, LoginRequiredMixin):
    login_url = 'login'
    model = Article
    # model = AuthorUser
    template_name = 'detail_article.html'


class CreateArticleView(CreateView, PermissionRequiredMixin):
    permission_required = 'test_task.add_article'
    login_url = 'login'
    model = Article
    template_name = 'create_article.html'
    fields = "__all__"


class UpdatelArticleView(UpdateView, PermissionRequiredMixin):
    permission_required = 'test_task.change_article'
    login_url = 'login'
    model = Article
    template_name = 'update_article.html'
    fields = "__all__"


class DeleteArticleView(DeleteView, PermissionRequiredMixin):
    permission_required = 'test_task.delete_article'
    login_url = 'login'
    model = Article
    template_name = 'delete_article.html'
    success_url = reverse_lazy('index')
