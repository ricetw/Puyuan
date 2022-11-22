import json
import random
import string
import urllib.parse
from django.conf import settings
from django.contrib import auth
from django.contrib.sessions.models import Session
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Puyuan import settings
from User.models import *
from Body.models import *
from Friend.models import *
# Create your views here.


@csrf_exempt
def register(request):  # 1.註冊(OK)
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            user = UserProfile.objects.create(
                username=data["account"], account=data["account"], phone=data[
                    "account"], email=data["email"], password=data["password"], invite_code=''.join(random.sample(
                        string.digits, 6))
            )
            user.set_password(data["password"])
            user.save()
            Medical.objects.create(user_id=user.pk)
            UserDefault.objects.create(user_id=user.pk)
            UserSetting.objects.create(user_id=user.pk)
            output = {"status": "0"}
        except:
            output = {"status": "1"}
        return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def login(request):  # 2.登入(OK)
    if request.method == 'POST':
        data = json.loads(request.body)
        request.session.flush()
        try:
            accountlogin = UserProfile.objects.get(account=data['account'])
            if accountlogin.verified == False:
                output = {'status': "2"}
            else:
                user = auth.authenticate(request,
                                         username=data['account'], password=data['password'])
                if user is not None and user.is_active:
                    auth.login(request, user)
                    request.session['user_id'] = accountlogin.pk
                    request.session.save()
                    if accountlogin.login_times == None:
                        accountlogin.login_times = 1
                    else:
                        accountlogin.login_times += 1
                    accountlogin.save()
                    output = {'status': "0",
                              "token": request.session.session_key}
                else:
                    output = {'status': "1"}
        except:
            output = {'status': "1"}
        return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def send(request):  # 3.發送驗證碼(OK)
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            if list(VerificationCode.objects.filter(email=data["email"])) == []:
                code = VerificationCode.objects.create(
                    email=data["email"], VerificationCode=''.join(random.sample(
                        string.ascii_letters+string.digits, 6)))
            else:
                code = VerificationCode.objects.get(email=data['email'])
            send_mail('電子郵件驗證', code.VerificationCode,
                      settings.DEFAULT_FROM_EMAIL, [data['email']])
            output = {'status': "0"}
        except:
            output = {'status': "1"}
        return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def check(request):  # 4.檢查驗證碼
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            emailcheck = VerificationCode.objects.get(email=data['email'])
            if data['code'] == emailcheck.VerificationCode:
                verification = UserProfile.objects.get(email=data['email'])
                verification.verified = True
                verification.save()
                emailcheck.delete()
                output = {'status': "0"}
            else:
                output = {'status': "1"}
        except:
            output = {'status': "1"}
        return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def forget_password(request):  # 5.忘記密碼(OK)
    if request.method == 'POST':
        inputdata = urllib.parse.unquote(
            (request.body).decode('UTF-8'))
        data = {i.split('=')[0]: i.split('=')[1] for i in inputdata.split('&')}
        try:
            password = ''.join(random.sample(
                string.ascii_letters+string.digits, 12))
            user = UserProfile.objects.get(email=data['email'])
            user.set_password(password)
            user.must_change_password = True
            user.save()
            send_mail('新密碼', password, settings.DEFAULT_FROM_EMAIL,
                      [data['email']])
            output = {'status': "0"}
        except:
            output = {'status': "1"}
        return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def reset_password(request):  # 6.重設密碼(OK)
    if request.method == 'POST':
        data = json.loads(request.body)
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                account = UserProfile.objects.get(
                    pk=(Session.objects.get(
                        pk=token['Bearer']).get_decoded())['user_id']
                )
                account.set_password(data['password'])
                account.must_change_password = False
                account.save()
                output = {'status': "0"}
        except:
            output = {'status': "1"}
        return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def share(request):  # 23.分享
    if request.method == 'POST':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                print(Session.objects.get(
                    pk=token['Bearer']).get_decoded())
                output = {'status': '0'}
        except:
            output = {'status': '1'}
        return JsonResponse({'status': '0'}, safe=False, json_dumps_params={'ensure_ascii': False})


@ csrf_exempt
def seeshare(request, type):  # 24.查看(X)
    if request.method == 'GET':
        # print(request.headers)
        # print(request.GET)
        # print(request.body)
        # print(request.headers['sessionid'])
        # token = {request.headers["Authorization"].split(
        #     ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        # try:
        #     if Session.objects.get(pk=token['Bearer']):
        output = {'status': '0'}
        # except:
        #     output = {'status': '1'}
        return JsonResponse({'status': '0'}, safe=False, json_dumps_params={'ensure_ascii': False})


@ csrf_exempt
def news(request):  # 29.最新消息(OK)
    if request.method == 'GET':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                output = {'status': '0'}
        except:
            output = {'status': '1'}
        return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@ csrf_exempt
def notification(request):  # 36.親友團通知
    if request.method == 'POST':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                output = {'status': '0'}
        except:
            output = {'status': '1'}
        return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@ csrf_exempt
def registercheck(request):  # 38.註冊確認(OK)
    if request.method == 'GET':
        try:
            output = {"status": "0"}
            if list(UserProfile.objects.filter(account=request.GET['account'])) != []:
                output = {"status": "1"}
        except:
            output = {"status": "1"}
        return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})
