"""hotels_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from guest import views as guest_view
from hotel_server import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.LoginView.as_view(), name="login"),
    path('logout', views.LogoutView.as_view(), name="logout"),
    path("api/rooms/", include("room.urls"), name="room"),
    path("api/guests/", include("guest.urls"), name="guest"),
    path("new-guest/", guest_view.new_guest, name="new guest")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
