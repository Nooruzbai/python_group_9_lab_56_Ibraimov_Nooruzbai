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


