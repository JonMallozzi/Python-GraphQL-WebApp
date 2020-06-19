from django.shortcuts import render
from pythongraphql.models import users

# Create your views here.
def user_detail(request, pk):
    users_object = users.objects.get(pk=pk)
    
    context = {
        "users": users_object
    }

    return render(request,"user_detail.html", context)