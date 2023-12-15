from django.http import JsonResponse

def hello_world(request):
    data = {"message" : "hello world"}
    return JsonResponse(data)
