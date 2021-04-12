from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        full_name = request.POST['full_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if not full_name:
            messages.info(
                request, 'İsim-Soyisim alanı doldurulması gereken bir alandır.')
        elif len(password1) < 6:
            messages.info(request, 'Şifreniz en az 6 karakterden oluşmalıdır.')
        elif User.objects.filter(email=email):
            messages.error(request, 'Email adresiniz daha önce başka bir kullanıcı tarafından kullanılmıştır.Eğer şifrenizi unuttuysanız "Giriş Yap" kısmında yer alan "Şifremi Unuttum" seçeneğini kullanabilirsiniz.Bir terslik olduğunu düşünüyorsanız lütfen bizimle iletişime geçiniz.')
        elif len(first_name) < 5:
            messages.info(
                request, 'İsim Soyisim en az 5 karakterden oluşmalıdır.')
        else:
            if password1 == password2:
                pass
    else:
        pass


def login(request):
    pass


def logout(request):
    pass


def todolist(request):
    pass
