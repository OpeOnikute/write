import random
from emails.models import customer_service, client, friends_and_family, job_acceptance, job_interview

def get_mail(mail_type, type_category):
    print mail_type, type_category
    if mail_type == 'customer_service':
            type_obj = customer_service.objects.get(category=type_category)                            #Get the category of event story
    elif mail_type == 'client':
            type_obj = client.objects.get(category=type_category)
    elif mail_type == 'friends_and_family':
            type_obj = friends_and_family.objects.get(category=type_category)
    elif mail_type == 'job_acceptance':
            type_obj = job_acceptance.objects.get(category=type_category)
    elif mail_type == 'job_acceptance':
            type_obj = job_acceptance.objects.get(category=type_category)

    mail_content = type_obj.content.split('||')   #Get the stories in form a split list
    print mail_content
    mail = random.choice(mail_content)
    print mail
    return mail   #return the content of the mail
        

