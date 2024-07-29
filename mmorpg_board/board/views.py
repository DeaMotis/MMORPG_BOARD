from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm
from .models import Post, Response


class PostList(ListView):
    model = Post
    template_name = 'post_list.html'
    ordering = 'title'
    context_object_name = 'posts'


class PostItem(DetailView):
    model = Post
    template_name = 'post_item.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if Response.objects.filter(author_id=self.request.user.id).filter(post_id=self.kwargs.get('pk')):
            context['respond'] = "Откликнулся"
        elif self.request.user == Post.objects.get(pk=self.kwargs.get('pk')).author:
            context['respond'] = "Мое_объявление"
        return context


class PostCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('board.add_Post',)
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.user = None

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        return super().form_valid(form)

    def add_post(request):
        if not request.user.has_perm('board.add_post'):
            raise PermissionDenied


class PostEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('board.change_Post',)
    model = Post
    form_class = PostForm
    template_name = 'post_edit.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('board.delete_Post',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class CommentList(PermissionRequiredMixin, ListView):
    model = Response
    template_name = 'responses.html'
    success_url = reverse_lazy('post_list')
    context_object_name = 'comments'
    permission_required = 'board.add_post'
    paginate_by = 10


class CommentDetail(PermissionRequiredMixin, DetailView):
    model = Response
    template_name = 'comment_detail.html'
    context_object_name = 'one_comment'
    success_url = reverse_lazy('post')
    permission_required = 'board.add_post'


class CommentDelete(DeleteView):
    pass


class CommentEdit(UpdateView):
    pass


class AddComment(PermissionRequiredMixin, CreateView):
    pass