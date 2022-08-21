"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from rosters import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genre_list/', views.GenreList.as_view()),
    path('genre/<int:pk>/', views.GenreDetailView.as_view()),
    path('genre_delete/<int:pk>/', views.GenreDeleteView.as_view()),
    path('add_genre/', views.GenreAddView.as_view()),
    path('author_list/', views.AuthorList.as_view()),
    path('author/<int:pk>/', views.AuthorDetailView.as_view()),
    path('author_delete/<int:pk>/', views.AuthorDeleteView.as_view()),
    path('add_author/', views.AuthorAddView.as_view()),
    path('series_list/', views.SeriesList.as_view()),
    path('series/<int:pk>/', views.SeriesDetailView.as_view()),
    path('series_delete/<int:pk>/', views.SeriesDeleteView.as_view()),
    path('add_series/', views.SeriesAddView.as_view()),
    path('publ_list/', views.Publ_houseList.as_view()),
    path('publ/<int:pk>/', views.Publ_houseDetailView.as_view()),
    path('publ_delete/<int:pk>/', views.Publ_houseDeleteView.as_view()),
    path('add_publ/', views.Publ_houseAddView.as_view()),
]
