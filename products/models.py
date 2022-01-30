from django.db import models
from django.utils.safestring import mark_safe


class ProductsCategory(models.Model):
    name = models.CharField(verbose_name='kategoriyasi', max_length=50)
    class Meta:
        ordering = ('-name',)
        verbose_name = 'kategoriyasi'
        verbose_name_plural = 'kategoriyalari'
    def __str__(self):
        return self.name

class Products(models.Model):
    category = models.ManyToManyField(ProductsCategory,  verbose_name='mahsulot turi')
    name = models.CharField(verbose_name='kitob nomi', max_length=50)
    author = models.CharField(verbose_name='muallifi', max_length=50)
    made_by = models.CharField(verbose_name='nashriyot', max_length=50)
    description = models.TextField(verbose_name='haqida')
    image = models.ImageField(verbose_name='foto', upload_to='uploads/%Y/%m/%d/')
    price = models.DecimalField(verbose_name='narxi', max_digits=10, decimal_places=2)
    rating_choices = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5")
    )
    rating = models.IntegerField(default=0, choices=rating_choices, verbose_name='reytingi')
    status = models.CharField(max_length=100, verbose_name='statusi')
    class Meta:
        ordering = ('name',)
        verbose_name = 'kitob'
        verbose_name_plural = 'kitoblar'
    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True