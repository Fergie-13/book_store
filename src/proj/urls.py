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
    path('genre_list/', views.GenreList.as_view(), name="gen-li"),
    path('genre/<int:pk>/', views.GenreDetailView.as_view(), name="gen-det"),
    path('genre_delete/<int:pk>/', views.GenreDeleteView.as_view(), name="gen-del"),
    path('genre_add/', views.GenreAddView.as_view(), name="gen-add"),
    path('genre-edit/<int:pk>/', views.GenreUpdateView.as_view(), name="gen-ed"),
    path('author_list/', views.AuthorList.as_view(), name="aut-li"),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name="aut-det"),
    path('author_delete/<int:pk>/', views.AuthorDeleteView.as_view(), name="aut-del"),
    path('author-edit/<int:pk>/', views.AuthorUpdateView.as_view(), name="aut-ed"),
    path('author_add/', views.AuthorAddView.as_view(), name="aut-add"),
    path('series_list/', views.SeriesList.as_view(), name="ser-li"),
    path('series/<int:pk>/', views.SeriesDetailView.as_view(), name="ser-det"),
    path('series_delete/<int:pk>/', views.SeriesDeleteView.as_view(), name="ser-del"),
    path('series-edit/<int:pk>/', views.SeriesUpdateView.as_view(), name="ser-ed"),
    path('series_add/', views.SeriesAddView.as_view(), name="ser-add"),
    path('publ_list/', views.Publ_houseList.as_view(), name="pub-li"),
    path('publ/<int:pk>/', views.Publ_houseDetailView.as_view(), name="pub-det"),
    path('publ_delete/<int:pk>/', views.Publ_houseDeleteView.as_view(), name="pub-del"),
    path('publ_add/', views.Publ_houseAddView.as_view(), name="pub-add"),
    path('publ-edit/<int:pk>/', views.Publ_houseUpdateView.as_view(), name="pub-ed"),
]
