from .models import Product, Notification

def save_notification(message):
    date = message['fecha']
    time = message['hora']
    product = Product.objects.filter(name=message['nombre']).first()
    notificacion = Notification(date=date, time=time, product=product)
    notificacion.save()
    return notificacion

def update_product(message):
    product = Product.objects.get(name=message['nombre'])
    product.amount = message['cantidad']
    product.save()
    return product