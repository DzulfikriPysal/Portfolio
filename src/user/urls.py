from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('loggedInUser/', views.loggedInUser, name='loggedInUser'),
    path('logout/', views.logout_view, name="logout"),
    path('post_page/', views.PostList, name='post_page'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]