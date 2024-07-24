from django.contrib import admin

from dogs_api.models import Dog, Breed

admin.site.register(Dog)
admin.site.register(Breed)

