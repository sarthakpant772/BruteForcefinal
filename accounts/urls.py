
from django.urls import path,include
from . import views



urlpatterns = [
    path('donator',views.donator,name="donator"),
    path('register',views.register,name="register"),
    path('info',views.info,name="info"),
    # path('home_page', views.home_page,name="home_page"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('payment',views.payment,name="payment"),
    path('payment2',views.payment2,name="payment2"),
    # path('login',views.login,name="login"),
    path('dashb',views.dashb,name="dashb")


]