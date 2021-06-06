from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from datetime import datetime


@login_required
def index(request):
    current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S (%A)")
    html = "<html><body><h2>Сейчас: %s</h2></body></html>" % current_date
    return HttpResponse(html)
