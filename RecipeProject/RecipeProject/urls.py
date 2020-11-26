from django.contrib import admin
from django.urls import path
from recipeapp import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'recipeapp'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('home', views.home, name = 'home'),
    path('create', views.create, name = 'create'),
    path('<int:id>/delete', views.delete, name = 'delete'),
    path('<int:id>/details', views.details, name = 'details')
]


if settings.DEBUG == True:
    urlpatterns +=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)