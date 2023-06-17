from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def segitiga(request, number) : 
    numbers= []
    return HttpResponse(numbers)

def ganjil(request, number) : 
    numbers = []
    for i in number:
        if (i == 0) :
            continue
        else:
            if(number % 2) != 0:
                numbers.push(i)
    return HttpResponse(numbers)

def prima(request, number) : 
    numbers = []
    for i in number:
        if (i == 1):
            continue
        elif (i > 1):
            for j in range(2,i):
                if(i % j) == 0:
                    numbers.push(i)
                    break

    return HttpResponse(numbers)