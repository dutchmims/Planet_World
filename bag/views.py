from django.shortcuts import render
from .models import Item


def bag_view(request):
    items = Item.objects.all()
    return render(request, 'bag/bag.html', {'items': items})


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')
