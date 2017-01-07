# -*- coding: utf-8 -*-
from django.apps import apps                                    
from django.shortcuts import render
from django.core.urlresolvers import reverse 
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from post.get_pdf import get_pdf
from converter import get_mail
from post.models import Email
from .models import customer_service, client, friends_and_family, job_acceptance, job_interview

def clean_underscore(text):
        text = text.replace('_', ' ')
        return text

def index(request):
        for key in request.session.keys():                                                                      #clear any previous sessions, without logging the user out
                del request.session[key]
        request.session['data'] = ' '
        # this is to get the inner category actually
        models = list(apps.all_models['emails'])                                # convert the ordered dict to a list
        cleaned_models = []
        

        for model in models:
                index = models.index(model)
                model = clean_underscore(model)
                cleaned_models.append(model)
        
        combined_list = zip(models, cleaned_models)
        
        if request.method == 'POST':
                print 'email posted!'
                request.session['data'] = request.POST['category']
                print request.session['data']
                return HttpResponseRedirect(reverse('emails:select_category'))
        else:
                pass

        return render(request, 'emails/index.html', {'combined_list':combined_list})


def select_category(request):
        # this is to get the inner category actually
        data = request.session['data']                                                          #Data is gotten as a unicode object
        category = str(data)
        cleaned_category = clean_underscore(str(data))
        print 'Selected category gotten to emails:' + category
        categories_list = []
        if category == 'client':
                for cat in list(client.categories):
                        categories_list.append(cat[0])  
        elif category == 'customer_service':
                for cat in customer_service.categories:
                        categories_list.append(cat[0])                  #The categories list is a two-dimensional array, with the same values in each
        elif category == 'friends_and_family':
                for cat in friends_and_family.categories:
                        categories_list.append(cat[0])
        elif category == 'job_acceptance':
                for cat in job_acceptance.categories:
                        categories_list.append(cat[0])
        elif category == 'job_interview':
                for cat in job_interview.categories:
                        categories_list.append(cat[0])

        print 'Email category: ' + str(categories_list)                                                         # Sanity check

        if request.method == 'POST':
                request.session['inner_category'] = request.POST['inner_category']
                return HttpResponseRedirect(reverse('emails:result'))


        return render(request, 'emails/category.html', {'category':category, 'cleaned_category':cleaned_category,'categories_list':categories_list})

def result(request):
        category = str(request.session['data'])
        inner_category = str(request.session['inner_category'])
        print 'Category received is:' + inner_category

        #do the actual conversion here.
        email = get_mail(category, inner_category)

        if request.method == 'POST':
                mail_obj = Email()
                mail_obj.author ='Anon'
                mail_obj.mail_type = category.title()
                mail_obj.category =inner_category
                mail_obj.content = email
                mail_obj.save()
                get_pdf(email)
                fs = FileSystemStorage()
                filename = 'write_final.pdf'
                if fs.exists(filename):
                        with fs.open(filename) as pdf:
                            response = HttpResponse(pdf, content_type='application/pdf')
                            response['Content-Disposition'] = 'attachment; filename="write_final.pdf"'
                            return response
                else:
                        return HttpResponseNotFound('The requested pdf was not found in our server.')

            
        return render(request, 'emails/result.html', {'email':email})
