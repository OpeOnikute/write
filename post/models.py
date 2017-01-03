from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.
class event(models.Model):
    Past_Events = 'Past events'
    Opportunities = 'Opportunities'
    
    categories = ((Past_Events, 'Past events'),
        (Opportunities, 'Opportunities'),
        )
    
    questions = models.TextField(max_length=10000, null=True, unique=True,  blank=True)
    question_order = models.CharField(max_length=1000, null=True, blank= True)
    stories =  models.TextField(max_length=10000, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank= True,
        choices=categories)

    def __unicode__(self):
        return self.category

class news(models.Model):
    Change = 'Something changing'
    Pathetic = 'Pathetic Occurrence About To Happen '
    Gist = 'Gist'
    Good_News = 'Good News (Anticipated)'
    
    categories = (
        (Change,'Something changing'), 
        ( Pathetic,'Pathetic Occurrence About To Happen '),
        (Gist,'Gist'),
        (Good_News,'Good News (Anticipated)')
        )
    
    questions = models.TextField(max_length=10000, null=True, unique=True,  blank=True)
    question_order = models.CharField(max_length=1000, null=True, blank= True)
    stories =  models.TextField(max_length=10000, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank= True,
        choices=categories)

    def __unicode__(self):
        return self.category



class Stories(models.Model):
    author = models.CharField(max_length=100, null=True, blank= True)
    story_type = models.CharField(blank=True, null=True,
                                    max_length=100)
    category = models.CharField(blank=True, null=True,
                                    max_length=100)
    content = models.TextField(max_length=10000, null=True, blank=True)
    
    def __unicode__(self):
        return self.author 

class Email(models.Model):
    author = models.CharField(max_length=100, null=True, blank= True)
    mail_type = models.CharField(blank=True, null=True,
                                    max_length=100)
    category = models.CharField(blank=True, null=True,
                                    max_length=100)
    content = models.TextField(max_length=10000, null=True, blank=True)
    
    def __unicode__(self):
        return self.author 






    


