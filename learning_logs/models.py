from django.db import models

# Create your models here. (Cria os modelos/tabelas do banco de dados) O próprio Django executa os comandos SQL

class Topic(models.Model): # Irá virar uma tabela no banco de dados
  """Um assunto sobre o qual o usuário esta aprendendo"""
  text =  models.CharField(max_length=200) # Cada atributo adcionado será um campo da tabela do banco
  date_added = models.DateTimeField(auto_now_add=True) # Adiciona automaticamente data e hora atual


  def __str__(self):
    """Devolve uma representação em string do modelo no painel administrativo do Django"""
    return self.text
  