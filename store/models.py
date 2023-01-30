from django.db import models

# Create your models here.


class Collection(models.Model):
    title = models.CharField(max_length=120)
    featured_product = models.ForeignKey('Product',on_delete=models.SET_NULL,null=True,related_name='+')


class Promotions(models.Model):
    description = models.TextField(blank=True, null=True)
    discount = models.FloatField()
    #start_date = models.DateTimeField(auto_now=True)
    #end_date = models.DateTimeField(auto_now=True)


class Product(models.Model):
    title = models.CharField(max_length=120)
    slug=models.SlugField()
    description = models.TextField(blank=True, null=True)
    unit_price = models.DecimalField(decimal_places=2, max_digits=6)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(
        Promotions)


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICE = [(MEMBERSHIP_BRONZE, 'Bronze'),
                         (MEMBERSHIP_SILVER, 'Silver'), (MEMBERSHIP_GOLD, 'Gold')]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICE, default=MEMBERSHIP_BRONZE)


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICE = [(PAYMENT_STATUS_PENDING, 'Pending'),
                             (PAYMENT_STATUS_COMPLETE, 'Completed'), (PAYMENT_STATUS_FAILED, 'Failed')]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICE, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    # one to one relationship
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, primary_key=True)
    # one to many relationship
    # customer=models.ForeignKey(Customer,on_delete=models.CASCADE)


class OrderItem(models.Model):
    quantity = models.PositiveSmallIntegerField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
