from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CheckoutForm
from .models import Order

def checkout_view(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            return redirect('order_confirmation')
        else:
            return render(request, 'checkout.html', {'form': form})
    else:
        form = CheckoutForm()
    return render(request, 'checkout.html', {'form': form})

def order_confirmation_view(request):
    latest_order = Order.objects.latest('created_at')
    return render(request, 'order_confirmation.html', {'order': latest_order})
