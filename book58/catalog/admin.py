from django.contrib import admin
from .models import Author, Book, Genre, Language, Status, BookInstance, Point

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
admin.site.register(BookInstance)
admin.site.register(Point)