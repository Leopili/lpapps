from django.contrib import admin
from django.urls import path
from core import views as core_views
from portfolio import views as portfolio_views
from django.conf import settings


urlpatterns = [
    path('',core_views.home, name='home'),
    path('nosotros/',core_views.about,name='about'),
    path('apps/',portfolio_views.portfolio,name='portfolio'),
    path('apps/turnos',portfolio_views.turnos,name='turnos'),
    path('contacto/',core_views.contact,name='contact'),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    from django.conf.urls.static import static 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
