from django.db import models

# Create your models here.
CHOICES = [('other', 'Other'), ('grocery', 'Grocery'), ('cleaning_supplies', 'Cleaning Supplies'), ('stationary', 'Stationary'), ('butchers', 'Butchers')]


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Name")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Description")
    category = models.TextField(default=CHOICES[0], choices=CHOICES, null=False, blank=False, verbose_name="Category")
    remainder = models.PositiveIntegerField(null=False, blank=False, verbose_name="Remainder")
    price = models.DecimalField(null=False, blank=False, max_digits=7, decimal_places=2, verbose_name="Price")

    def __str__(self):
        return f"{self.pk}. {self.name} {self.category}"

    class Meta:
        db_table = "product"
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductInBag(models.Model):
    amount = models.PositiveIntegerField(null=False, blank=False,  verbose_name='Amount')
    product = models.ForeignKey('productshop.Product',
                                on_delete=models.CASCADE,
                                related_name="products_in_bag",
                                verbose_name="Product in Bag",)

    class Meta:
        db_table = 'product_in_bag'
        verbose_name = 'Product in Bag'
        verbose_name_plural = 'Products in Bag'

    @property
    def get_total_for_product(self):
        total = self.amount * self.product.price
        return total


class Order(models.Model):
    username = models.CharField(max_length=200, null=False, blank=False, verbose_name='Username'),
    phone_number = models.CharField(max_length=200, null=False, blank=False, verbose_name='Phone number')
    address = models.CharField(max_length=200, null=False, blank=False, verbose_name='Address'),
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created"),

    def __str__(self):
        return f"{self.pk}. {self.username} {self.phone_number}  {self.date_created}"

    class Meta:
        db_table = "order"
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class ProductOrder(models.Model):
    product=models.ForeignKey('productshop.Product', on_delete=models.CASCADE, related_name='product_orders', verbose_name='Product')
    order=models.ForeignKey('productshop.Order', on_delete=models.CASCADE, related_name='product_orders', verbose_name='Orders')
    amount=models.PositiveIntegerField(verbose_name="Amount")

    def __str__(self):
        return f"{self.pk}. {self.product} {self.order}  {self.amount}"

    class Meta:
        db_table = "product_order"
        verbose_name = "Product Order"
        verbose_name_plural = "Product Orders"

