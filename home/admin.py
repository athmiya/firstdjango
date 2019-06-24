from django.contrib import admin
from home.models import Book,Author,Genre
# Register your models here.
#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(Genre)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
     search_fields = ('id','name')
     fields=[('id','name'),('genre','author')]
     # note: RelatedOnlyFieldListFilter => applicable when some fields are related to other tables
     list_filter = ('name','purchase_date',('author',admin.RelatedOnlyFieldListFilter))
     list_filter = ('name','purchase_date','author')
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
     list_filter = ('date_of_birth','date_of_death')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
     pass
#@admin.register(member)
#class memberAdmin(admin.ModelAdmin):
 #    search_fields = ('date_of_purchase','member_name')   
