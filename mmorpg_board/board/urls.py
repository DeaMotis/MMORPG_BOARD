from django.urls import path
from .views import PostList, PostItem, PostCreate, PostEdit, PostDelete, CommentList, CommentDetail, CommentEdit, \
    CommentDelete, AddComment

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostItem.as_view(), name='post_item'),

    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

    path('responses/', CommentList.as_view(), name='comments'),
    path('response/<int:pk>/', CommentDetail.as_view(), name='one_comment'),
    path('response/<int:pk>/edit/', CommentEdit.as_view(), name='comment_edit'),
    path('response/<int:pk>/delete/', CommentDelete.as_view(), name='comment_delete'),
    path('response/create/', AddComment.as_view(), name='add_comment')
]
