from django.contrib import admin

from checklist.models import ListTemplate, ListItemTemplate


class ItemListTemplateInline(admin.StackedInline):
    model = ListItemTemplate


class ListTemplateAdmin(admin.ModelAdmin):
    inlines = [ItemListTemplateInline, ]


admin.site.register(ListTemplate, ListTemplateAdmin)
admin.site.register(ListItemTemplate)
