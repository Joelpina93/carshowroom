from django.shortcuts import render
from listings.models import Listing
from salesman.models import Salesman
from listings.choices import price_choices, door_choices, state_choices


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'door_choices': door_choices,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    salesman = Salesman.objects.order_by('-hire_date')

    mvp_salesman = Salesman.objects.all().filter(is_mvp=True)

    context = {
        'salesman': salesman,
        'mvp_salesman': mvp_salesman
    }
    return render(request, 'pages/about.html', context)
