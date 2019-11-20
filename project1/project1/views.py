from django.http import JsonResponse
import random

COLORS = ['#4a4e4d', '#0e9aa7', '#3da4ab', '#f6cd61', '#fe8a71']

def api(request):
    maxValue = request.GET.get('max', 10)
    return JsonResponse({
        'x': random.randint(0, int(maxValue)),
        'y': random.randint(0, int(maxValue)),
        'color': random.choice(COLORS)
    })
