from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('blog/',views.blog,name='blog'),
    path('training/',views.training,name='training'),
    path('feature/',views.feature,name='feature'),
    path('gallery/',views.gallery,name='gallery'),
    path('new/',views.new,name='new'),
    path('footer/',views.footer,name='footer'),
]
