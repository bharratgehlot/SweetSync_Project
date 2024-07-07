from django.shortcuts import render

def test_page(request):
  return render(request, 'SweetSync/test_page.html')

def test_page2(request):
  return render(request, 'SweetSync/test_page2.html')
