from django.shortcuts import render, redirect

# Create your views here.
def map(request):
  print('map 왔음')
  return render(request, 'building/map.html')