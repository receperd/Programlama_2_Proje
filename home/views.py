from django.http import HttpResponse
from django.shortcuts import render

from home.models import Settings


# Create your views here.
def index(request):
    setting = Settings.objects.get(pk=2)
    context={'setting':Settings, 'page':'home'}
    return render(request, 'index.html', context)

#def index(request):
    #    Settings = Settings.object.get(pk=1)
    #   context={'settings':settings, 'page':'home'}
#   return render(request,'index.html',context)
def hakkimizda(request):
    setting = Settings.objects.get(pk=2)
    context={'setting':Settings}
    return render(request,'hakkimizda.html',context)


def iletisim(request):
    setting = Settings.objects.get(pk=2)
    context={'setting':Settings}
    return render(request,'iletisim.html',context)

