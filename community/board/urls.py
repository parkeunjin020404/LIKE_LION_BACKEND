from django.urls import path
from . import views
from .views import *

app_name = 'board'

urlpatterns = [
    path('', community_list),
    path('post/create/', community_list, name='community_list_post'),
    path('post/detail/<int:pk>/', community_detail, name='community_detail_get'),
    path('post/update/<int:pk>/', community_detail, name='community_detail_put'),
    path('post/delete/<int:pk>/', community_detail, name='community_detail_delete'),
    path('comment/create/<int:post_id>/',create_comment ),
    path('comment/list/<int:post_id>/', get_comments ),
    
]