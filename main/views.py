from django.shortcuts import render
from  django.http import JsonResponse, HttpResponse


def json_response(request):
    print('ff')


def http_response(request):
    print('ff')


def say_hello(req):
   return HttpResponse("<h1> hello Mona me </h1>")


def user_profile(request):
    return JsonResponse({
        'firstname':'PERIS',
        'lastname': "MUTHONI",
        'age': 89,
        'phoneNumber': '2456754334567545'
    })


data_records = {
    1: {"id": 1, "karen": "Avoid her for your own good", "Abijan": "beautiful but dangerous"},
    2: {"id": 2, "Bena-bena": "Good", "Lagos": "Value 2"},
    3: {"id": 3, "sila": "Good 3", "Harare": "Value 3"},
    4: {"id": 3, "Jude": "No good", "Accra": "Java hundred percent but forgets he like plantain"}
}   


def filter_queries(request, query_id):
    try:
        record = data_records[int(query_id)]
        return JsonResponse(record, status=200)
    except KeyError:
        return JsonResponse({'error': 'Record not found'}, status=404)


