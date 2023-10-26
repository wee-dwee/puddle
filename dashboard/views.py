from django.shortcuts import render
from item.models import items
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    it=items.objects.filter(created_by=request.user)
    return render(request,'dashboard/index.html',{
        'items':it
    })