from django.shortcuts import render
#from django.http import H
# ttpResponse
# Create your views here.
from .models import Room

#  rooms=[
#     {'id':1,'name':'Lets learn Python'},
#      {'id':2,'name':'Lets learn .net'},
#     {'id':3,'name':'Design with me'},
# ]



def home(request):
    # return HttpResponse('Home page')
    #return render(request,'home.html',{'rooms':rooms})
    rooms=Room.objects.all()
    context={'rooms':rooms}
    return render(request,'base/home.html',context)
def room(request,pk):
    room=Room.objects.get(id=pk)
    # for i in rooms:
    #     if i['id'] ==int(pk):
    #         room=i
    context={'room':room}
    #retur n HttpResponse('Room')
    return render(request,'base/room.html',context)


def createRoom(request):
    context={}
    return render(request,'base/room_form.html',context)