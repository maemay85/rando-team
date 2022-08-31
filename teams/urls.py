from django.urls import path

from . import views

#app_name = 'teams'

urlpatterns = [
    # ex: /polls/
    path('', views.get_name, name='get_name'),
    path('yourname/', views.yourname, name='yourname'),
    path('thanks', views.thanks, name='thanks'),
]
