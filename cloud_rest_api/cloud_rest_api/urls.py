from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rest API
    path('api/', include('counter.api.urls'))
]
