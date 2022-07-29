from django.contrib import admin

# Register your models here.
from django.conf import settings
from django.contrib import admin


# @admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude',)
    search_fields = ('name',)

    fieldsets = (
        (None, {
            'fields': ( 'name', 'latitude', 'longitude',)
        }),
    )

    # class Media:
        # if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            # css = {
                # 'all': ('angular-restaurantsUI/src/app/app.component.css',),
            # }
            # js = (
                # 'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                # 'angular-restaurantsUI/src/app/app.component.spec.ts',
            # )