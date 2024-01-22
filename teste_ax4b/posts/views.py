from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Postagens, Comentarios


def index(request):
    post_list = Postagens.objects.order_by('id')
    context = {
        'post_list': post_list,
    }
    return render(request, 'index.html', context)

def postagem(request, post_id):
    post = Postagens.objects.get(id=post_id)
    comment_list = Comentarios.objects.filter(post_id=post_id)
    context = {
        'post': post,
        'comment_list': comment_list,
    }
    return render(request, 'post.html', context)




# Create your views here.
