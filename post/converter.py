import random
from post.models import event, news
from sanitize import sanitize_input

def get_story(type, type_category):
        if type == 'events':
                type_obj = event.objects.get(category=type_category)                            #Get the category of event story
        elif type == 'news':
                type_obj = news.objects.get(category=type_category)

        stories = type_obj.stories.split('||')   #Get the stories in form a split list
        story_type = random.choice(stories)
        return (story_type, stories.index(story_type))    #return the story_type from database and its index
        
def e_past(data):
        print data
        from datetime import datetime
        past_obj = event.objects.get(category='Past events')
        
        #function to calculate the number of days past since an event 
        def get_days_past(event_date):
                date_format = "%Y-%m-%d"
                today = datetime.today().strftime(date_format)
                event_day = datetime.strptime(event_date, date_format)
                today_time = datetime.strptime(today, date_format)
                delta = today_time - event_day
                days_passed = str(delta).split(',')[0]          #Remove the part that shows the number of seconds, dont need that
                return days_passed

        #populate the data temporarily for testing and what-not.
        # data = {'event_date':r'12/12/2016', 
        #                 'event_name':'FELABRATION', 
        #                 'event_purpose':'to make money', 
        #                 'event_organizer':'Opeyemi Onikute', 
        #                 'event_location':'Gbagada, Lagos', 
        #                 'event_elaboration':'We also learned how to make money',
        #                 'event_opportunities':'Go and buy food',
        #                 'people_attended':'Opeyemi, Tunji and others'
        #                 }

        event_date = sanitize_input(data['event_date'])                         #Remember that the data values are inputted as strings.
        event_name = sanitize_input(data['event_name'],  title = True)
        event_purpose = sanitize_input(data['event_purpose'], lower = True)
        event_organizer = sanitize_input(data['event_organizer'],  title=True)
        event_location = sanitize_input(data['event_location'], title=True)
        event_elaboration = sanitize_input(data['event_elaboration'], lower=True)
        event_opportunities = sanitize_input(data['event_opportunities'], capitalize=True)
        people_attended = sanitize_input(data['people_attended'],  title=True)
        days_passed = get_days_past(event_date)

        story_to_use = get_story('events','Past events') 
        if story_to_use[1] == 0:       #use the index to identify the order
                story = story_to_use[0] % (days_passed, event_name, event_purpose, event_location, people_attended, event_organizer, event_elaboration, event_opportunities)
        else:
                story = 'Error. Please try again.'

        return story 

def e_opportunity(data):
        past_obj = event.objects.get(category='Opportunities')                  #initialize an opportunity object
                
        # data = {'event_date':r'12/12/2016', 
        #                 'event_name':'FELABRATION', 
        #                 'event_purpose':'to make money', 
        #                 'event_organizer':'Opeyemi Onikute', 
        #                 'event_location':'Gbagada, Lagos', 
        #                 'event_elaboration':'We also learned how to make money',
        #                 'event_opportunities':'Go and buy food',
        #                 'people_attended':'Opeyemi, Tunji and others',
        #                 'how_to_apply':'hug a transformer',
        #                 'event_type':'meetup',
        #                 'duration': '5 hours',
        #                 'participants_will':'eat rice',
        #                 'deadline': 'tomorrow',
        #                 'partners':'Arik and co.',
        #                 'conditions':'Know how to cook',
        #                 'time':'9 a.m',
        #         }

        event_name = sanitize_input(data['event_name'],  title = True)
        purpose =  sanitize_input(data['event_purpose'], lower=True)
        location = sanitize_input(data['event_location'] , title = True)
        conditions = sanitize_input(data['conditions'], lower=True) 
        how_to_apply = sanitize_input(data['how_to_apply'], capitalize=True)
        event_type = sanitize_input(data['event_type'], lower=True)
        person = sanitize_input(data['event_organizer'],  title = True) #make sure the company is started with uppercase
        event_date = sanitize_input(data['event_date'], capitalize = True)
        duration = sanitize_input(data['duration'], lower=True)
        time = sanitize_input(data['time'], lower=True)
        participants_will = sanitize_input(data['participants_will'], lower=True)
        deadline = sanitize_input(data['deadline'], lower=True)
        partners = sanitize_input(data['partners'], title = True).title()
        story_to_use = get_story('events','Opportunities') 

        if story_to_use[1] == 0: 
                story = story_to_use[0] % (person, partners, event_type, event_name, event_date, purpose, location,
          	time, duration, participants_will, how_to_apply, conditions)

        elif story_to_use[1] == 1:
            story = story_to_use[0] % (person, partners, event_type, event_name, event_date, purpose, location, 
                time, duration, participants_will, how_to_apply, conditions, deadline)

        return story


def n_change(data):
        past_obj = news.objects.get(category='Something changing')                 

        event_date = sanitize_input(data['event_date'])
        company_name = sanitize_input(data['company_name'],  title = True)
        company_info = sanitize_input(data['company_info'],  title = True)
        before_info = sanitize_input(data['before_info'],  title = True)
        implications = sanitize_input(data['implications'],  title = True)
        people_affected = sanitize_input(data['people_affected'],  lower = True)

        story_to_use = get_story('news','Something changing') 

        if story_to_use[1] == 0: 
                story = story_to_use[0] % (event_date,company_name,company_info,before_info,implications,people_affected)

        return story


def n_pathetic(data):
        past_obj = news.objects.get(category='Pathetic Occurrence About To Happen ')                 
        
        actual_news = sanitize_input(data['actual_news'], title=True)
        person= sanitize_input(data['person'], title=True)
        pathetic_reason = sanitize_input(data['pathetic_reason'], lower=True)
        platform = sanitize_input(data['platform'])

        story_to_use = get_story('news','Pathetic Occurrence About To Happen ') 

        if story_to_use[1] == 0:
                story = story_to_use[0] % (actual_news,person,platform, pathetic_reason,platform)

        return story


def n_gist(data):
        past_obj = news.objects.get(category='Gist')                 
        
        happening = sanitize_input(data['happening'], title=True)
        person = sanitize_input(data['person'], title=True)
        reason = sanitize_input(data['reason'], title=True)
        consequences = sanitize_input(data['consequences'], title=True)
        action = sanitize_input(data['action'], title=True)

        story_to_use = get_story('news','Gist') 

        if story_to_use[1] == 0: 
                story = story_to_use[0] % (happening, person, reason, consequences, action)

        return story

def n_good(data):
        past_obj = news.objects.get(category='Good News (Anticipated)')  

        information = sanitize_input(data['information'], title=True)
        further_info = sanitize_input(data['further_info'], title=True) 
        gain = sanitize_input(data['gain'], title=True)


        story_to_use = get_story('news','Good News (Anticipated)') 

        if story_to_use[1] == 0: 
                story = story_to_use[0] % (information,further_info,gain)

        return story
