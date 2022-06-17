from django.contrib import admin
from .models import server, type_of_server,user, application, services,applicaitonshasservices, overall

admin.site.register(server)
admin.site.register(type_of_server)

admin.site.register(user)
admin.site.register(application)

admin.site.register(services)

admin.site.register(applicaitonshasservices)
admin.site.register(overall)

