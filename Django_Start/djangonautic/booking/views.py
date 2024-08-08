from django.shortcuts import render
from booking.models import Students

# Create your views here.
def home_view(request):
    stud = Students.objects.all()
    context = {'stud': stud}
    return render(request, "home.html", context)