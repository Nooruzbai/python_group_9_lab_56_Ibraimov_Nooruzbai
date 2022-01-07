from django.db import models

# Create your models here.
CHOICES = [('grocery', 'Grocery'), ('cleaning_supplies', 'Cleaning Supplies'), ('stationary', 'Stationary'), ('butchers', 'Butchers')]


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Name")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Description")
    category = models.TextField(default="Other", choices=CHOICES, null=False, blank=False, verbose_name="Category")
    remainder = models.PositiveIntegerField(null=False, blank=False, verbose_name="Remainder")
    price = models.DecimalField(null=False, blank=False, max_digits=7, decimal_places=2, verbose_name="Price")

    def __str__(self):
        return f"{self.pk}. {self.name} {self.category}"

    class Meta:
        db_table = "product"
        verbose_name = "Product"
        verbose_name_plural = "Products"
