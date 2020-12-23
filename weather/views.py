from django.shortcuts import render

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=3ea47570c01b0b477c56df2727ef37f7'
    city = 'Las Vegas'
    
    return render(request, 'weather/index.html')