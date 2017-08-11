from rest_framework.decorators import api_view
from rest_framework.response import Response


from store_users.serializers import STUser, STUserSerializer


@api_view(['GET'])
def get_user(request, **kwargs):#Метод, возвращающий информацию о пользователе по id
    id = request.data['id']
    user = STUser.objects.get(id=id)
    serializer = STUserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
def get_bought_books(request, **kwargs):#Метод, возвращающий информацию о купленных книгах пользователя
    id = request.data['id']
    bought_books = STUser.objects.get(id=id)
    serializer = STUserSerializer(bought_books)
    return Response(serializer.data)



