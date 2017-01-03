from django.contrib import admin

from .models import customer_service, client, friends_and_family, job_acceptance, job_interview


admin.site.register(client)
admin.site.register(customer_service)
admin.site.register(friends_and_family)
admin.site.register(job_acceptance)
admin.site.register(job_interview)




