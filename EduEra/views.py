from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from datetime import datetime
from EduEra.models import teacherForm,studentForm
from django.contrib.auth.models import User
from django.http import JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder
from .models import RoomMember
import json
from django.views.decorators.csrf import csrf_exempt

def lobby(request):
    return render(request, 'lobby.html')

def room(request):
    return render(request, 'room.html')


def getToken(request):
    appId = "9f2f51b1bb2e4711b31153cb8e626fef"
    appCertificate = "de03ffca3e334aa0862fcdac9e686c1b"
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600 * 24
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

    return JsonResponse({'token': token, 'uid': uid}, safe=False)


@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name':data['name']}, safe=False)


def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name}, safe=False)

@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    member = RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    member.delete()
    return JsonResponse('Member deleted', safe=False)


# Create your views here.

def studentform(request):
    
    if (request.method=="POST"):
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        phoneNo = request.POST.get("phoneNo")
        email = request.POST.get("email")
        password = request.POST.get("password")
        SForm = studentForm(firstName=firstName,lastName=lastName,phoneNo=phoneNo,email=email,password=password)
        SForm.save()
        messages.success(request, 'Your Message Has been sent!')
        if request.method == "POST":
            firstName =request.POST['firstName']
            lastName =request.POST['lastName']
            email =request.POST['email']
            password =request.POST['password']
            username= firstName+lastName
            myuser = User.objects.create_user(username,email,password)
            myuser.first_name = firstName
            myuser.last_name = lastName

            myuser.save()
            return redirect('studentform')

        return render (request,"news/signup.html")
        def __str__(self):
            return self.firstName
        
    else:
        return render(request,'studentform.html')
        

def teacherform(request):
    if request.method=="POST":
        firstName = request.POST.get("firstName")
        secondName = request.POST.get("secondName")
        phoneNo = request.POST.get("phoneNo")
        subject = request.POST.get("subject")
        email = request.POST.get("email")
        password = request.POST.get("password")
        tf = teacherForm(firstName=firstName,secondName=secondName,phoneNo=phoneNo,subject=subject,email=email,password=password)
        tf.save()
        print(firstName)
    return render(request,'teacherform.html')


def signinuser(request):
    if request.method=='POST':
        firstName=request.POST['firstName']
        password=request.POST['password']
        username=firstName
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            firstName=user.first_name
            return render (request,"indexin.html", {'firstName':firstName})

        else:
            messages.error(request,"Bad Credentials") 
            return redirect('home')   


    return render(request,'signinuser.html')


def signout(request):
    logout(request) 
    messages.success(request,"Logged Out Successfully")
    return redirect('home')


def index(request):
    return render(request,'index.html')



