from rest_framework.decorators import api_view

from rest_framework.response import Response

from books.models import Book
from books.serializers import BookSerializer



@api_view(['GET']) #Декоратор, разрешающий только метод GET
def all_books(request, **kwargs):#Метод, возвращающий список всех книг
    books = Book.objects.all()
    serializers = BookSerializer(books, many=True)
    return Response(serializers.data)



@api_view(['GET'])
def get_book(request, **kwargs):#Метод, возвращающий информацию об одной книге по id
    id = request.data['id']
    book = Book.objects.get(id=id)
    serializer = BookSerializer(book)
    return Response(serializer.data)




