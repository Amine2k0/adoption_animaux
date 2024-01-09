from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('template/index.html',views.index,name='index'),
    path('template/contact.html',views.contact,name='contact'),
    path('template/cat.html',views.cat,name='cat'),
    path('template/dog.html',views.dog,name='dog'),
    path('template/ois.html',views.ois,name='ois'),
    path('template/adoption_form.html',views.adoption_form,name='adoption_form'),
    
]
