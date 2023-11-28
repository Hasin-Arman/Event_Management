from django.contrib import admin
from .models import event,event_registration

class EventAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if event.objects.all().count() == 0:
            obj.registered_user=0
            obj.save()
        super().save_model(request, obj, form, change)
    
admin.site.register(event,EventAdmin)
admin.site.register(event_registration)
