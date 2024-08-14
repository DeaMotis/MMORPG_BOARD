from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .forms import PostForm
from .models import Post, Response
from .filters import PostFilter  # Импортируем фильтр


class PostList(ListView):
    model = Post
    template_name = 'board/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10  # Пагинация

    def get_queryset(self):
        queryset = super().get_queryset()
        # Примените фильтрацию
        self.filterset = PostFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs  # Возвращаем отфильтрованные результаты


def board_list(request):
    posts = Post.objects.all()
    filterset = PostFilter(request.GET, queryset=posts)

    paginator = Paginator(filterset.qs, 10)  # Пагинация
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'board/post_list.html', {
        'posts': page_obj.object_list,
        'filterset': filterset,
        'page_obj': page_obj,
    })


class PostItem(DetailView):
    model = Post
    template_name = 'board/post_item.html'
    context_object_name = 'post'  # Исправляем имя для единообразия

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = self.kwargs.get('pk')
        context['respond'] = "Откликнулся" if Response.objects.filter(author=self.request.user, post_id=post_id) else "Мое_объявление" if self.request.user == self.get_object().author else None
        return context


class PostCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('board.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'board/post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        return super().form_valid(form)


class PostEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('board.change_post',)
    model = Post
    form_class = PostForm
    template_name = 'board/post_edit.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('board.delete_post',)
    model = Post
    template_name = 'board/post_delete.html'
    success_url = reverse_lazy('post_list')


class CommentList(PermissionRequiredMixin, ListView):
    model = Response
    template_name = 'board/responses.html'
    context_object_name = 'comments'
    permission_required = 'board.add_response'
    paginate_by = 10


class CommentDetail(PermissionRequiredMixin, DetailView):
    model = Response
    template_name = 'board/comment_detail.html'
    context_object_name = 'one_comment'


class CommentDelete(DeleteView):
    model = Response
    template_name = 'board/comment_delete.html'
    success_url = reverse_lazy('post')


class CommentEdit(UpdateView):
    model = Response
    template_name = 'board/comment_edit.html'
    success_url = reverse_lazy('post')


class AddComment(PermissionRequiredMixin, CreateView):
    model = Response
    template_name = 'board/add_comment.html'
    success_url = reverse_lazy('post')