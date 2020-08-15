from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
import json
from app.models import Profile


def index(request):
    # foundProfile = Profile.objects.filter(pk=profile_pk)
    # if len(foundProfile) == 0:
    #     return redirect('mypage')
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
