# from django.db import models

# class Quote(models.Model):
#     """
#     The scrapped data will be saved in this model
#     """
#     text = models.TextField()
#     author = models.CharField(max_length=512)



import json
from django.db import models
from django.utils import timezone


class Events(models.Model):

    url = models.TextField()
    hashed_data = models.TextField()
    status = models.CharField(max_length=50,null=True)
    date = models.DateTimeField(default=timezone.now)



class Quote(models.Model):
    """
    The scrapped data will be saved in this model
    """
    text = models.TextField()
    author = models.CharField(max_length=512)




class ScrapyItem(models.Model):
    unique_id = models.CharField(max_length=100, null=True)
    data = models.TextField() # this stands for our crawled data
    date = models.DateTimeField(default=timezone.now)
    
    # This is for basic and custom serialisation to return it to client as a JSON.
    @property
    def to_dict(self):
        data = {
            'data': json.loads(self.data),
            'date': self.date
        }
        return data

    def __str__(self):
        return self.unique_id