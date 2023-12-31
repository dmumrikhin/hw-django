from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def omlet(request):
    context = {}
    context['omlet'] = DATA['omlet']
    servings = int(request.GET.get('servings', 1))
    for key, value in context['omlet'].items():
        context['omlet'][key] = value * servings
    return render(request, 'calculator/omlet.html', context)
    
def pasta(request):
    context = {}
    context['pasta'] = DATA['pasta']
    servings = int(request.GET.get('servings', 1))
    for key, value in context['pasta'].items():
        context['pasta'][key] = value * servings
    return render(request, 'calculator/pasta.html', context)

def buter(request):
    context = {}
    context['buter'] = DATA['buter']
    servings = int(request.GET.get('servings', 1))
    for key, value in context['buter'].items():
        context['buter'][key] = value * servings
    return render(request, 'calculator/buter.html', context)
