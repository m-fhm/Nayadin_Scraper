from django.contrib import admin
from main.models import Quote,Events

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', )

# Register your models here.
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Events)