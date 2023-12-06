from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Sped Ran',
        'class': 'PBP S',
    }

    return render(request, "main.html", context)