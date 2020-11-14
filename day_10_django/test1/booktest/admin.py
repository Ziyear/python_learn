from django.contrib import admin

# Register your models here.
from .models import *


# class HeroInfoInline(admin.StackedInline):
class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 3


class BookInfoAdmin(admin.ModelAdmin):
    # 列表展示字段
    list_display = ['id', 'btitle', 'bpub_date']

    # 过滤字段
    list_filter = ['btitle']

    # 搜索字段
    search_fields = ['btitle']

    # 分页
    list_per_page = 2

    # 修改页面先后顺序
    # fields = ['bpub_date','btitle']

    # 属性分组
    fieldsets = [
        ('basic', {'fields': ['btitle']}),
        ('more', {'fields': ['bpub_date']}),
    ]

    # 嵌入关联对象
    inlines = [HeroInfoInline]


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo)
