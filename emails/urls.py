from django.conf.urls import url
from . import views

app_name = 'emails'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^category/', views.select_category, name='select_category'),
	url(r'^result/', views.result, name='result'),
	# url(r'^convert/', views.convert, name='convert'),
	# url(r'^result/', views.result, name='result'),
	]