from django.contrib import admin

from checklist.models import ListTemplate, ListItemTemplate, List, Item


class ItemListTemplateInline(admin.StackedInline):
    model = ListItemTemplate


class ListTemplateAdmin(admin.ModelAdmin):
    inlines = [ItemListTemplateInline, ]


class ItemInline(admin.StackedInline):
    model = Item


class ListAdmin(admin.ModelAdmin):
    inlines = [ItemInline, ]


admin.site.register(ListTemplate, ListTemplateAdmin)
admin.site.register(ListItemTemplate)
admin.site.register(List, ListAdmin)
admin.site.register(Item)
