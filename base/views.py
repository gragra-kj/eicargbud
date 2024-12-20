from django.shortcuts import render,redirect
#from django.http import H
# ttpResponse
# Create your views here.
from .models import Room

from .forms import RoomForm,MessageForm

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
    form=RoomForm()
    if request.method=='POST':
        #print(request.POST)
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'base/room_form.html',context)

def updateRoom(request,pk):
    room=Room.objects.get(id=pk)
    form=RoomForm(instance=room)
    if request.method=='POST':
        form=RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'base/room_form.html',context)


def deleteRoom(request,pk):
    room=Room.objects.get(id=pk)
    if request.method=='POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':room})
    
def createMessage(request):
    form=MessageForm()
        