from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def start(request):
    return render(request, 'start.html')

def result(request):
    name = request.GET['name']
    spoon = [1, 2, 3, 4, 5]
    result = ['못생김', '매력', '수명', '재력', '예쁨', '귀여움']
    random.shuffle(spoon)
    random.shuffle(result)
    return render(request, 'result.html', {'name':name, 'spoon':spoon, 'result':result })
    
