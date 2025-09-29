from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from .models import Order, OrderItem

@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    if not cart.items.exists():
        return redirect('view_cart')
    total = sum(item.subtotal for item in cart.items.all())
    if request.method == 'POST':
        address = request.POST.get('address')
        request.user.address = address
        request.user.save()
    return render(request, 'orders/checkout.html', {'cart': cart, 'total': total})

def process_payment(request):
    if request.method == 'POST':
        cart = Cart.objects.get(user=request.user)
        total = sum(item.subtotal for item in cart.items.all())
        order = Order.objects.create(user=request.user, total_amount=total)
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
        cart.items.all().delete()
        return redirect('orders:payment_success')  # Updated here
    return redirect('orders:checkout')

def payment_success(request):
    return render(request, 'orders/payment_success.html')

def payment_cancel(request):
    return render(request, 'orders/payment_cancel.html')