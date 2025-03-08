from django.db import models

class CatalogSection(models.Model):
    """Model to define the overall catalog section."""
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class CatalogItem(models.Model):
    """Model to represent each item in the catalog."""
    section = models.ForeignKey(CatalogSection, related_name="items", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to='catalog/icons/', blank=True, null=True)

    def __str__(self):
        return self.title
