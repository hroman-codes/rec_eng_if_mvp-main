#TODO uncomment model once business logic grows 
# from django.db import models
# from apps.seeker.models import Seeker

#TODO need to add creation date to model 
# class RecommendationEngine(models.Model):
#     seeker = models.ForeignKey(Seeker, on_delete=models.CASCADE)
#     hiring_manager = models.BooleanField()
#     contacted = models.BooleanField()
#     scheduled = models.BooleanField()
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     title = models.CharField(max_length=255)
#     company = models.CharField(max_length=255)
#     position = models.CharField(max_length=255, default='', blank=True)
#     linkedin_url = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     ask = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
    
    
#     def __str__(self) -> str:
#         return f'RecommendationEnding ID: {self.ID}'
    