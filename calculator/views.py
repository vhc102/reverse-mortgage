from django.shortcuts import render
from .forms import ReverseMortgageForm


def calculate_principal_limit(age, home_value, margin):
    # Basic formula for principal limit calculation (simplified)
    principal_limit = home_value * (0.5 + (age - 62) * 0.01) - (home_value * (margin / 100))
    return principal_limit


def mortgage_calculator(request):
    if request.method == 'POST':
        form = ReverseMortgageForm(request.POST)
        if form.is_valid():
            return render(request, 'calculator/result.html', {'form': form})
    else:
        form = ReverseMortgageForm()

    return render(request, 'calculator/calculator.html', {'form': form})
