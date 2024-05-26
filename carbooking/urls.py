from django.urls import path
from . import views
from .views import initiate_payment


urlpatterns = [
    path("",views.Home,name="home"),
    path("detail/<str:pk>/",views.Detail,name="detail"),
    path("login/",views.Login,name="login"),
    path("register/",views.register,name="register"),
    path("logout/",views.Logout,name="logout"),
    path("hire/",views.Hire,name="hire"),
    path('initiate-payment/', initiate_payment, name='initiate_payment'),
]
