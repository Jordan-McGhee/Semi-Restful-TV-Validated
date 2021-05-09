from django.db import models
from datetime import datetime

# Create your models here.
class ShowManager(models.Manager):
    def validator(self, postData):
        all_shows = Show.objects.all()

        todays_date = datetime.now()
        date_format = "%Y-%m-%d"
        input_date = datetime.strptime(postData['release_date'], date_format)
        
        errors = {}

        if not postData['title']:
            errors['title'] = "Please provide a title."

        for show in all_shows:
            if postData['title'] == show.title:
                errors['title'] = "This show is already in the database."
                return errors

        if not postData['network']:
            errors['network'] = "Please provide a network."

        if not postData['release_date']:
            errors['release_date'] = "Please select when the show was released."

        if todays_date <= input_date:
            errors['release_date'] = "Please choose a date in the past."

        if len(postData['description']) < 10:
            if postData['description'] == '':
                pass
            else:
                errors['description'] = "The description must be longer than 10 characters."

        return errors

    def edit_validator(self, postData):
        all_shows = Show.objects.all()

        todays_date = datetime.now()
        date_format = "%Y-%m-%d"
        input_date = datetime.strptime(postData['release_date'], date_format)
        
        errors = {}

        if not postData['title']:
            errors['title'] = "Please provide a title."

        if not postData['network']:
            errors['network'] = "Please provide a network."

        if not postData['release_date']:
            errors['release_date'] = "Please select when the show was released."

        if todays_date <= input_date:
            errors['release_date'] = "Please choose a date in the past."

        if len(postData['description']) < 10:
            if postData['description'] == '':
                pass
            else:
                errors['description'] = "The description must be longer than 10 characters."

        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField()
    objects = ShowManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)