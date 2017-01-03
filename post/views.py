import converter
from get_pdf import get_pdf
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.core.urlresolvers import reverse 
from .models import event, news, Stories
# Create your views here.

def about(request):
	return render(request, 'about.html')

def index(request):
	for key in request.session.keys():									#clear any previous sessions, without logging the user out
		del request.session[key]
	category = ''
	
	if request.method == 'POST':
		print 'posted!'
		request.session['data'] = request.POST['story_category']
		print request.session['data']
                return HttpResponseRedirect(reverse('post:category'))
        else:
                pass

	return render(request, 'post/index.html')

def category(request):
	data = request.session['data']								#Data is gotten as a unicode object
	category = str(data)
	print 'Selected category gotten to converter: ' + category
	categories_list = []
	if category == 'event':
		for cat in list(event.categories):
			categories_list.append(cat[0])				#The categories list is a two-dimensional array, with the same values in each
	elif category == 'news':
		for cat in news.categories:
			categories_list.append(cat[0])
	elif category == 'emails':
		return HttpResponseRedirect(reverse('emails:index'))
	print categories_list								# Sanity check

	if request.method == 'POST':
		request.session['category'] = request.POST['category']
		return HttpResponseRedirect(reverse('post:convert'))


	return render(request, 'post/category.html', {'category':category, 'categories_list':categories_list})

def convert(request):
	category = str(request.session['data'])
	inner_category = str(request.session['category'])
	print 'Selected inner category gotten to converter:' + inner_category
	
	if category == 'event':
		story_object = event.objects.get(category=inner_category)
	elif category == 'news':
		story_object = news.objects.get(category=inner_category)
	else:
		return HttpResponseRedirect(reverse('post:error'))

	questions = story_object.questions.split(' | ')
	order = story_object.question_order.split(',')
	combined_list = zip(questions, order)

	if request.method == 'POST':
		print request.POST
		request.session['Final Data'] = dict(request.POST)
		print request.session['Final Data']
		return HttpResponseRedirect(reverse('post:result'))
		

	return render(request, 'post/converter.html', {'combined_list':combined_list})

def result(request):
	category = str(request.session['data'])
	inner_category = str(request.session['category'])
	final_data = request.session['Final Data']	
	story = ''

	#do the actual conversion here.
	if category == 'event':
		if inner_category == 'Opportunities':
			story = converter.e_opportunity(final_data)
		elif inner_category == 'Past events':
			story = converter.e_past(final_data)
	elif category == 'news':
		if inner_category == 'Something changing':
			story = converter.n_change(final_data)
		elif inner_category == 'Pathetic Occurrence About To Happen ':
			story = converter.n_pathetic(final_data)
		elif inner_category == 'Gist':
			story = converter.n_gist(final_data)
		elif inner_category == 'Good News (Anticipated)':
			story = converter.n_good(final_data)
	else:
		return HttpResponseRedirect(reverse('post:error'))


	if request.method == 'POST':
		get_pdf(story)
		fs = FileSystemStorage()
                filename = 'write_final.pdf'
                if fs.exists(filename):
                        with fs.open(filename) as pdf:
                            response = HttpResponse(pdf, content_type='application/pdf')
                            response['Content-Disposition'] = 'attachment; filename="write_final.pdf"'
                            return response
                else:
                        return HttpResponseNotFound('The requested pdf was not found in our server.')
		# story_obj = Stories()
		# story_obj.author ='Anon'
  #               story_obj.story_type = category.title()
  #               story_obj.category =inner_category
  #               story_obj.content = story
  #               story_obj.save()
    
	
	return render(request, 'post/result.html', {'story':story})

def error(request):
	return render(request, '404.html')
