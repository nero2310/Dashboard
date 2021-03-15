from django import template

from math import floor

register = template.Library()


@register.filter
def round_currency(value, decimal_place=3):
    '''
    Round number to the nearest value,using half up method
    Example: 1.2 -> 1, 1.49 -> 1, 1.5 -> 2
    value - Number to round
    decimal_place - Round Precision
    Return - Rounded Value
    '''
    multipler = 10 ** decimal_place
    return floor(value * multipler + 0.5) / multipler
