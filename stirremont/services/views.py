from django.shortcuts import render, get_object_or_404
from .models import Service

menu = [
    {'title': 'Услуги', 'url_name': 'home'},
    {'title': 'Подробнее', 'url_name': 'more_info'},
]

meta_description = 'ремонт стиральных машин на дому нижний тагил'
meta_keywords = 'ремонт, стиральных машин, на дому, нижний тагил, в нижнем тагиле, не работает, стиральная машина, сломалась, как починить, течет, мастер, вызвать'

info = {
    'title': 'Ремонт стиральных машин на дому, Нижний Тагил',
    'phone': '+7(950)206-21-38',
    'name': 'Михаил',
    'schedule': 'График 09:00-20:00 без выходных',
    'footer': 'от 300 рублей за услугу',
    
    'brief_info_list': [
        'Низкие цены',
        'Качественные детали',
        'Опыт более 15 лет',
        'Выдаётся гарантийный талон',
        'Выезд бесплатно'
    ],

    'more_info_list': [
        'Работа по договору',
        'Возможна оплата картой',
        'Фронтальная и вертикальная загрузка',
        'Есть опыт работы с техникой премиум-класса',
        'Организация работы: у клиента или удаленно',
        'Машины: встраиваемые, отдельно стоящие, под раковину',
    ]
}

def home(request):
    context = {
        'services': Service.objects.filter(is_active=True),
        'menu': menu,
        'info': info,
        'meta_keywords': meta_keywords,
        'meta_description': meta_description,
    }
    return render(request, 'services/home.html', context=context)

def about_service(request, service_slug):
    context = {
        's': get_object_or_404(Service, slug=service_slug),
        'menu': menu,
        'info': info,
        'meta_keywords': meta_keywords,
        'meta_description': meta_description,
    }
    return render(request, 'services/about_service.html', context)

def more_info(request):
    context = {
        'menu': menu,
        'info': info,
        'meta_keywords': meta_keywords,
        'meta_description': meta_description,
    }
    return render(request, 'services/more_info.html', context)

def page_not_found(request, exception):
    context = {
        'menu': menu,
        'info': info,
        'meta_keywords': meta_keywords,
        'meta_description': meta_description,
    }
    return render(request, 'services/page_not_found.html', context)
