from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug_value = base_slug
            i = 1
            while Phone.objects.filter(slug=slug_value).exists():
                slug_value = f"{base_slug}-{i}"
                i += 1
            self.slug = slug_value
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name