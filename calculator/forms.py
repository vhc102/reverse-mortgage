from django import forms


class ReverseMortgageForm(forms.Form):
    home_value = forms.IntegerField(label='Home Value')
    margin = forms.DecimalField(label='Margin', max_digits=5, decimal_places=2)
    # age = forms.IntegerField(label='Age')
    # home_value = forms.IntegerField(label='Home Value')
    # margin = forms.ChoiceField(label='Margin', choices=[(i, f'{i}%') for i in range(1, 6)])
