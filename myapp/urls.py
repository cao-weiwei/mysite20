from django.urls import path
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'about/', views.about, name='about'),
    path(r'courses/', views.courses, name='courses'),
    path(r'place_order/', views.place_order, name='place_order'),
    path(r'order_response/', views.place_order, name='order_response'),
    path(r'<top_no>/', views.detail, name='detail'),
]
