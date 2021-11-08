from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Article
# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Article
    fields = ['title', 'summary', 'body', 'photo']
    template_name = 'article_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # obj = self.get_object()
        return self.request.user.is_superuser

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Article
    fields = ['title', 'summary', 'body', 'photo']
    success_url = reverse_lazy('article_list')
    template_name = 'article_update.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Article
    success_url = reverse_lazy('article_list')
    template_name = 'article_delete.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
   