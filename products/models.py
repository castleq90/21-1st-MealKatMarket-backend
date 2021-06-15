from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'categories'

class Food(models.Model):
    name             = models.CharField(max_length=50, unique=True)
    price            = models.DecimalField(max_digits=10, decimal_places=2)
    discount         = models.PositiveIntegerField(default=0)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    star_score       = models.DecimalField(max_digits=2, decimal_places=1)
    review_count     = models.PositiveIntegerField()
    detail_image     = models.URLField()
    create_at        = models.DateTimeField()
    update_at        = models.DateTimeField()
    categories       = models.ManyToManyField(Category, through='Categoryfood')

    class Meta:
        db_table = 'foods'

class CategoryFood(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    food     = models.ForeignKey(Food, on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories_foods'

class FoodImage(models.Model):
    food      = models.ForeignKey(Food, on_delete=models.CASCADE) 
    image_url = models.URLField()

    class Meta:
        db_table = 'food_images'

class RequiredOption(models.Model):
    food     = models.ForeignKey(Food, on_delete=models.CASCADE)
    name     = models.CharField(max_length=30, unique=True)
    price    = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    class Meta:
        db_table = 'required_options'

class SelectOption(models.Model):
    food     = models.ForeignKey(Food, on_delete=models.CASCADE)
    name     = models.CharField(max_length=30, unique=True)
    price    = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    class Meta:
        db_table = 'select_options'