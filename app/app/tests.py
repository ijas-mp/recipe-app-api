'''
sample test
'''

from django.test import SimpleTestCase
from app import calc


class calcTests(SimpleTestCase):
    def test_add_no(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_substract_no(self):
        res = calc.substract(10, 15)
        self.assertEqual(res, 5)
