import requests
from posts.models import Postagens, Comentarios, Usuarios


usuarios = requests.get('https://jsonplaceholder.typicode.com/users')


posts = requests.get('https://jsonplaceholder.typicode.com/posts')


comentarios = requests.get('https://jsonplaceholder.typicode.com/comments')


for usuario in usuarios.json():
    user = Usuarios(id=usuario['id'], name=usuario['name'], email=usuario['email'])
    user.save()

for postagem in posts.json():
    post = Postagens(id=postagem['id'] , user_id=Usuarios.objects.get(id=postagem['userId']), title=postagem['title'], body=postagem['body'])
    post.save()

for comentario in comentarios.json():
    comments = Comentarios(id=comentario['id'], name=comentario['name'], email=comentario['email'], body=comentario['body'], post_id=Postagens.objects.get(id=comentario['postId']))
    comments.save()




