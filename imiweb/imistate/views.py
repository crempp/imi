# Create your views here.

from imistate.models import *
from django.http import HttpResponse

    
def home(request):
    l = Product.objects.all()
    output = ', '.join([p.name for p in l])
    return HttpResponse(output)
