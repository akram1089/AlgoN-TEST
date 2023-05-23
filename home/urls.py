
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
urlpatterns = [
    
    path('',views.home , name="home"),
    path('signup', views.signup, name ="signup"),
    path('login', views.loginuser, name ="login"),
    path('logout', views.logoutuser, name ="logout"),
    path('dashboard', views.dashboard, name ="dashboard"),

    path('user_details',views.user_details,name='user_details'),
    path('contact_us',views.contact_us,name='contact_us'),
    path('pricing',views.pricing,name='pricing'),
    path('syntax',views.syntax,name='syntax'),
    path('indicator_store',views.indicator_store,name='indicator_store'),
    path('symbol',views.symbol,name='symbol'),
    path('video',views.video,name='video'),
    path('faq',views.faq,name='faq'),
    path('admin_panel',views.admin_panel,name='admin_panel'),
    path('delete_user/<str:id>',views.delete_user,name='delete_user'),
    path('delete_feedback/<str:id>',views.delete_feedback,name='delete_feedback'),
    path('reset_password/',views.reset_password,name='reset_password'),
    path('change_pass/<token>/',views.change_pass,name='change_pass'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

