import os

from django.db import models


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Author(models.Model):
    """
    Модель автора
    """
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ('id',)
    first_name = models.CharField('Имя автора',max_length=50)
    last_name = models.CharField('Фамилия автора',max_length=50)
    photo = models.ImageField(verbose_name='Фотография',upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return u'{l} {f}'.format(l=self.last_name, f=self.first_name)

class Book(models.Model):
    """
    Модель книги
    """
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ('id',)
    authors = models.ManyToManyField(Author,blank=True)
    title = models.CharField('Название книги',max_length=100)
    desc = models.TextField('Описание',max_length=2500,blank=True)
    photo = models.ImageField(verbose_name='Фотография',upload_to=get_image_path, blank=True, null=True)
    cost = models.DecimalField(verbose_name='Стоимость',decimal_places=2, max_digits=5)
    download = models.CharField('Ссылка на скачивание книги',max_length=100, blank=True, null=True )



    def got_authors(self):
        return ", ".join([str(p) for p in self.authors.all()])

    def __str__(self):
        return self.title





