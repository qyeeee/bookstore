from rest_framework import serializers

from books.serializers import BookSerializer
from store_users.models import STUser, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')



class STUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    bought_books = BookSerializer(many=True)
    class Meta:
        model = STUser
        fields = ('id', 'name', 'user', 'phone', 'bought_books')

