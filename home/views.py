from django.http import HttpResponse
from django.shortcuts import render

import content
from content.models import Content, Category
from home.models import Settings


# Create your views here.
def index(request):
    setting = Settings.objects.get(pk=2)
    sliderdata= Content.objects.all()[:3]
    category = Category.objects.all();
    dayblogs= Content.objects.all()[:3]
    context={'setting':Settings, 'page':'home','sliderdata':sliderdata, 'category':category}
    return render(request, 'index.html', context)


def hakkimizda(request):
    setting = Settings.objects.get(pk=2)
    context={'setting':Settings}
    return render(request,'hakkimizda.html',context)


def iletisim(request):
    setting = Settings.objects.get(pk=2)
    context={'setting':Settings}
    return render(request,'iletisim.html',context)
def category_blogs(request,id,slug):
    category = Category.objects.filter(pk=id)
    content = Content.objects.filter(category_id=id)
    context = {'content' : content,'category' : category}
    return render(request,'category_blogs.html',context)