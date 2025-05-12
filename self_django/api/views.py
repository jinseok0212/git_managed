from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

def hello(request):
    return HttpResponse("안녕하세요")

@csrf_exempt
def posthello(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        return JsonResponse({
            'message' : f'{name} 반가워요.' if name else '무명이시군요.',
            'age' : f'{age}살이군요.' if age else '나이를 모르시군요.',
        },
        json_dumps_params={'ensure_ascii': False},
        )
    else:
        return JsonResponse(
            {'message' : '적절한 요청이 아닙니다.'},
            json_dumps_params={'ensure_ascii': False}, 
        )

