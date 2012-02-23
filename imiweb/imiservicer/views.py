from imistate.models import *
from imistate.forms import *

from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import Context, Template
from django.utils import simplejson
#from django.core.serializers import serialize

from dojoserializer import serialize

data_obj={"first_name":"First Name", "last_name":"Last Name"}

def entitiesForm(request):
    #EntityFormSet = modelformset_factory(Author)
    #if request.method == 'POST':
    #    formset = AuthorFormSet(request.POST, request.FILES)
    #    if formset.is_valid():
    #        formset.save()
    #        # do something.
    #else:
    #    formset = AuthorFormSet()
    #return render_to_response("manage_authors.html", {
    #    "formset": formset,
    #}
    form = EntityForm()
    return render_to_response('forms/testform.html', {'form': form})

def getInfrastructures(request):
    #http://imi.chadrempp.com:8181/imictl/get/entities/
    #data = serializers.serialize("json", Product.objects.all())
    #data = serializers.serialize("json", Entity.objects.all())
    #return HttpResponse(.dumps(response_dict), mimetype='application/javascript')
    #data =  Entity.objects.all()
    #return HttpResponse(simplejson.dumps(data), mimetype='application/javascript')
    
    #if request.is_ajax():
    if True:
        #Set the result to serialized JSON data.
        
        #result = serialize("json", Infrastructure.objects.all())
        result = serialize(Infrastructure.objects.all())
    else:
        raise Http404
    
    return HttpResponse(result)

def getEntities(request):
    #http://imi.chadrempp.com:8181/imictl/get/entities/
    #data = serializers.serialize("json", Product.objects.all())
    #data = serializers.serialize("json", Entity.objects.all())
    #return HttpResponse(.dumps(response_dict), mimetype='application/javascript')
    #data =  Entity.objects.all()
    #return HttpResponse(simplejson.dumps(data), mimetype='application/javascript')
    
    #if request.is_ajax():
    if True:
        #Set the result to serialized JSON data.
        #result = serialize("json", data_obj)
        result = serialize("json", Entity.objects.all())
    else:
        raise Http404
    
    return HttpResponse(result)

def getProducts(request):
    #if request.is_ajax():
    if True:
        #Set the result to serialized JSON data.
        #result = serialize("json", data_obj)
        result = serialize("json", Product.objects.all())
    else:
        raise Http404
    
    return HttpResponse(result)

def setEntity(request):
    pass

def ajax_example(request):
    if not request.POST:
        return render_to_response('weblog/ajax_example.html', {})
    xhr = request.GET.has_key('xhr')
    response_dict = {}
    name = request.POST.get('name', False)
    total = request.POST.get('total', False)
    response_dict.update({'name': name, 'total': total})
    if total:
        try:
            total = int(total)
        except:
            total = False
    if name and total and int(total) == 10:
        response_dict.update({'success': True})
    else:
        response_dict.update({'errors': {}})
        if not name:
            response_dict['errors'].update({'name': 'This field is required'})
        if not total and total is not False:
            response_dict['errors'].update({'total': 'This field is required'})
        elif int(total) != 10:
            response_dict['errors'].update({'total': 'Incorrect total'})
    if xhr:
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
    return render_to_response('weblog/ajax_example.html', response_dict)