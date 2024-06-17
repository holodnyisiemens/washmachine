from django.shortcuts import render, get_object_or_404
from .models import Service

menu = [
    {'title': 'Услуги', 'url_name': 'home'},
    {'title': 'Подробнее', 'url_name': 'more_info'},
]

header_title = 'Ремонт стиральных машин на дому Нижний Тагил'
main_description = 'Ремонт стиральных машин на дому Нижний Тагил. Без выходных, телефон: +7(950)206-21-38. Опытный мастер. Низкие цены, гарантия и качественные детали. Выезд бесплатно.'
main_keywords = '''ремонт стиральных машин на дому нижний тагил, ремонт бытовой техники нижний тагил недорого'''

info = {
    'header_title': header_title,
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
        'title': header_title,
        'description': main_description,
        'keywords': main_keywords,
        'services': Service.objects.filter(is_active=True),
        'menu': menu,
        'info': info,
    }
    return render(request, 'services/home.html', context=context)

def about_service(request, service_slug):
    s = get_object_or_404(Service, slug=service_slug)
    extended_title = f'{s.title} стиральной машины на дому Нижний Тагил'

    context = {
        'title': extended_title,
        'description': s.title + '. ' + main_description,
        'keywords': extended_title + ', ' + main_keywords,
        's': s,
        'menu': menu,
        'info': info,
    }
    return render(request, 'services/about_service.html', context)

def more_info(request):
    context = {
        'title': header_title,
        'description': main_description,
        'keywords': main_keywords,
        'menu': menu,
        'info': info,
    }
    return render(request, 'services/more_info.html', context)

def page_not_found(request, exception):
    context = {
        'title': header_title,
        'description': main_description,
        'keywords': main_keywords,
        'menu': menu,
        'info': info,
    }
    return render(request, 'services/page_not_found.html', context)
