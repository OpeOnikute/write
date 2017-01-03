from django.conf.urls import url
from . import views

app_name = 'post'
urlpatterns = [
	url(r'^$', views.about, name='about'),
	url(r'^post/index/', views.index, name='index'),
	url(r'^category/', views.category, name='category'),
	url(r'^convert/', views.convert, name='convert'),
	url(r'^result/', views.result, name='result'),
	url(r'^not_found/', views.convert, name='error'),
	]