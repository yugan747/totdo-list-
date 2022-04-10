from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns=[
    path("",views.home,name='home'),
    path('createtodo/',views.createtodo,name="createtodo"),
    path('signup/',views.signup,name="signup"),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('authenticateduser/',views.authenticateduser,name='authenticateduser'),
    path('logoutpage/',views.logoutpage,name="Logout"),
    path('viewtodo/',views.viewtodo,name='viewtodo')
]+static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
