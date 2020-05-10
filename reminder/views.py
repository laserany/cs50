from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from reminder.forms import RegisterForm
from reminder.models import CustomUser, Record, Group, GroupMember
import os
from twilio.rest import Client
# Create your views here.

@login_required
def index(request):
    if request.method == 'POST':
        if 'group_name' in request.POST:
            group_name = request.POST['group_name']
            group = Group(name=group_name, user=request.user)
            group.save()
            return redirect('index')
        elif 'member_name' in request.POST:
            member_name = request.POST['member_name']
            member_phone = request.POST['member_phone']
            member_email = request.POST['member_email']
            member_group = Group.objects.filter(name=request.POST['member_group'])[0]
            group_member = GroupMember(name=member_name, phone=member_phone, email=member_email, group=member_group)
            group_member.save()
            return redirect('index')
        else:
            description = request.POST['description']
            method = request.POST['method']
            account_sid = os.getenv('ACC_SID')
            auth_token = os.getenv('AUTH_TOKEN')
            client = Client(account_sid, auth_token)
            if request.POST['people'] == 'yourself':
                record = Record(description=description, method=method, user=request.user)
                record.save()
                if method == 'call':
                    client.calls.create(
                        twiml= '<Response><Say>' + description + '</Say></Response>',
                        to= '+1' + str(request.user.phone)[1:4] + str(request.user.phone)[6:9] + str(request.user.phone)[10:14],
                        from_= os.getenv('TWIL_PHONE')
                    )
                elif method == 'text':
                    client.messages.create(
                        body=description,
                        from_= os.getenv('TWIL_PHONE'),
                        to= '+1' + str(request.user.phone)[1:4] + str(request.user.phone)[6:9] + str(request.user.phone)[10:14]
                    )
                elif method == 'email':
                    send_mail(
                        'Reminder',
                        description,
                        'dotachessfan@gmail.com',
                        [request.user.email],
                        fail_silently=False,
                    )
            else:
                group = Group.objects.filter(name=request.POST['group_list'])[0]
                group_members = GroupMember.objects.filter(group = group)
                for member in group_members:
                    record = Record(description=description, method=method, user=request.user, group=group)
                    record.save()
                    if method == 'call':
                        client.calls.create(
                            twiml= '<Response><Say>' + description + '</Say></Response>',
                            to= '+1' + str(member.phone)[1:4] + str(member.phone)[6:9] + str(member.phone)[10:14],
                            from_= os.getenv('TWIL_PHONE')
                        )
                    elif method == 'text':
                        client.messages.create(
                            body=description,
                            from_= os.getenv('TWIL_PHONE'),
                            to= '+1' + str(member.phone)[1:4] + str(member.phone)[6:9] + str(member.phone)[10:14]
                        )
                    elif method == 'email':
                        send_mail(
                            'Reminder',
                            description,
                            'dotachessfan@gmail.com',
                            [member.email],
                            fail_silently=False,
                        )
            return HttpResponse("Your reminder has been sent!")
    else:
        group_list = request.user.group_set.all()
        return render(request, 'index.html', {'group_list': group_list})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        form.save()
        return redirect('index')
    else:
        return render(request, 'registration/register.html', {'form': RegisterForm()})


