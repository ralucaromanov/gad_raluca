from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail, name='post_detail')
    #path('ratings/', include('star_ratings.urls', namespace='ratings'), name='ratings'),


]