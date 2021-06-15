from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from .models import Category,CategoryFood,Food,FoodImage

class FoodlistView(View):
    def get(self, request):
        category_id = request.GET.get('categoryId')
        sort        = request.GET.get('sort','id')

        q = Q()

        if category_id:
            q = Q(categories__id=category_id)

        foods = Food.objects.filter(q).order_by(sort)
        
        result = []
        for food in foods:
            
            food_info = {
                'id'               : food.id,
                'img_url'          : food.foodimage_set.first().image_url,
                'name'             : food.name,
                'price'            : food.price,
                'discount'         : food.discount,
                'discounted_price' : food.discounted_price,
                'star_score'       : food.star_score,
                'review_count'     : food.review_count,
                'create_at'        : food.create_at
            }
            result.append(food_info)

        return JsonResponse({'result' : result}, status=200)