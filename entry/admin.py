from django.contrib import admin
from .models import Entry


def make_allowed(modeladmin, request, queryset):
    queryset.update(allowed=True)
make_allowed.short_description = "Mark selected entries as allowed"

def make_qualified(modeladmin, request, queryset):
    queryset.update(status='qualified')
make_qualified.short_description = "Mark selected entries as qualified"

def make_disqualified(modeladmin, request, queryset):
    queryset.update(status='disqualified')
make_disqualified.short_description = "Mark selected entries as disqualified"

def make_winner(modeladmin, request, queryset):
    queryset.update(status='winner')
make_winner.short_description = "Mark selected entries as winner"

class EntryAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','status','allowed']
    actions = [make_allowed,make_qualified,make_disqualified,make_winner]

admin.site.register(Entry, EntryAdmin)


# Register your models here.
