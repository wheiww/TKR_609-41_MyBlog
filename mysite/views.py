from django.shortcuts import render

def homepage(request):
    data = {"header": "Добро пожаловать в КошкоБлог!", "message": "Всё о жизни с кошкой."}
    return render(request, "homepage.html", context=data)

def about(request):
    header = "О нас"
    staff = ['Камилла Таджибова', 'Иван Иванов', 'Мария Петрова']
    director = {"name": "Камилла Таджибова"}
    address = ('ул. Кошачья, 1', 'Сургут', 'Россия')
    data = {"header": header, "staff": staff, "director": director, "address": address}
    return render(request, 'about.html', data)