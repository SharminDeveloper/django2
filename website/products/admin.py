from django.contrib import admin
from .models import Product,Comment,Rate
# Register your models here.
class CommentInlines(admin.StackedInline):
    model = Comment
    extra = 0
class RateInlines(admin.StackedInline):
    model = Rate
    extra = 0
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [CommentInlines,RateInlines]
    list_display = ['name','price','rate','provider','status','number_of_comments','date','slug']
    search_fields = ['name','price','provider','status','description','rate']