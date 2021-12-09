from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField, SlugField
from django.contrib.auth.models import User
from django.urls import reverse

# Post do blog
class Post(models.Model):
    # CharField são strigs com tamanho até 255.
    # O CharField, funciona como se fosse o varchar do sql
    title = models.CharField(max_length=255)
    
    # Exemplo de slug.
    # www.meusite.com/blog/slug=introducao-ao-django
    slug = SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now= True)
    class Meta:
        ordering = ("-created",)
        
    # Ao invés de retornar Post Object padrão, retornará o titulo do post cadastrado.
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})