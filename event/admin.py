from django.contrib import admin
from .models import *
# Register your models here.

class EventGalleryInline(admin.TabularInline):
    model = EventGallery

class EventAdmin(admin.ModelAdmin):
    inlines = [EventGalleryInline]

admin.site.register(Host)
admin.site.register(BrideGroom)
admin.site.register(Venue)
admin.site.register(Event,EventAdmin)
admin.site.register(EventGallery)
admin.site.register(Invitation)
admin.site.register(CongratulationWhises)
admin.site.register(Attendance)

