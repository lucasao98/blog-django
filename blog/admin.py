from django.contrib import admin
from .models import Post # Importa o model Post

@admin.register(Post) # Adiciona o Post na interface de admin. Com isso é possível adicionar posts no blog.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "updated")
    prepopulated_fields = {"slug": ("title",)} # Ao inserir o titulo, o slug é automaticamente preenchido, com o mesmo nome do titulo.