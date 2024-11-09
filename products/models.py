from django.db import models
import uuid

# Create your models here.

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    ceated_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Product(BaseModel):
    product_name = models.CharField(max_length=50)
    product_slug = models.SlugField(unique=True)
    product_description = models.TextField()
    product_price = models.IntegerField(default=True)
    product_demoprice = models.IntegerField(default=True)
    quentity = models.CharField(max_length=100, null=True, blank=True)

class ProductMetaInformation(BaseModel):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="product_meta_information")
    product_quentity = models.CharField(max_length=100)
    quentity_unit = models.CharField(max_length=100, choices=[("kg", "kg"), ("l", "l"), ("g", "g"), ("ml", "ml"), (None, None)])
    is_restrict = models.BooleanField(default=False)
    restrict_quentity = models.IntegerField()

class ProductImages(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    product_images = models.ImageField(upload_to="product_media")
    