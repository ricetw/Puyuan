import time
import json
from datetime import datetime
from django.contrib.sessions.models import Session
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from User.models import *
from Body.models import *
from Friend.models import *

# Create your views here.


@csrf_exempt
def user(request):  # 7.個人資訊設定(OK)/12.個人資訊(OK?)
    if request.method == 'PATCH':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                data = json.loads(request.body)
                user = UserProfile.objects.get(
                    pk=(Session.objects.get(
                        pk=token['Bearer']).get_decoded())['user_id'])
                for key, value in data.items():
                    if key == 'name':
                        user.name = value
                    elif key == 'birthday':
                        user.birthday = value
                    elif key == 'height':
                        user.height = value
                    elif key == 'gender':
                        user.gender = value
                    elif key == 'fcm_id':
                        user.fcm_id = value
                    elif key == 'address':
                        user.address = value
                    elif key == 'weight':
                        user.weight = value
                    elif key == 'phone':
                        user.phone = value
                    elif key == 'email':
                        user.email = value
                user.save()
                output = {'status': "0"}
        except:
            output = {'status': "1"}
    elif request.method == 'GET':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                userprofile = UserProfile.objects.get(
                    pk=(Session.objects.get(
                        pk=token['Bearer']).get_decoded())['user_id'])
                userdefault = UserDefault.objects.get(user_id=userprofile.pk)
                usersetting = UserSetting.objects.get(user_id=userprofile.pk)
                output = {'status': "0",
                          'user': {"id": userprofile.pk,
                                   "name": userprofile.name,
                                   "account": userprofile.account,
                                   "email": userprofile.email,
                                   "phone": userprofile.phone,
                                   "fb_id": userprofile.fb_id,
                                   "status": userprofile.status,
                                   "group": userprofile.group,
                                   "birthday": userprofile.birthday,
                                   "height": userprofile.height,
                                   "weight": userprofile.weight,
                                   "gender": userprofile.gender,
                                   "address": userprofile.address,
                                   "unread_records": userprofile.unread_records,
                                   "verified": userprofile.verified,
                                   "privacy_policy": userprofile.privacy_policy,
                                   "must_change_password": userprofile.must_change_password,
                                   "fcm_id": userprofile.fcm_id,
                                   "badge": userprofile.badge,
                                   "login_times": userprofile.login_times,
                                   "created_at": datetime.strftime(userprofile.created_at, '%Y-%m-%d %H:%M:%S'),
                                   "updated_at": datetime.strftime(userprofile.updated_at, '%Y-%m-%d %H:%M:%S'),
                                   "default": {"id": userdefault.pk,
                                               "user_id": userdefault.user_id,
                                               "sugar_delta_max": userdefault.sugar_delta_max,
                                               "sugar_delta_min": userdefault.sugar_delta_min,
                                               "sugar_morning_max": userdefault.sugar_morning_max,
                                               "sugar_morning_min": userdefault.sugar_morning_min,
                                               "sugar_evening_max": userdefault.sugar_evening_max,
                                               "sugar_evening_min": userdefault.sugar_evening_min,
                                               "sugar_before_max": userdefault.sugar_before_max,
                                               "sugar_before_min": userdefault.sugar_before_min,
                                               "sugar_after_max": userdefault.sugar_after_max,
                                               "sugar_after_min": userdefault.sugar_after_min,
                                               "systolic_max": userdefault.systolic_max,
                                               "systolic_min": userdefault.systolic_min,
                                               "diastolic_max": userdefault.diastolic_max,
                                               "diastolic_min": userdefault.diastolic_min,
                                               "pulse_max": userdefault.pulse_max,
                                               "pulse_min": userdefault.pulse_min,
                                               "weight_max": userdefault.weight_max,
                                               "weight_min": userdefault.weight_min,
                                               "bmi_max": userdefault.bmi_max,
                                               "bmi_min": userdefault.bmi_min,
                                               "body_fat_max": userdefault.body_fat_max,
                                               "body_fat_min": userdefault.body_fat_min,
                                               "created_at": datetime.strftime(userprofile.created_at, '%Y-%m-%d %H:%M:%S'),
                                               "updated_at": datetime.strftime(userprofile.updated_at, '%Y-%m-%d %H:%M:%S')},
                                    "setting": {"id": usersetting.pk,
                                                "user_id": usersetting.user_id,
                                                "after_recording": usersetting.after_recording,
                                                "no_recording_for_a_day": usersetting.no_recording_for_a_day,
                                                "over_max_or_under_min": usersetting.over_max_or_under_min,
                                                "after_meal": usersetting.after_meal,
                                                "unit_of_sugar": usersetting.unit_of_sugar,
                                                "unit_of_weight": usersetting.unit_of_weight,
                                                "unit_of_height": usersetting.unit_of_height,
                                                "created_at": datetime.strftime(userprofile.created_at, '%Y-%m-%d %H:%M:%S'),
                                                "updated_at": datetime.strftime(userprofile.updated_at, '%Y-%m-%d %H:%M:%S')}}}
        except:
            output = {'status': "1"}
    return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def bloodpressure(request):  # 8.上傳血壓(OK?)
    if request.method == 'POST':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                data = json.loads(request.body)
                BloodPressure.objects.create(
                    user_id=(Session.objects.get(
                        pk=token['Bearer']).get_decoded())['user_id'], systolic=data["systolic"],
                    diastolic=data["diastolic"], pulse=data["pulse"], recorded_at=data["recorded_at"]
                )
                output = {'status': "0"}
        except:
            output = {'status': "1"}
        return JsonResponse(output, safe=True, json_dumps_params={'ensure_ascii': True})


@ csrf_exempt
def weight(request):  # 9.上傳體重(OK?)
    if request.method == 'POST':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                data = json.loads(request.body)
                Weight.objects.create(
                    user_id=(Session.objects.get(
                        pk=token['Bearer']).get_decoded())['user_id'], weight=data[
                        "weight"], body_fat=data["body_fat"], bmi=data["bmi"], recorded_at=data["recorded_at"]
                )
                output = {'status': "0"}
        except:
            output = {'status': "1"}
        return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@ csrf_exempt
def bloodsuger(request):  # 10.上傳血糖(OK?)
    if request.method == 'POST':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                data = json.loads(request.body)
                BloodSugar.objects.create(
                    user_id=(Session.objects.get(
                        pk=token['Bearer']).get_decoded())['user_id'],
                    sugar=data["sugar"], timeperiod=data["timeperiod"], recorded_at=data["recorded_at"]
                )
                output = {'status': "0"}
        except:
            output = {'status': "1"}
        return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@ csrf_exempt
def userdefault(request):  # 11.個人預設值(OK)
    if request.method == 'PATCH':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                data = json.loads(request.body)
                user = UserDefault.objects.get(
                    user_id=(Session.objects.get(
                        pk=token['Bearer']).get_decoded())['user_id'])
                for key, value in data.items():
                    if key == 'sugar_delta_max':
                        user.sugar_delta_max = value
                    elif key == 'sugar_delta_min':
                        user.sugar_delta_min = value
                    elif key == 'sugar_morning_max':
                        user.sugar_morning_max = value
                    elif key == 'sugar_morning_min':
                        user.sugar_morning_min = value
                    elif key == 'sugar_evening_max':
                        user.sugar_evening_max = value
                    elif key == 'sugar_evening_min':
                        user.sugar_evening_min = value
                    elif key == 'sugar_before_max':
                        user.sugar_before_max = value
                    elif key == 'sugar_before_min':
                        user.sugar_before_min = value
                    elif key == 'sugar_after_max':
                        user.sugar_after_max = value
                    elif key == 'sugar_after_min':
                        user.sugar_after_min = value
                    elif key == 'systolic_max':
                        user.systolic_max = value
                    elif key == 'systolic_min':
                        user.systolic_min = value
                    elif key == 'diastolic_max':
                        user.diastolic_max = value
                    elif key == 'diastolic_min':
                        user.diastolic_min = value
                    elif key == 'pulse_max':
                        user.pulse_max = value
                    elif key == 'pulse_min':
                        user.pulse_min = value
                    elif key == 'weight_max':
                        user.weight_max = value
                    elif key == 'weight_min':
                        user.weight_min = value
                    elif key == 'bmi_max':
                        user.pulse_max = value
                    elif key == 'bmi_min':
                        user.pulse_min = value
                    elif key == 'body_fat_max':
                        user.body_fat_max = value
                    elif key == 'body_fat_min':
                        user.body_fat_min = value
                user.save()
                output = {'status': "0"}
        except:
            output = {'status': "1"}
        return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@ csrf_exempt
def diary(request):  # 14.日記列表資料(OK?)
    if request.method == 'GET':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                timenow = time.strftime("%Y-%m-%d", time.localtime())
                bloodpressureinfo = BloodPressure.objects.values().filter(
                    user_id=(Session.objects.get(
                        pk=token['Bearer']).get_decoded())['user_id'], recorded_at__contains=timenow)
                weightinfo = Weight.objects.values().filter(
                    user_id=(Session.objects.get(
                        pk=token['Bearer']).get_decoded())['user_id'], recorded_at__contains=timenow)
                bloodsugerinfo = BloodSugar.objects.values().filter(
                    user_id=(Session.objects.get(
                        pk=token['Bearer']).get_decoded())['user_id'], recorded_at__contains=timenow)
                dietinfo = Diet.objects.values().filter(
                    user_id=(Session.objects.get(
                        pk=token['Bearer']).get_decoded())['user_id'], recorded_at__contains=timenow)
                infolist = []  # append/extend
                for i in list(bloodpressureinfo):
                    infolist.append({"id": i['id'],
                                    "user_id": i['user_id'],
                                     "systolic": i['systolic'],
                                     "diastolic": i['diastolic'],
                                     "pulse": i['pulse'],
                                     "recorded_at": str(i['recorded_at'].replace(tzinfo=None)),
                                     "type": "blood_pressure"
                                     })
                for i in list(weightinfo):
                    infolist.append({"id": i['id'],
                                    "user_id": i['user_id'],
                                     "weight": i['weight'],
                                     "body_fat": i['body_fat'],
                                     "bmi": i['bmi'],
                                     "recorded_at": str(i['recorded_at'].replace(tzinfo=None)),
                                     "type": "weight"
                                     })
                for i in list(bloodsugerinfo):
                    infolist.append({"id": i['id'],
                                    "user_id": i['user_id'],
                                     "sugar": i['sugar'],
                                     "timeperiod": i['timeperiod'],
                                     "recorded_at": str(i['recorded_at'].replace(tzinfo=None)),
                                     "type": "blood_sugar"
                                     })
                for i in list(dietinfo):
                    infolist.append({"id": i['id'],
                                    "user_id": i['user_id'],
                                     "description": i['description'],
                                     "meal": i['meal'],
                                     "tag": i['tag'],
                                     "image": list({
                                         "https://i.imgur.com/2UOau4R.png"
                                     }),
                                     "location": {
                        "lat": i['lat'],
                        "lng": i['lng']
                    },
                        "recorded_at": str(i['recorded_at'].replace(tzinfo=None)),
                        "type": "diet",
                        "reply": "安安"
                    })
                output = {'status': '0',
                          'diary': infolist}
        except:
            output = {'status': '1'}
        return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@ csrf_exempt
def diet(request):  # 15.飲食日記
    if request.method == 'POST':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                data = json.loads(request.body)
                Diet.objects.create(user_id=(Session.objects.get(
                    pk=token['Bearer']).get_decoded())['user_id'], description=data['description'],
                    meal=data['meal'], tag=data['tag'], image=data['image'], lat=data['lat'], lng=data['lng'], recorded_at=data['recorded_at']
                )
            output = {'status': '0',
                      'image_url': 'https://i.imgur.com/2UOau4R.png'}
        except:
            output = {'status': '1'}
        return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@ csrf_exempt
def lastupload(request):  # 25.最後上傳時間
    if request.method == 'GET':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                user = (Session.objects.get(
                    pk=token['Bearer']).get_decoded())['user_id']
                blood_pressure = BloodPressure.objects.filter(
                    user_id=user.user_id
                ).order_by('-recorded_at')[0].get().recorded_at
                weight = Weight.objects.filter(
                    user_id=user.user_id
                ).order_by('-recorded_at')[0].get().recorded_at
                blood_suger = BloodSugar.objects.filter(
                    user_id=user.user_id
                ).order_by('-recorded_at')[0].get().recorded_at
                diet = Diet.objects.filter(
                    user_id=user.user_id
                ).order_by('-recorded_at')[0].get().recorded_at
                output = {'status': '0',
                          'last_upload': {
                              'blood_pressure': blood_pressure,
                              'weight': weight,
                              'blood_suger': blood_suger,
                              'diet': diet
                          }}
        except:
            output = {'status': '1'}
        return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@ csrf_exempt
def care(request):  # 27. 獲取關懷諮詢/28. 發送關懷諮詢/試試看
    if request.method == 'GET':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                cares = []
                count = Care.objects.values().filter(reply_id=(Session.objects.get(
                    pk=token['Bearer']).get_decoded())['user_id'])
                for i in list(count):
                    cares.append({"id": i['pk'],
                                  "user_id": i['user_id'],
                                  "member_id": i['member_id'],
                                  "reply_id": i['reply_id'],
                                  "message": i['message'],
                                  "created_at": i['created_at'],
                                  "updated_at": i['updated_at']
                                  })
                output = {'status': '0',
                          'cares': cares}
        except:
            output = {'status': '1'}
    elif request.method == 'POST':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                data = json.loads(request.body)
                output = {'status': '0'}
        except:
            output = {'status': '1'}
    return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@ csrf_exempt
def medical(request):  # 30.就醫資訊(OK)/31.更新就醫資訊(OK)/for/elif
    if request.method == 'PATCH':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                data = json.loads(request.body)
                medical = Medical.objects.get(
                    user_id=(Session.objects.get(
                        pk=token['Bearer']).get_decoded())['user_id'])
                for key, value in data.items():
                    if key == 'diabetes_type':
                        medical.diabetes_type = value
                    elif key == 'oad':
                        medical.oad = value
                    elif key == 'insulin':
                        medical.insulin = value
                    elif key == 'anti_hypertensives':
                        medical.anti_hypertensives = value
                medical.save()
                output = {'status': "0"}
        except:
            output = {'status': "1"}
    elif request.method == 'GET':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                medical_info = Medical.objects.get(user_id=(Session.objects.get(
                    pk=token['Bearer']).get_decoded())['user_id'])
                output = {'status': "0",
                          'medical_info': {'id': medical_info.pk,
                                           'user_id': medical_info.user_id,
                                           'diabetes_type': medical_info.diabetes_type,
                                           'oad': medical_info.oad,
                                           'insulin': medical_info.insulin,
                                           'anti_hypertensives': medical_info.anti_hypertensives,
                                           'created_at': medical_info.created_at,
                                           'updated_at': medical_info.updated_at
                                           }}
            else:
                output = {'status': "1"}
        except:
            output = {'status': "1"}
    return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@ csrf_exempt
def alc(request):  # 32.糖化血色素(OK?)/33.送糖化血色素(OK)/34.刪除糖化血色素(OK)
    if request.method == 'POST':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                data = json.loads(request.body)
                Alc.objects.create(user_id=(Session.objects.get(
                    pk=token['Bearer']).get_decoded())['user_id'], a1c=data["a1c"],
                    recorded_at=data["recorded_at"])
            output = {"status": "0"}
        except:
            output = {"status": "1"}
    elif request.method == 'GET':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                info = Alc.objects.values().filter(user_id=(Session.objects.get(
                    pk=token['Bearer']).get_decoded())['user_id'])
                A1clist = []
                for i in list(info):
                    A1clist.append({"id": i['id'],
                                    "user_id": int(i['user_id']),
                                    "a1c": str(i['a1c']),
                                    "recorded_at": datetime.strftime(i['recorded_at'], '%Y-%m-%d %H:%M:%S'),
                                    "created_at": datetime.strftime(i['created_at'], '%Y-%m-%d %H:%M:%S'),
                                    "updated_at": datetime.strftime(i['updated_at'], '%Y-%m-%d %H:%M:%S'),
                                    })
                output = {'status': "0",
                          'a1cs': A1clist}
        except:
            output = {"status": "1"}
    elif request.method == 'DELETE':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                data = json.loads(request.body)
                for id in data["ids"]:
                    try:
                        delete = Alc.objects.get(pk=id)
                        delete.delete()
                    except:
                        pass
                output = {"status": "0"}
        except:
            output = {"status": "1"}
    return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@ csrf_exempt
def usersetting(request):  # 35.個人設定(OK)/for
    if request.method == 'PATCH':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                data = json.loads(request.body)
                user = UserSetting.objects.get(
                    user_id=(Session.objects.get(
                        pk=token['Bearer']).get_decoded())['user_id'])
                for key, value in data:
                    if key == 'after_recording':
                        user.after_recording = value
                    elif key == 'no_recording_for_a_day':
                        user.no_recording_for_a_day = value
                    elif key == 'over_max_or_under_min':
                        user.over_max_or_under_min = value
                    elif key == 'after_meal':
                        user.after_meal = value
                    elif key == 'unit_of_sugar':
                        user.unit_of_sugar = value
                    elif key == 'unit_of_weight':
                        user.unit_of_weight = value
                    elif key == 'unit_of_height':
                        user.unit_of_height = value
                user.save()
                output = {'status': "0"}
        except:
            output = {'status': "1"}
    return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@ csrf_exempt
def badge(request):  # 39.更新badge(OK)
    if request.method == 'PUT':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                data = json.loads(request.body)
                user = UserProfile.objects.get(pk=(Session.objects.get(
                    pk=token['Bearer']).get_decoded())['user_id'])
                user.badge = data['badge']
                user.save()
                output = {'status': '0'}
        except:
            output = {'status': '1'}
    return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@ csrf_exempt
def drug(request):  # 41.藥物資訊(OK?)/42.上傳藥物資訊(OK)/43.刪除藥物資訊(OK)
    if request.method == 'POST':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                data = json.loads(request.body)
                Drug.objects.create(user_id=(Session.objects.get(
                    pk=token['Bearer']).get_decoded())['user_id'],
                    type=data["type"], name=data['name'], recorded_at=data["recorded_at"])
                output = {"status": "0"}
        except:
            output = {"status": "1"}
    elif request.method == 'GET':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                drug_useds = Drug.objects.values().filter(user_id=(Session.objects.get(
                    pk=token['Bearer']).get_decoded())['user_id'])
                output = {'status': "0",
                          'drug_useds': list(drug_useds)}
        except:
            output = {"status": "1"}
    elif request.method == 'DELETE':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                data = json.loads(request.body)
                for id in data["ids"]:
                    try:
                        delete = Drug.objects.get(pk=id)
                        delete.delete()
                    except:
                        pass
                output = {"status": "0"}
        except:
            output = {"status": "1"}
    return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})


@ csrf_exempt
def records(request):  # 40.刪除日誌紀錄/44.上一筆紀錄資訊/改44.
    if request.method == 'POST':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                data = json.loads(request.body)
                blood_pressure = BloodPressure.objects.filter(
                    user_id=(Session.objects.get(
                        pk=token['Bearer']).get_decoded())['user_id']
                ).order_by('-recorded_at')[:1].get()
                weight = Weight.objects.filter(
                    user_id=(Session.objects.get(
                        pk=token['Bearer']).get_decoded())['user_id']
                ).order_by('-recorded_at')[:1].get()
                try:
                    blood_suger = BloodSugar.objects.filter(
                        user_id=(Session.objects.get(
                            pk=token['Bearer']).get_decoded())['user_id'], timeperiod=data['diets']
                    ).order_by('-recorded_at')[:1].get()
                except:
                    pass
                try:
                    output = {'status': '0',
                              'blood_sugers': {
                                  'id': blood_suger.pk,
                                  'user_id': blood_suger.user_id,
                                  "sugar": blood_suger.sugar,
                                  "exercise": blood_suger.exercise,
                                  "drug": blood_suger.drug,
                                  "timeperiod": blood_suger.timeperiod,
                                  "recorded_at": str(blood_suger.recorded_at.replace(tzinfo=None))
                              },
                              "blood_pressures": {
                                  "id": blood_pressure.pk,
                                  "user_id": blood_pressure.user_id,
                                  "systolic": blood_pressure.systolic,
                                  "diastolic": blood_pressure.diastolic,
                                  "pulse": blood_pressure.pulse,
                                  "recorded_at": str(blood_pressure.recorded_at.replace(tzinfo=None))
                              },
                              "weights": {
                                  "id": weight.pk,
                                  "user_id": weight.user_id,
                                  "weight": weight.weight,
                                  "body_fat": weight.body_fat,
                                  "bmi": weight.bmi,
                                  "recorded_at": str(weight.recorded_at.replace(tzinfo=None))
                              }
                              }
                except:
                    output = {'status': '0',
                              "blood_pressures": {
                                  "id": blood_pressure.pk,
                                  "user_id": blood_pressure.user_id,
                                  "systolic": blood_pressure.systolic,
                                  "diastolic": blood_pressure.diastolic,
                                  "pulse": blood_pressure.pulse,
                                  "recorded_at": str(blood_pressure.recorded_at.replace(tzinfo=None))
                              },
                              "weights": {
                                  "id": weight.pk,
                                  "user_id": weight.user_id,
                                  "weight": weight.weight,
                                  "body_fat": weight.body_fat,
                                  "bmi": weight.bmi,
                                  "recorded_at": weight.recorded_at
                              }}
        except:
            output = {'status': '1'}
    elif request.method == 'DELETE':
        token = {request.headers["Authorization"].split(
            ' ')[0]: request.headers["Authorization"].split(' ')[1]}
        try:
            if Session.objects.get(pk=token['Bearer']):
                data = json.loads(request.body)
                print(data)
                datalist = {
                    "blood_sugars": BloodSugar,
                    "blood_pressures": BloodPressure,
                    "weights": Weight,
                    "diets": Diet
                }
                for key, value in data.items():
                    for id in value:
                        datalist[key].objects.get(pk=id).delete()
            output = {"status": "0"}
        except:
            output = {"status": "1"}
    return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})
