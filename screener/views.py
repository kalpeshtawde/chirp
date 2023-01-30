from django.shortcuts import render


def stockplot(request):
    return render(request, 'chart.html')
