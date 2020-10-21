from django.shortcuts import render, redirect

from .models import Passwords

# Create your views here.


def home(request):
    if request.user.is_authenticated:
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
    else:
        return redirect("login")


def delete(request, id):
    Passwords.objects.get(id=id).delete()
    return redirect('home')


def update(request, id, val):
    pwd = Passwords.objects.get(id=id)
    if request.method == 'POST':
        if val != 'form':
            website_url = request.POST["website_url"]
            website_name = request.POST["website_name1"]
            email = request.POST["Email_User1"]
            password = request.POST["password1"]
            pwd.website_url = website_url
            pwd.website_name = website_name
            pwd.email = email
            pwd.password = password
            pwd.save()
            return redirect("home")
        return render(request, 'update.html', {
            'pas': pwd
        })
    return render(request, 'update.html', {
        'pas': pwd
    })


def search(request, id):
    if request.method == 'POST':
        qu = request.POST["web"]
        webs = []
        webs += (list(Passwords.objects.filter(website_name__icontains=qu, user_id=id)))
        webs += (list(Passwords.objects.filter(website_url__icontains=qu, user_id=id)))
        webs += (list(Passwords.objects.filter(email__icontains=qu, user_id=id)))

        return render(request, 'home.html', {'websites': webs})
    return render(request, 'home.html')
