from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .api import Message

def simulator(request):
    if request.method == 'GET':
        return render(request, "wechat_message/simulator.html")
    elif request.method == 'POST':
        url = request.POST['url']
        xml = request.POST['xml']
        api = Message()
        result = api.get_data(url, xml, 'string')
        return HttpResponse(result, content_type='text/xml')

@csrf_exempt
def index(request):
    wx = Message()
    try:
        """ First bind """
        echostr = request.GET['echostr']
        """
        result = wx.check_sign(request.GET)
        if result:
            return HttpResponse(echostr)
        else:
            return HttpResponse('error')
        """
        return HttpResponse(echostr)
    except KeyError:
        """ Normal message """
        data = wx.receive(request.body)
        keyword = wx.get_keyword(data)
        result = wx.response(keyword, data)
        return HttpResponse(result)
