
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path("",include("homepage.urls"),name='homepage'),
    path('', include('engineering.urls')),
    path('weflow-community',include('webflow.urls'))
]
