from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("嘿，哥们，你现在访问的是投票应用的首页。")
