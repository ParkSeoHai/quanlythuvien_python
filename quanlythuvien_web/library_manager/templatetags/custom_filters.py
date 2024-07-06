from django import template
from datetime import datetime

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def kqdays(ngay_hen_tra):
    today = datetime.now().strftime('%Y-%m-%d')
    a = datetime.strptime(ngay_hen_tra, "%Y-%m-%d")
    b = datetime.strptime(today, "%Y-%m-%d")
    date_muon = int((a - b).days)
    return date_muon
@register.filter
def kqdaysTra(ngay_hen_tra, ngay_tra):
    a = datetime.strptime(ngay_hen_tra, "%Y-%m-%d")
    b = datetime.strptime(ngay_tra, "%Y-%m-%d")
    date_muon = int((a - b).days)
    return date_muon
@register.filter
def Sum(numbers):
    kq = 0
    for number in numbers:
        kq = kq + number
    return kq