from django.shortcuts import HttpResponse,render
from visits.models import PageVisit

def visit(request,*args, **kwargs):
    all_visits = PageVisit.objects.all()
    page_visit = PageVisit.objects.filter(path = request.path)
    try:
        percent = (page_visit.count()*100.0) / all_visits.count()
    except:
        percent = 0
    context = {
        "total_visit_count":all_visits.count(),
        "page_visit_count":page_visit.count(),
        "percent":percent
    }
    return context
def home_view(request,*args, **kwargs):
    context = visit(request,*args, **kwargs)
    PageVisit.objects.create(path=request.path)
    return render(request,"home.html",context=context)



def about_view(request,*args, **kwargs):
    context = visit(request,*args, **kwargs)
    PageVisit.objects.create(path=request.path)
    return render(request,"about.html",context=context)