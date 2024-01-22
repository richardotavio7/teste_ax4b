from django.shortcuts import render
from django.http import HttpResponse
from .models import Postagens, Comentarios

def index(request):
    post_list = Postagens.objects.order_by('id')
    context = {
        'post_list': post_list,
    }
    return render(request, 'index.html', context)

# Create your views here.
