"""second URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import myapp.views
import sm_practice_app.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("myapp/", myapp.views.main, name="main"),
    path("myapp/google_move/", myapp.views.google_move, name="google_move"),
    path("myapp/detail/<int:blog_id>", myapp.views.detail, name="detail"),
    path("myapp/new/", myapp.views.new, name="new"),
    path("myapp/renew/<int:blog_id>", myapp.views.renew, name="renew"),
    path("myapp/remove/<int:blog_id>", myapp.views.remove, name="remove"),
    path("", sm_practice_app.views.index, name="index"),
    path("upload/", sm_practice_app.views.upload, name="upload"),
    path("upload_result/", sm_practice_app.views.upload_result, name="upload_result"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
