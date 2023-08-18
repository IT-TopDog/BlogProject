from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=40, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Почта')
    date = models.DateField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self) -> str:
        return f'{self.first_name}'
    
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

class Categoty(models.Model):
    name = models.CharField(max_length=30, verbose_name='Категория')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Article(models.Model):
    heading = models.CharField(max_length=50, verbose_name='Заголовок')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey(Categoty, on_delete=models.CASCADE, verbose_name='Категория')
    content = models.TextField(verbose_name='Содержание')
    publication_date = models.DateField(verbose_name='Дата публикации')

    def __str__(self) -> str:
        return self.heading
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

# Create your models here.
