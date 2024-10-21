from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputUpperLimit
# Create your views here.
from utils import slieve

    
def home(request):
    if request.method == 'POST':
        num = int(request.POST['upper_limit'])
        prime_list = slieve(num)
        l = len(prime_list)
        return render(request, 'result.html', {'result': prime_list, 'n': num, 'l': l})

    else: 
        form = InputUpperLimit()
        return render(request, "home.html", {"form": form})
def janika(request): 
    return HttpResponse("janika csinalta")
