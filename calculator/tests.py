from django.test import TestCase
from .forms import ReverseMortgageForm
from .views import calculate_principal_limit


class ReverseMortgageTestCase(TestCase):
    def test_principal_limit_calculation(self):
        age = 70
        home_value = 300000
        margin = 3
        expected_principal_limit = 300000 * (0.5 + (70 - 62) * 0.01) - (300000 * (3 / 100))
        self.assertAlmostEqual(calculate_principal_limit(age, home_value, margin), expected_principal_limit)

    def test_form_validation(self):
        form_data = {'age': 70, 'home_value': 300000, 'margin': '3'}
        form = ReverseMortgageForm(data=form_data)
        self.assertTrue(form.is_valid())
