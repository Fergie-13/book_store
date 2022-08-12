from django.shortcuts import render, HttpResponse
from random import randint
# Create your views here.

NAMES = ('Ivanov', 'Petrov', 'Sidorov')
def rosters_view(request):
    name = NAMES[randint(0, 2)]
    print(request.user)
    return HttpResponse(f"<h1>Hello { name }!</h1>") 