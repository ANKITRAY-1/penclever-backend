from django.contrib import admin
from .models import Categories


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',
                    )
# Register your models here.


admin.site.register(Categories, CategoryAdmin)
