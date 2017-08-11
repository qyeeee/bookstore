from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from books.views import all_books, get_book
from store_users.views import get_user,get_bought_books

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^books/all/', all_books),
    url(r'^user/', get_user),
    url(r'^book/', get_book),
    url(r'^bought_books/',get_bought_books ),
    url(r'^api-auth/', include('rest_framework.urls',
                                namespace='rest_framework')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)# Необходимо для загрузки фотографий
