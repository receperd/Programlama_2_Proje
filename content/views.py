from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    #text="merhaba dünya"
    #return HttpResponse("ilk django projesi %s." % text)
    text='text metni ';
    context={'text':text}
    return render(request, 'index.html', context)