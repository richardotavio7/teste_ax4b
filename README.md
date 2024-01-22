# INSTRUÇÕES DE INSTALAÇÃO

Certifique-se de ter o Python 3 instalado.
Inicie um ambiente virtual do Python

``` 
python -m venv venv
```

Entre no ambiente virtual
Para Windows:

``` 
.\venv\Scripts\Activate.ps1
```

Para Linux:

```
source ./venv/bin/activate
```

Instale as bibliotecas necessarias:

```
pip install -r requirements.txt
```

Acesse a pasta do Projeto: 

```
cd teste_ax4b
```

Faça a criação do Banco de Dados:

```
python manage.py migrate
```

Importe os arquivos via API:

```
python manage.py shell --command="exec(open('dados.py').read())"
```

Execute o Servidor:

```
python manage.py runserver 
```

O servidor estará disponivel no endereço:

http://localhost:8000/posts