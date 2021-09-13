from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ListUploadFile, search_view
urlpatterns = [
	#path('', views.home, name='home'),
	path('', ListUploadFile.as_view(template_name='pdf/home.html'), name="home" ),
	path('search/', search_view, name='search'),
	path('email-contact/', views.email_contact, name='email_contact'),
    path('email-subscribe/', views.email_subscribe, name='email_subscribe'),

]


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)