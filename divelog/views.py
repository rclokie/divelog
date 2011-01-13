from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from divelog.models import Dive

def index(request):
    latest_dive_list = Dive.objects.all().order_by('-date', '-id')
    return render_to_response('divelog/index.html',
    {
        'latest_dive_list': latest_dive_list,
    })

def detail(request, dive_id):
    dive = get_object_or_404(Dive, pk=dive_id);
    return render_to_response('divelog/detail.html',
                              {'dive': dive},
                              context_instance=RequestContext(request))



