from django.contrib import admin
from .models import Team, About, Portfolio, ContactMessage, Clients, Service, Footer

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'id')
    search_fields = ('name', 'post')


@admin.action(description='Обработано')
def make_processed(modeladmin, request, queryset):
    queryset.update(is_processed=True)

@admin.action(description='Не обработано')
def not_processed(modelamin, request, queryset):
    queryset.update(is_processed=False)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'date', 'is_processed')
    search_fields = ('name', 'phone', 'is_processed')
    ordering = ('-date',)
    actions = [make_processed, not_processed]


admin.site.register(Team, TeamAdmin)
admin.site.register(About)
admin.site.register(Portfolio)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Clients)
admin.site.register(Service)
admin.site.register(Footer)

