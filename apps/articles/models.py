from django.db import models


class Product(models.Model):
    nume = models.CharField('Nume', max_length=200)
    sku = models.CharField('SKU', max_length=200)
    price = models.FloatField('Pret')
    date = models.DateTimeField('Data')

    class Meta:
        verbose_name = 'Produs'
        verbose_name_plural = 'Produse'


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    producator = models.CharField('Producator', max_length=100)
    comment = models.CharField('Descriere', max_length=300)

    class Meta:
        verbose_name = 'Comentariu'
        verbose_name_plural = 'Comentarii'
