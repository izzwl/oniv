from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from .forms import AttendanceForm,CongratulationWhisesForm

# Create your views here.


def index(request,undangan,template='ui/base.html'):
    att_form = AttendanceForm(request.POST or None,instance=None,initial={'is_attend':True})
    # crw_form = CongratulationWhisesForm(request.POST or None,instance=None,)
    if att_form.is_valid():
        ins = att_form.save(commit=False)
        ins.event = Event.objects.get(name=undangan)
        try:
            ins.save()
            att_form = AttendanceForm(initial={'is_attend':True})
            messages.add_message(request, messages.INFO, 'thank you %s for submitting attendance form'%ins.name)
        except:
            messages.add_message(request, messages.ERROR, 'Attendance not submited')
    # if crw_form.is_valid():
    #     ins = crw_form.save(commit=False)
    #     ins.event = event
    #     try:
    #         ins.save()
    #         messages.add_message(request, messages.INFO, 'Terimakasih.')
    #     except:
    #         messages.add_message(request, messages.ERROR, 'Whises not submited')                
    event = Event.objects.select_related(
        'bride','groom','venue',
    ).prefetch_related(
        'eventgallery_set','attendance_set',
    ).get(name=undangan)
    return render(request,template,{
        'event':event,'att_form':att_form,
    })
    # return HttpResponse('test')