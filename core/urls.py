from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('Figuras', Figuras, name="figuras"),
    path('accesorios', accesorios, name="accesorios"),
    path('ropa', ropa, name="ropa"),
    path('login', LoginView.as_view(template_name='core/login.html'), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('carrito', carrito, name="carrito"),
    path('addtocar/<id>', addtocar, name="addtocar"),
    path('dropitem/<id>', dropitem, name="dropitem"),
    path('limpiar', limpiar),
]
