from django.shortcuts import HttpResponse,render
from visits.models import PageVisit


def home_page_view(request,*args, **kwargs):
    
    return render(request,"home.html")