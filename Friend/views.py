from datetime import datetime
import json

from django.contrib.sessions.models import Session
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from User.models import *
from Body.models import *
from Friend.models import *


# Create your views here.
@csrf_exempt
def invitecode(request):  # 16.獲取控糖團邀請碼(OK)
    if request.method == 'GET':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                userprofile = UserProfile.objects.get(
                    pk=(Session.objects.get(
                        pk=token['Bearer']).get_decoded())['user_id'])
                output = {'status': "0",
                          'invite_code': userprofile.invite_code}
        except:
            output = {'status': "1"}
        return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def lists(request):  # 17.控糖團列表(OK)
    if request.method == 'GET':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                user = Friendsend.objects.values().filter(user_id=(Session.objects.get(
                    pk=token['Bearer']).get_decoded())['user_id'], status=1)
                relation = Friendsend.objects.values().filter(relation_id=(Session.objects.get(
                    pk=token['Bearer']).get_decoded())['user_id'], status=1)
                friends = []
                for i in list(user):
                    userprofile = UserProfile.objects.get(pk=i['relation_id'])
                    friends.append({"id": userprofile.pk,
                                    "name": str(userprofile.name),
                                    "account": str(userprofile.account),
                                    "email": str(userprofile.email),
                                    "phone": str(userprofile.phone),
                                    "fb_id": str(userprofile.fb_id),
                                    "status": str(userprofile.status),
                                    "group": str(userprofile.group),
                                    "birthday": str(userprofile.birthday),
                                    "height": userprofile.height,
                                    "gender": str(userprofile.gender),
                                    "verified": userprofile.verified,
                                    "privacy_policy": userprofile.privacy_policy,
                                    "must_change_password": userprofile.must_change_password,
                                    "badge": (userprofile.badge),
                                    "created_at": datetime.strftime(userprofile.created_at, '%Y-%m-%d %H:%M:%S'),
                                    "updated_at": datetime.strftime(userprofile.updated_at, '%Y-%m-%d %H:%M:%S'),
                                    "relation_type": int(i['type'])})
                for i in list(relation):
                    userprofile = UserProfile.objects.get(pk=i['user_id'])
                    friends.append({"id": userprofile.pk,
                                    "name": str(userprofile.name),
                                    "account": str(userprofile.account),
                                    "email": str(userprofile.email),
                                    "phone": str(userprofile.phone),
                                    "fb_id": str(userprofile.fb_id),
                                    "status": str(userprofile.status),
                                    "group": str(userprofile.group),
                                    "birthday": str(userprofile.birthday),
                                    "height": userprofile.height,
                                    "gender": str(userprofile.gender),
                                    "verified": userprofile.verified,
                                    "privacy_policy": userprofile.privacy_policy,
                                    "must_change_password": userprofile.must_change_password,
                                    "badge": (userprofile.badge),
                                    "created_at": datetime.strftime(userprofile.created_at, '%Y-%m-%d %H:%M:%S'),
                                    "updated_at": datetime.strftime(userprofile.updated_at, '%Y-%m-%d %H:%M:%S'),
                                    "relation_type": int(i['type'])})
                output = {'status': '0',
                          'friends': friends}
        except:
            output = {'status': '1'}
    return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def requests(request):  # 18.獲取控糖團邀請(OK)
    if request.method == 'GET':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                friendsendrequest = Friendsend.objects.values().filter(relation_id=(Session.objects.get(
                    pk=token['Bearer']).get_decoded())['user_id'])
                requests = []
                for i in list(friendsendrequest):
                    read = Friendsend.objects.get(user_id=i['user_id'],
                                                  relation_id=i['relation_id'])
                    if i['status'] == 0:
                        read.read = True
                        read.save()
                        user = UserProfile.objects.get(
                            pk=i['user_id'])
                        requests.append({
                            "id": i['id'],
                            "user_id": i['user_id'],
                            "relation_id": i['relation_id'],
                            "type": i['type'],
                            "status": i['status'],
                            "created_at": datetime.strftime(i['created_at'], '%Y-%m-%d %H:%M:%S'),
                            "updated_at": datetime.strftime(i['updated_at'], '%Y-%m-%d %H:%M:%S'),
                            "user": {
                                "id": user.pk,
                                "name": user.name,
                                "account": user.account,
                                "email": user.email,
                                "phone": user.phone,
                                "fb_id": user.fb_id,
                                "status": user.status,
                                "group": user.group,
                                "birthday": user.birthday,
                                "height": user.height,
                                "gender": user.gender,
                                "verified": user.verified,
                                "privacy_policy": user.privacy_policy,
                                "must_change_password": user.must_change_password,
                                "badge": user.badge,
                                "created_at": datetime.strftime(user.created_at, '%Y-%m-%d %H:%M:%S'),
                                "updated_at": datetime.strftime(user.updated_at, '%Y-%m-%d %H:%M:%S'),
                            }
                        })
            output = {'status': '0',
                      'requests': requests}
        except:
            output = {'status': '1'}
        return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@ csrf_exempt
def friendsend(request):  # 19.送出控糖團邀請(OK)
    if request.method == 'POST':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                data = json.loads(request.body)
                user = UserProfile.objects.get(invite_code=data['invite_code'])
                if int(user.pk) != int((Session.objects.get(
                        pk=token['Bearer']).get_decoded())['user_id']):
                    try:
                        try:
                            check = Friendsend.objects.get(user_id=(Session.objects.get(
                                pk=token['Bearer']).get_decoded())['user_id'], relation_id=user.pk)
                        except:
                            check = Friendsend.objects.get(user_id=user.pk, relation_id=(Session.objects.get(
                                pk=token['Bearer']).get_decoded())['user_id'])
                        if check.status == 1:
                            output = {'status': '2'}
                        else:
                            output = {'status': '1'}
                    except:
                        Friendsend.objects.create(
                            user_id=(Session.objects.get(
                                pk=token['Bearer']).get_decoded())['user_id'],
                            relation_id=user.pk, type=data['type'], status=0)
                        output = {'status': '0'}
                else:
                    output = {'status': '1'}
        except:
            output = {'status': '1'}
    return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@ csrf_exempt
def accept(request, id):  # 20.接受控糖團邀請(OK)
    if request.method == 'GET':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                friend = Friendsend.objects.get(pk=id)
                friend.status = 1
                friend.save()
                output = {'status': '0'}
            else:
                output = {'status': '1'}
        except:
            output = {'status': '1'}
    return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@ csrf_exempt
def refuse(request, id):  # 21.拒絕控糖團邀請(OK)
    if request.method == 'GET':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                friend = Friendsend.objects.get(pk=id)
                friend.status = 2
                friend.save()
                output = {'status': '0'}
            else:
                output = {'status': '1'}
        except:
            output = {'status': '1'}
    return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@ csrf_exempt
def remove(request, id):  # 22.刪除控糖團邀請
    if request.method == 'GET':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                Friendsend.objects.get(relation_id=id).delete()
                output = {'status': '0'}
            else:
                output = {'status': '1'}
        except:
            output = {'status': '1'}
    return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@ csrf_exempt
def results(request):  # 26.控糖團結果(OK)
    if request.method == 'GET':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                friendresults = Friendsend.objects.values().filter(user_id=(Session.objects.get(
                    pk=token['Bearer']).get_decoded())['user_id'])
                results = []
                for i in list(friendresults):
                    read = Friendsend.objects.get(user_id=i['user_id'],
                                                  relation_id=i['relation_id'])
                    if read.read == True:
                        user = UserProfile.objects.get(
                            pk=i['relation_id'])
                        results.append({
                            "id": i['id'],
                            "user_id": int(i['user_id']),
                            "relation_id": int(i['relation_id']),
                            "type": i['type'],
                            "status": i['status'],
                            "read": i['read'],
                            "created_at": datetime.strftime(i['created_at'], '%Y-%m-%d %H:%M:%S'),
                            "updated_at": datetime.strftime(i['updated_at'], '%Y-%m-%d %H:%M:%S'),
                            "relation": {
                                "id": user.pk,
                                "name": str(user.name),
                                "account": str(user.account),
                                "email": str(user.email),
                                "phone": str(user.phone),
                                "fb_id": str(user.fb_id),
                                "status": str(user.status),
                                "group": str(user.group),
                                "birthday": str(user.birthday),
                                "height": user.height,
                                "gender": str(user.gender),
                                "unread_records": "[0,0,0]",
                                "verified": user.verified,
                                "privacy_policy": user.privacy_policy,
                                "must_change_password": user.must_change_password,
                                "badge": int(user.badge),
                                "created_at": datetime.strftime(user.created_at, '%Y-%m-%d %H:%M:%S'),
                                "updated_at": datetime.strftime(user.updated_at, '%Y-%m-%d %H:%M:%S'),
                            }
                        })
                        read.read = False
                        read.save()
                output = {'status': '0',
                          'results': results}
        except:
            output = {'status': '1'}
    return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@ csrf_exempt
def removefriend(request):  # 37.刪除好友(OK)
    if request.method == 'DELETE':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                data = json.loads(request.body)
                try:
                    Friendsend.objects.get(user_id=(Session.objects.get(
                        pk=token['Bearer']).get_decoded())['user_id'], relation_id=data["ids[]"]).delete()
                except:
                    Friendsend.objects.get(user_id=data["ids[]"], relation_id=(Session.objects.get(
                        pk=token['Bearer']).get_decoded())['user_id']).delete()

                output = {"status": "0"}
        except:
            output = {"status": "1"}
    return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})
