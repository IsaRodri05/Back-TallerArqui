from .models import Product, Changes

def save_changes(message):
    date = message['fecha']
    time = message['hora']
    product = Product.objects.filter(name=message['nombre']).first()
    amount = message['cantidad']
    change = Changes(date=date, time=time, product=product, amount=amount)
    change.save()
    return change

def update_create_product(message):
    product, created = Product.objects.get_or_create(name=message['nombre'], defaults={'amount': message['cantidad']})
    if not created:
        product.amount = message['cantidad']
        product.save()
    return product

def last_changes():
    changes = Changes.objects.order_by('-date', '-time')[:10]
    data = []
    for change in changes:
        data.append({
            'date': change.date,
            'time': change.time,
            'product': change.product.name,
            'amount': change.amount
        })
    return data