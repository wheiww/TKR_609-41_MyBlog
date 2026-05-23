from django.shortcuts import render

def homepage(request):
    data = {"header": "Добро пожаловать в NifiБлог!", "message": "Жизнь с Нифи."}
    return render(request, "homepage.html", context=data)

def about(request):
    header = "О нас"
    staff = ['Камилла Таджибова', 'Камиллка', 'Камилла Руслановна']
    director = {"name": "Камилла Таджибова"}
    address = ('ул. Кошачья, 1', 'Сургут', 'Россия')
    data = {"header": header, "staff": staff, "director": director, "address": address}
    return render(request, 'about.html', data)