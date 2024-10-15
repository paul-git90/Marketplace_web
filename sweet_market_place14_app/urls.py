from django.urls import path
from ProiecteDjango.sweet_market_place14.sweet_market_place14_app.views import home_view

app_name = 'sweet_market_place14_app'

urlpatterns = [
    path('', home_view, name='home'),
    
]