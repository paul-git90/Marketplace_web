from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, template_name='sweet_market_place14_app/home.html')
