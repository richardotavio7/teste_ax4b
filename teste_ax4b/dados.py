import requests
import json
from posts.models import Postagens, Comentarios, Usuarios

url = 'https://jsonplaceholder.typicode.com'


usuarios = requests.get(f'{url}/users')

posts = requests.get(f'{url}/posts')

comentarios = requests.get(f'{url}/comments')


user = Usuarios()

for usuario in usuarios.json():
    user(id=usuario['id'], name=usuario['name'], email=usuario['email'])


post = Postagens()

for postagem in posts.json():
    post(id=postagem['id'] , user_id=user.objects.get(id=postagem['userId']), title=postagem['title'], body=postagem['body'])


comments = Comentarios()

for comentario in comentarios.json():
    comments(id=comentario['id'], name=comentario['name'], email=comentario['email'], body=comentario['body'], post_id=post.objects.get(id=comentario['postId']))


user.save()
post.save()
comments.save()


