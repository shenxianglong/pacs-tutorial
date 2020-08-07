from django.shortcuts import render
from django.http import FileResponse
from server import models
import json
import uuid
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.
def read0(request):
    file = open('./testdcm/ImageFileName0080.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="0.dcm"'
    # response["Access-Control-Allow-Headers"] = "Access-Control-Allow-Origin"
    return response

def read1(request):
    file = open('./testdcm/ImageFileName0081.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="1.dcm"'
    return response
def read2(request):
    file = open('./testdcm/ImageFileName0082.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="2.dcm"'
    return response
def read3(request):
    file = open('./testdcm/ImageFileName0083.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="3.dcm"'
    return response
def read4(request):
    file = open('./testdcm/ImageFileName0084.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="4.dcm"'
    return response
def read5(request):
    file = open('./testdcm/ImageFileName0085.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="5.dcm"'
    return response
def read6(request):
    file = open('./testdcm/ImageFileName0086.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="6.dcm"'
    return response
def read7(request):
    file = open('./testdcm/ImageFileName0087.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="7.dcm"'
    return response
def read8(request):
    file = open('./testdcm/ImageFileName0088.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="8.dcm"'
    return response
def read9(request):
    file = open('./testdcm/ImageFileName0089.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="9.dcm"'
    return response
