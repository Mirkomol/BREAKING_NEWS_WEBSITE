from django.urls import path
from .views import (PostListView,
                    PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,LikeView,
                    ItListView, ItPostDetailView, ItCreateView, ItUpdateView, ItDeleteView, ItLikeView,  BusinessPostDetailView,
                    BusinessPostListView, BusinessPostDeleteView, BusinessPostUpdateView, BusinessPostCreateView,
                    SportPostListView, SportPostDetailView, SportPostCreateView, SportPostUpdateView,
                    SportPostDeleteView, TravelPostDeleteView, TravelPostUpdateView, TravelPostCreateView,
                    TravelPostDetailView, TravelPostListView, UserPostListView, ItUserPostListView,
                    TravelUserPostListView, SportUserPostListView, BusinessUserPostListView, BusinessLikeView ,
                    SportLikeView, TravelLikeView
                    )
from .import views

urlpatterns = [

    # Home
    path('', PostListView.as_view(), name = 'index' ),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name = 'post-detail' ),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name = 'post-update' ),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('like/<int:pk>', LikeView, name='like_post'),

    # It
    path('it_news/',ItListView.as_view(), name='it_news'),
    path('it_news/user/<str:username>', ItUserPostListView.as_view(), name='it-user-posts'),
    path('it_news/post/<int:pk>', ItPostDetailView.as_view(), name='it-post-detail'),
    path('it_news/new/', ItCreateView.as_view(), name='it-post-create'),
    path('it_news/post/<int:pk>/update', ItUpdateView.as_view(), name='it-post-update'),
    path('it_news/post/<int:pk>/delete', ItDeleteView.as_view(), name='it-post-delete'),
    path('it_news/it_like/<int:pk>', ItLikeView, name='it_like_post'),

    # Business
    path('business/', BusinessPostListView.as_view(), name='business'),
    path('business/user/<str:username>', BusinessUserPostListView.as_view(), name='business-user-posts'),
    path('business/post/<int:pk>', BusinessPostDetailView.as_view(), name='business-post-detail'),
    path('business/new/',  BusinessPostCreateView.as_view(), name='business-post-create'),
    path('business/post/<int:pk>/update',  BusinessPostUpdateView.as_view(), name='business-post-update'),
    path('business/post/<int:pk>/delete', BusinessPostDeleteView.as_view(), name='business-post-delete'),
    path('business/business_like/<int:pk>', BusinessLikeView, name='business_like_post'),

    # Sports
    path('sports/', SportPostListView.as_view(), name='sports'),
    path('sports/user/<str:username>', SportUserPostListView.as_view(), name='sport-user-posts'),
    path('sports/post/<int:pk>', SportPostDetailView.as_view(), name='sport-post-detail'),
    path('sports/new/', SportPostCreateView.as_view(), name='sport-post-create'),
    path('sports/post/<int:pk>/update', SportPostUpdateView.as_view(), name='sport-post-update'),
    path('sports/post/<int:pk>/delete', SportPostDeleteView.as_view(), name='sport-post-delete'),
    path('sports/sport_like/<int:pk>', SportLikeView, name='sport_like_post'),

    # Travel
    path('travel/', TravelPostListView.as_view(), name='travel'),
    path('travel/user/<str:username>', TravelUserPostListView.as_view(), name='travel-user-posts'),
    path('travel/post/<int:pk>', TravelPostDetailView.as_view(), name='travel-post-detail'),
    path('travel/new/', TravelPostCreateView.as_view(), name='travel-post-create'),
    path('travel/post/<int:pk>/update', TravelPostUpdateView.as_view(), name='travel-post-update'),
    path('travel/post/<int:pk>/delete', TravelPostDeleteView.as_view(), name='travel-post-delete'),
    path('travel/travel_like/<int:pk>', TravelLikeView, name='travel_like_post'),


   # Contact and About

    path('contact/', views.contact, name='contact'),

    path('aboutus/', views.aboutus, name='aboutus'),
]
