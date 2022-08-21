from multiprocessing import context
from tkinter.messagebox import QUESTION
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views import generic
from . import models
from . import forms
from datetime import datetime
from django.urls import reverse_lazy


# Create your views here.

       

class GenreList(generic.ListView):
    template_name = 'rosters/genre_list.html'
    model=models.Genre
    # context-> object_list + modelname

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['today'] = datetime.now().date
        return context

    def get_queryset(self):
        qs = self.model.objects.all()
        return qs



class GenreDetailView(generic.DetailView):
    template_name = 'rosters/genre_view.html'
    model=models.Genre
    # context-> object + modelname


class GenreAddView(generic.CreateView):
    template_name = 'rosters/genre_add.html'
    model=models.Genre   
    fields = ['name', 'description']   # context-> form
    
    def get_success_url(self):
        return reverse_lazy("gen-det", kwargs={'pk' : self.object.pk})
        #return f"/genre/{self.object.pk}/"


class GenreDeleteView(generic.DeleteView):
    template_name = 'rosters/genre_delete.html'
    model=models.Genre  
    success_url = '/genre_list/'

def city_delete_view(request, pk):
    models.Genre.objects.get(pk=pk).delete()
    return HttpResponse("Object was deleted!")


class GenreUpdateView(generic.UpdateView):
    template_name = 'rosters/genre_add.html'
    model=models.Genre  
    fields = ['name', 'description'] 
    success_url = '/genre_list/'






class AuthorList(generic.ListView):
    template_name = 'rosters/author_list.html'
    model=models.Author
    # context-> object_list + modelname
    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['today'] = datetime.now().date
        return context


class AuthorDetailView(generic.DetailView):
    template_name = 'rosters/author_view.html'
    model=models.Author
    # context-> object + modelname


class AuthorAddView(generic.CreateView):
    template_name = 'rosters/author_add.html'
    model=models.Author   
    fields = ['name', 'description']   # context-> form
    
    def get_success_url(self):
        return reverse_lazy("aut-det", kwargs={'pk' : self.object.pk})


class AuthorDeleteView(generic.DeleteView):
    template_name = 'rosters/author_delete.html'
    model=models.Author  
    success_url = '/author_list/'

def city_delete_view(request, pk):
    models.Author.objects.get(pk=pk).delete()
    return HttpResponse("Object was deleted!")


class AuthorUpdateView(generic.UpdateView):
    template_name = 'rosters/author_add.html'
    model=models.Author  
    fields = ['name', 'description'] 
    success_url = '/author_list/'




class SeriesList(generic.ListView):
    template_name = 'rosters/series_list.html'
    model=models.Series
    # context-> object_list + modelname
    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['today'] = datetime.now().date
        return context



class SeriesDetailView(generic.DetailView):
    template_name = 'rosters/series_view.html'
    model=models.Series
    # context-> object + modelname


class SeriesAddView(generic.CreateView):
    template_name = 'rosters/series_add.html'
    model=models.Series   
    fields = ['name', 'description']   # context-> form
    
    def get_success_url(self):
        return reverse_lazy("ser-det", kwargs={'pk' : self.object.pk})


class SeriesDeleteView(generic.DeleteView):
    template_name = 'rosters/series_delete.html'
    model=models.Series  
    success_url = '/series_list/'

def city_delete_view(request, pk):
    models.Series.objects.get(pk=pk).delete()
    return HttpResponse("Object was deleted!")


class SeriesUpdateView(generic.UpdateView):
    template_name = 'rosters/series_add.html'
    model=models.Series  
    fields = ['name', 'description'] 
    success_url = '/series_list/'




class Publ_houseList(generic.ListView):
    template_name = 'rosters/publ_list.html'
    model=models.Publ_house
    # context-> object_list + modelname
    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['today'] = datetime.now().date
        return context


class Publ_houseDetailView(generic.DetailView):
    template_name = 'rosters/publ_view.html'
    model=models.Publ_house
    # context-> object + modelname


class Publ_houseAddView(generic.CreateView):
    template_name = 'rosters/publ_add.html'
    model=models.Publ_house   
    fields = ['name']   # context-> form
    
    def get_success_url(self):
        return reverse_lazy("pub-det", kwargs={'pk' : self.object.pk})


class Publ_houseDeleteView(generic.DeleteView):
    template_name = 'rosters/publ_delete.html'
    model=models.Publ_house  
    success_url = '/publ_list/'

def city_delete_view(request, pk):
    models.Publ_house.objects.get(pk=pk).delete()
    return HttpResponse("Object was deleted!")


class Publ_houseUpdateView(generic.UpdateView):
    template_name = 'rosters/publ_add.html'
    model=models.Publ_house  
    fields = ['name'] 
    success_url = '/publ_list/'