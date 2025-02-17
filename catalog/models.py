from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="наименование продукта")
    description = models.TextField(verbose_name="описание продукта", blank=True, null=True)
    photo = models.ImageField(upload_to="product/photo", verbose_name="Фото продукта", blank=True, null=True)
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="категория",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.IntegerField(verbose_name="цена за покупку")
    created_at = models.DateField(verbose_name="дата создания", blank=True, null=True)
    updated_at = models.DateField(verbose_name="дата последнего изменения", blank=True, null=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ['category', 'name']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="наименование категории")
    description = models.TextField(verbose_name="описание категории", blank=True, null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
