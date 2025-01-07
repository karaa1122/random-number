from django.shortcuts import render
from .utils import generate_unique_number_and_message

def random_number_view(request):
    number, message = generate_unique_number_and_message()
    context = {
        "number": number,
        "message": message,
    }
    return render(request, "random_number.html", context)
