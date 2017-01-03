#Clean up the text entered.

def sanitize_input(text, title=False, capitalize=False,
            lower=False):                     #The function that accepts and processes inputs
    text = str(text[0])
    def pprint(text, title, capitalize, lower):      #function to punctuate and/or edit a word or sentence
        ptext = text
        if title == True:
            ptext = ptext.title()
        if capitalize == True:
            ptext = ptext.capitalize()
        if lower == True:
            ptext =  ptext.lower()
        
        return ptext 
            
    ptext = pprint(text, title, capitalize, lower)
    return ptext
