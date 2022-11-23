
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from app_weldlog.models import Weldlog
from app_weldlog.serializers import Weldlogserializers
import re

data = {"data": [
    {
        "id": "15",
        "line": "Albania",
        "isometry": "Bolivia",
        "spool": "China",
        "joint": "6",
        "dia": 68,
        "mat1": "Turquoise",
        "p1": 2,
        "mat2": "Goldenrod",
        "p2": 0,
        "fitupdate": "",
        "fitupresult": "X",
        "weldclass": "2t",
        "pwht": "Y",
        "wps": "X",
        "location": "AL",
        "weldtype": "Honorable",
        "welder": "X",
        "vtdate": "",
        "vtreport": "X",
        "pwhtdate": "",
        "pwhtreport": "X",
        "rtdate": "",
        "rtreportno": "X",
        "rtresult": "X",
        "penalty": "X",
        "tpno": "X",
        "cancel": "0",
        "rtrate": "",
        "pwhtrate": 10
    },
]}


@csrf_exempt
def getWeldlog(request):
    if request.method == 'GET':
        welds = Weldlog.objects.all()
        weldlog_serializers = Weldlogserializers(welds, many=True)
        response_data = {"data": weldlog_serializers.data}

        # response_data=data

        return JsonResponse(response_data, safe=False)


@csrf_exempt
def getWeldlogs(request):
    if request.method == 'GET':
        welds = Weldlog.objects.all()
        weldlog_serializers = Weldlogserializers(welds, many=True)
        response_data = {"data": weldlog_serializers.data}

        return JsonResponse(response_data, safe=False)

    elif request.method == 'POST':
        if request.POST.get('action') == 'edit':
            print("------------------")
            print(request.POST)
            print(list(request.POST.dict().values())[0])
            key_list = list(request.POST.dict().keys())
            value_list = list(request.POST.dict().values())
            keyS = key_list[0]
            print(re.findall('\[(.*?)\]', keyS))
            print(re.findall('\[(.*?)\]', keyS)[0])

            for row in data["data"]:
                if row["id"] == re.findall('\[(.*?)\]', keyS)[0]:
                    new_data = row

            for index, key in enumerate(key_list[:-1]):
                # print(re.findall('\[(.*?)\]', key))
                # print(value_list[index])
                key_1 = re.findall('\[(.*?)\]', key)[1]
                new_data[key_1] = value_list[index]

            response_data = {
                "data": [
                    new_data
                ]
            }

            return JsonResponse(response_data, safe=False)

        if request.POST.get('action') == 'create':
            print("------------------")
            print(request.POST)
            print(request.POST.get('action'))
            key_list = list(request.POST.dict().keys())
            value_list = list(request.POST.dict().values())

            created_row = {
                "id": "5",
                "line": "Alb",
                "isometry": "Boli",
                "spool": "Chin",
                "joint": "6",
                "dia": 68,
                "mat1": "Turq",
                "p1": 2,
                "mat2": "Golde",
                "p2": 0,
                "fitupdate": "2022-01-01",
                "fitupresult": "X",
                "weldclass": "2t",
                "pwht": "Y",
                "wps": "X",
                "location": "AL",
                "weldtype": "Honorable",
                "welder": "X",
                "vtdate": "2022-01-01",
                "vtreport": "X",
                "pwhtdate": "2022-01-01",
                "pwhtreport": "X",
                "rtdate": "2022-01-01",
                "rtreportno": "X",
                "rtresult": "X",
                "penalty": "X",
                "tpno": "X",
                "cancel": "0",
                "rtrate": 0,
                "pwhtrate": 10
            }

            for index, key in enumerate(key_list[:-1]):
                print(re.findall('\[(.*?)\]', key))
                print(value_list[index])
                key_1 = re.findall('\[(.*?)\]', key)[1]
                if value_list[index] != "":
                    created_row[key_1] = value_list[index]

            print(created_row)
            weldrecord = Weldlog(
                line=created_row["line"],
                isometry=created_row["isometry"],
                spool=created_row["spool"],
                joint=created_row["joint"],
                dia=created_row["dia"],
                mat1=created_row["mat1"],
                p1=created_row["p1"],
                mat2=created_row["mat2"],
                p2=created_row["p2"],
                fitupdate=created_row["fitupdate"],
                fitupresult=created_row["fitupresult"],
                weldclass=created_row["weldclass"],
                pwht=created_row["pwht"],
                wps=created_row["wps"],
                location=created_row["location"],
                weldtype=created_row["weldtype"],
                welder=created_row["welder"],
                vtdate=created_row["vtdate"],
                vtreport=created_row["vtreport"],
                pwhtdate=created_row["pwhtdate"],
                pwhtreport=created_row["pwhtreport"],
                rtdate=created_row["rtdate"],
                rtreportno=created_row["rtreportno"],
                rtresult=created_row["rtresult"],
                penalty=created_row["penalty"],
                tpno=created_row["tpno"],
                cancel=created_row["cancel"],
                rtrate=created_row["rtrate"],
                pwhtrate=created_row["pwhtrate"],
            )
            weldrecord.save()
            created_row["id"] = str(weldrecord.id)

            response_data = {
                "data": [
                    created_row
                ]
            }
            return JsonResponse(response_data, safe=False)

        if request.POST.get('action') == 'remove':
            response_data = {
                "data": []
            }
            return JsonResponse(response_data, safe=False)
