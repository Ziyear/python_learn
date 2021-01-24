from django.contrib import admin
from .models import *

@admin.register(BookInfo)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']
    pass


# admin.site.register(HeroInfo)

@admin.register(HeroInfo)
class HeroAdmin(admin.ModelAdmin):
    list_display = ['id','hname','book']
    pass