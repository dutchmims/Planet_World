from django.shortcuts import render, redirect
from .forms import CheckoutForm
from .models import Order

def checkout_view(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Process the form data
            # Create an order, save it to the database, etc.
            # Redirect to the order confirmation page
            return redirect('order_confirmation')
    else:
        form = CheckoutForm()
    return render(request, 'checkout.html', {'form': form})

def order_confirmation_view(request):
    # Retrieve the latest order from the database
    latest_order = Order.objects.latest('created_at')
    return render(request, 'order_confirmation.html', {'order': latest_order})
