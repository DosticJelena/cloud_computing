from django.urls import path

from counter.api.views import counter

app_name = 'counter'

urlpatterns = [
    path('count/', counter, name="counter")
]