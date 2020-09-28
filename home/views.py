from django.shortcuts import render, redirect

from .models import Passwords

# Create your views here.


def home(request):
    if request.method == 'POST':
        website_url = request.POST["website"]
        website_name = request.POST["website_name"]
        email = request.POST["Email_User"]
        password = request.POST["password"]
        user_id = request.POST['user_id']
        # print(user_id)
        website = Passwords(website_url=website_url,
                            website_name=website_name, email=email, password=password, user_id=user_id)
        website.save()
    user_id = request.user.id
    websites = Passwords.objects.filter(user_id=user_id)
    return render(request, 'home.html', {'websites': websites, })


def delete(request, id):
    Passwords.objects.get(id=id).delete()
    return redirect('home')
