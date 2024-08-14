from django.urls import path
from .views import PostList, PostItem, PostCreate, PostEdit, PostDelete, CommentList, CommentDetail, CommentEdit, \
    CommentDelete, AddComment

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>/', PostItem.as_view(), name='post_detail'),

    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

    path('responses/', CommentList.as_view(), name='comments'),
    # Список комментариев по адресу /board/responses/
    path('response/<int:pk>/', CommentDetail.as_view(), name='one_comment'),
    # Детали комментария по адресу /board/response/<id>/
    path('response/<int:pk>/edit/', CommentEdit.as_view(), name='comment_edit'),
    # Редактирование комментария по адресу /board/response/<id>/edit/
    path('response/<int:pk>/delete/', CommentDelete.as_view(), name='comment_delete'),
    # Удаление комментария по адресу /board/response/<id>/delete/
    path('response/create/', AddComment.as_view(), name='add_comment'),
    # Добавление комментария по адресу /board/response/create/
]

