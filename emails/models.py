from __future__ import unicode_literals

from django.db import models

class customer_service(models.Model):
    Angry = 'Angry' 
    Enquiry = 'Enquiry' 
    Holiday_Greeting = 'Holiday Greeting' 
    Marketing = 'Marketing'
    
    categories = (
                    (Angry,'Angry'),
                    (Enquiry,'Enquiry' ),
                    (Holiday_Greeting,'Holiday Greeting'),
                    (Marketing,'Marketing')
        )
    questions = models.TextField(max_length=10000, null=True, unique=True,  blank=True)
    content =  models.TextField(max_length=10000, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank= True,
        choices=categories)

    def __unicode__(self):
        return self.category


class client(models.Model):
    High = 'High (Accept)'
    Low = 'Low (Reject)'
    Accept = 'Null (Accept)'
    
    categories = (
                (High,'High (Accept)'),
                (Low,'Low (Reject)'),
                (Accept,'Null (Accept)'),
        )
    
    questions = models.TextField(max_length=10000, null=True, unique=True,  blank=True)
    content =  models.TextField(max_length=10000, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank= True,
        choices=categories)

    def __unicode__(self):
        return self.category

class friends_and_family(models.Model):
    Greetings = 'Greetings'
    Congrats = 'Congrats'
    Birthday = 'Birthday'
    Get_well = 'Get well soon'
    
    categories = (
                    (Greetings,'Greetings'),
                    (Congrats,'Congrats'),
                    (Birthday, 'Birthday'),
                    (Get_well, 'Get well soon')
        )
    
    questions = models.TextField(max_length=10000, null=True, unique=True,  blank=True)
    content =  models.TextField(max_length=10000, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank= True,
        choices=categories)

    def __unicode__(self):
        return self.category

class job_acceptance(models.Model):
    salary = 'Ask salary'
    requirements = 'Job requirements'
    
    categories = (
                    (salary,'Ask salary'),
                    (requirements,'Job requirements'),
        )
    
    questions = models.TextField(max_length=10000, null=True, unique=True,  blank=True)
    content =  models.TextField(max_length=10000, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank= True,
        choices=categories)

    def __unicode__(self):
        return self.category

class job_interview(models.Model):
    Accept = 'Accept'
    Decline = 'Decline'
    
    categories = (
                    (Accept,'Accept'),
                    (Decline,'Decline'),
        )
    questions = models.TextField(max_length=10000, null=True, unique=True,  blank=True)
    content =  models.TextField(max_length=10000, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank= True,
        choices=categories)

    def __unicode__(self):
        return self.category
