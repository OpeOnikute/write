from django.contrib import admin

# Register your models here.
from .models import Stories, Email, event, news

# class StoryAdmin(admin.ModelAdmin):
# 	class Meta:
# 		model = Story
class EventAdmin(admin.ModelAdmin):
	class Meta:
		model = event



admin.site.register(Stories)
admin.site.register(event)
admin.site.register(news)
admin.site.register(Email)



