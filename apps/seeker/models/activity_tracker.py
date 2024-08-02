# from django.db import models
# from apps.seeker.models import Seeker
# from django.utils import timezone

#TODO uncomment model once business logic grows from activity tracker  
# class ActivityTracker(models.Model):
#     seeker = models.ForeignKey(Seeker, on_delete=models.CASCADE)
#     hiring_manager = models.BooleanField(default=False)
#     name = models.CharField(max_length=255)
#     title = models.CharField(max_length=255)
#     company = models.CharField(max_length=255)
#     position = models.CharField(max_length=255)
    # linkedin_url = models.CharField(max_length=255)
    # met_on = models.DateTimeField(default=timezone.now)
    
    # def __str__(self) -> str:
    #     return f'ActivityTracker ID: {self.id}'
    