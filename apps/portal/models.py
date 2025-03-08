from django.db import models

class Services(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True, unique=True)
    title = models.CharField(max_length=50, blank=False, null=False, unique=True)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='services', blank=True, null=True)
    icon = models.ImageField(upload_to='services/icons', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        
    def __str__(self):
        return self.title


class ServiceItem(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True, unique=True)
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name="items")
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    hero_image = models.ImageField(upload_to='service/item/hero', blank=True, null=True)
    lead_image_1 = models.ImageField(upload_to='service/item/lead', blank=True, null=True)
    lead_image_2 = models.ImageField(upload_to='service/item/lead', blank=True, null=True)
    banner_image = models.ImageField(upload_to='service/item/banner', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Service Item'
        verbose_name_plural = 'Service Items'
        
    def __str__(self):
        return self.title


class ServiceItemCategory(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True, unique=True)
    service_item = models.ForeignKey(ServiceItem, on_delete=models.CASCADE, related_name="categories")
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='service/item/category', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Service Item Category'
        verbose_name_plural = 'Service Item Categories'
        
    def __str__(self):
        return self.title


class ServiceItemOption(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True, unique=True)
    service_item_category = models.ForeignKey(ServiceItemCategory, on_delete=models.CASCADE, related_name="options")
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='service/item/option', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Service Item Option'
        verbose_name_plural = 'Service Item Options'
        
    def __str__(self):
        return self.title


class ServiceItemOptionDescription(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True, unique=True)
    service_item_option = models.ForeignKey(ServiceItemOption, on_delete=models.CASCADE, related_name="descriptions")
    language = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Service Item Option Description'
        verbose_name_plural = 'Service Item Option Descriptions'
        
    def __str__(self):
        return f"{self.service_item_option.title} - {self.language}"


class ServiceItemOptionDescriptionValues(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True, unique=True)
    service_item_option_description = models.ForeignKey(ServiceItemOptionDescription, on_delete=models.CASCADE, related_name="description_values")
    key = models.CharField(max_length=50)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Service Item Option Description Value'
        verbose_name_plural = 'Service Item Option Description Values'
        
    def __str__(self):
        return f"{self.key}: {self.value[:30]}"
