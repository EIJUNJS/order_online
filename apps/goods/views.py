from django.shortcuts import render


# https://127.1.0.8000
# Create your views here.
def index(res):
    '''front page'''
    return render(res, 'index.html')
