from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Comment
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_create.html'
    success_url = reverse_lazy('post_list')

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_create.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        post_id = self.kwargs.get('pk')
        post = get_object_or_404(Post, pk=post_id)
        form.instance.post = post
        return super().form_valid(form)
