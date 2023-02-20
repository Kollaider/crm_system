from django.contrib import admin

from webapp.models import Company, Scope, Office, Profile, Position, Language

admin.site.register(Company)
admin.site.register(Scope)
admin.site.register(Office)
admin.site.register(Profile)
admin.site.register(Position)
admin.site.register(Language)