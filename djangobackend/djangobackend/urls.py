from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('accounts/', include('accounts.urls')),
    path('', views.homepage, name="homepage")
]

urlpatterns += staticfiles_urlpatterns()