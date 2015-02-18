from django.shortcuts import render
from datetime import datetime

def home(request):
        return render(request, 'home.html', {'right_now':datetime.utcnow()})
