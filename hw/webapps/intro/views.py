from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
import json
from intro.models import *

# The action for the 'intro/hello-world' route.
def home(request):
    # render takes: (1) the request,
    #               (2) the name of the view to generate, and
    #               (3) a dictionary of name-value pairs of data to be
    #                   available to the view template.
    return render(request, 'home.html', {})

def enter_chat(request):
    errors = []
    context = {}
    print request.POST

    if not 'username' in request.POST or not request.POST['username']:
        errors.append('Username required')
        context['errors'] = errors
        return render(request, 'home.html', context)
    else:
        context['username'] = request.POST['username']
    context['errors'] = errors
    messages = Message.objects.all()
    context['messages'] = messages
    return render(request,'chat.html',context)


def post_message(request):
    errors = []
    if not 'message' in request.POST or not request.POST['message']:
        errors.append('No message to post')
    else:
        new_message = Message(text=request.POST['message'],username=request.POST['username'])
        new_message.save()
    messages = Message.objects.all()
    context = {'errors':errors,'messages':messages,'username':request.POST['username']}
    return render(request,'chat.html',context)

def date_handler(obj):
    return obj.isoformat(' ') if hasattr(obj, 'isoformat') else obj

def get_list(request):
    temp_response = serializers.serialize("python", Message.objects.all())
    response_text = json.dumps(temp_response,default=date_handler)
    return HttpResponse(response_text, content_type="application/json")
