from django.contrib import admin
from django.urls import path,include
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
      path(r'^', include('django.contrib.auth.urls')),

      path('home/', views.HomeView.as_view()),
      path('about/', views.AboutView.as_view()),
      path('contact/', views.ContactView.as_view()),
      path('profile/edit/<int:pk>', views.MyProfileUpdateView.as_view(success_url="/home")),

      path('mypost/create/', views.MyPostCreate.as_view(success_url="/mypost")),
      path('mypost/', views.MyPostListView.as_view()),
      path('mypost/delete/<int:pk>', views.MyPostDeletelView.as_view(success_url="/mypost")),
      path('mypost/<int:pk>',views.MyPostDetailView.as_view()),

      path('myprofile/', views.MyProfileListView.as_view()),
      path('myprofile/<int:pk>', views.MyProfileDetailView.as_view()),

      path('myprofile/follow/<int:pk>', views.follow),
      path('myprofile/unfollow/<int:pk>',views.unfollow),

      path('mypost/like/<int:pk>', views.like),
      path('mypost/unlike/<int:pk>', views.unlike),


      path('',RedirectView.as_view(url="home/")),



]
# path('notice/',views.NoticeListView.as_view()),

# path('',RedirectView.as_view(url="notice"))