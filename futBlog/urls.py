
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from accounts.views import register
#from frontend.views import index
urlpatterns = [
    ##tinymce urls
    path('tinymce/', include('tinymce.urls')),
    
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('admin/', admin.site.urls),
    #path('', index),
    path('', include('pdf.urls')),
    ### quizes urls
    path('quiz/', include('quizes.urls', namespace='quiz')),

    
]
