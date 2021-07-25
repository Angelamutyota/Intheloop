from django import urls
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('register/', views.registerPage, name= 'register'),
    path('login/', views.loginPage, name= 'loginpage'),
    path('logout/',views.logoutpage,name='logout'),

    path('',views.index, name = 'index'),
    path('newhood/', views.create_hood, name='newhood'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)