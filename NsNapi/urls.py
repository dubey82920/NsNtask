from django.urls import path
from . import views
urlpatterns = [
    path("",views.getRoutes,name="routes"),
    path('work/',views.getWorks,name="works"),
    path('work/<str:artist_name>',views.getWork,name="work"),
    path('work/<str:work_type>',views.getWork,name="work"),
    path('register/',views.register,name="register")
]