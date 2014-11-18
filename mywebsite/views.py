# -*- coding: utf-8 -*-
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, this is a placeholder site that Mobingi has prepared for you. Please go to the Mocloud Console and upload or specify the location of your application.")
