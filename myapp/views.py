from django.shortcuts import render


def index(request):
    # ctx = {"message": "Hello, Good Evening!"}
    
    return render(request, "index.html")

def contact(request):
    # ctx = {"message": "Hello, Good Evening!"}
    
    return render(request, "contact.html")