from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from books.models import Book


class STUser(models.Model):
    """
    Модель пользователя
    """
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)
    name = models.CharField('Имя пользователя',max_length=50)
    user = models.ForeignKey(User)
    phone = models.CharField(max_length=12,
                             validators=[RegexValidator(
                                 regex=r'^\+\d{11}$',
                                 message='Телефон должен быть в формате +79161234567')],
                             verbose_name='Телефон',
                             blank=True)
    bought_books = models.ManyToManyField(Book,verbose_name='Купленные книги', blank=True)
    card_id = models.CharField(max_length=8,
                               verbose_name='id банковской карты',
                               blank=True)

    def got_books(self):
        return ", ".join([str(p) for p in self.bought_books.all()]) #Метод нужен для корректного отображения купленных книг в админке(обход ManyToManyField)


    def __str__(self):
        return self.name