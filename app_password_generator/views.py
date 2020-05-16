from django.shortcuts import render
from django.http import  JsonResponse
import string
import random
import json
import nltk
from nltk.corpus import wordnet as wn

# Create your views here.

def app_password_generator(request):
    get_url = str(request.get_full_path)    
    if request.is_ajax():
        print("Requesting the url {} and type Ajax".format(get_url))
        if 'ajax_password_generator.html' in str(get_url):
            return render(request, 'password_generator.html', {'var_page_to_load':'ajax'})
        else:
            U_case = str(request.GET['U_case'])
            L_case = str(request.GET['L_case'])
            S_chars = str(request.GET['S_chars'])
            Num_value = str(request.GET['Num_value'])
            slider_range = int(request.GET['slider_range'])
            lazy_words = str(request.GET['lazy_words'])
            print("lazy word is {}".format(lazy_words))
            data = {}
            word_list = []
            lazy_word_list = []            
            uppercase = (string.ascii_uppercase)
            lowercase = (string.ascii_lowercase)
            number = (string.digits)
            symbols = (string.punctuation)       
            if U_case in "ON":
                password_format = uppercase
                if L_case in "ON":
                    password_format = password_format + lowercase
                    if S_chars in "ON":
                        password_format = password_format + symbols
                        if Num_value in "ON":
                            password_format = password_format + number
                    elif Num_value in "ON":
                        password_format = password_format + number
                elif S_chars in "ON":
                    password_format = password_format + symbols
                elif Num_value in "ON":
                    password_format = password_format + number

            elif L_case in "ON":
                password_format =  lowercase
                if S_chars in "ON":
                    password_format = password_format + symbols
                    if Num_value in "ON":
                        password_format = password_format + number
                elif  Num_value in "ON":
                    password_format = password_format + number
            elif S_chars in "ON":
                password_format = symbols
                if Num_value in "ON":
                    password_format = password_format + number
            else:
                password_format = number
                

            if password_format in number:
                password_new = random.randint(10**(slider_range-1), (10**slider_range)-1)
            else:
                password_new = "".join(random.sample(password_format, slider_range))
            if lazy_words != "":
                nltk.download('wordnet')                
                for syn in wn.synsets(lazy_words):
                    for l in syn.lemmas(): 
                        
                        word_list.append(l.name()) 
                        if l.antonyms(): 
                            word_list.append(l.antonyms()[0].name())            
                if len(word_list) >= 1:
                    random.shuffle(word_list)
                    password_new = "_"
                    for words in word_list:
                        if U_case in "ON":
                            if L_case in "ON":
                                lazy_word = ''.join(random.choice((str.upper, str.lower))(characters) for characters in words )
                            else:
                                lazy_word = ''.join((str.upper)(characters) for characters in words )
                        else:
                            lazy_word = ''.join((str.lower)(characters) for characters in words )
                        lazy_word_list.append(lazy_word)
                    print("Lazy word list is {}".format(lazy_word_list))
                    password_new = password_new.join(random.choices(lazy_word_list, k=slider_range))
                    password_new = password_new[:slider_range]
                else:
                    word_list.append(lazy_words)
                    password_new = "_"
                    for words in word_list:
                        if U_case in "ON":
                            if L_case in "ON":
                                lazy_word = ''.join(random.choice((str.upper, str.lower))(characters) for characters in words )
                            else:
                                lazy_word = ''.join((str.upper)(characters) for characters in words )
                        else:
                            lazy_word = ''.join((str.lower)(characters) for characters in words )
                        lazy_word_list.append(lazy_word)
                    print("Lazy word list is {}".format(lazy_word_list))
                    password_new = password_new.join(random.choices(lazy_word_list, k=slider_range))
                    password_new = password_new[:slider_range]            
            print("Generated password is {}".format(password_new))
            data['password'] = str(password_new)
            data['word_list'] = word_list
            result = json.dumps(data)
            result = json.loads(result)
            print("Final json is {}".format(result))
            return JsonResponse(result, safe=False)
    else:
        print("Requesting the url {} and type normal".format(get_url))
        return render(request, 'base.html', {'var_page_to_load':'password_generator'})