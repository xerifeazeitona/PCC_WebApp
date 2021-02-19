from django.shortcuts import render

def index(request):
    """The home page for meal plans."""
    return render(request, 'meal_plans/index.html')
