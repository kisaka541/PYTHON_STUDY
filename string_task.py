#Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class 
#name = “  JOHn  .“ to “john”
#name = “  JOHn  .“ to “john”
name = "  JOHn  ."

name=name.lower()
name=name.replace('.','')
name=name.strip()
print(name)


#Slice the below string to get you the resulting sentence:
#sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”
sentence_one= "The Dod Breed is German Shepherd"
#[start_index:end_index+1]
sentence_one_sliced=sentence_one[8:23]
print(sentence_one_sliced)

#sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces”
sentence_two = "Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces"
sentence_two_sliced=sentence_two[16:30]
print(sentence_two_sliced)
#Split the below sentence using a semicolon i.e ; And display length of the result. 

#“The lazy dog; ran so fast; it hit the wall.” 
text="The lazy dog; ran so fast; it hit the wall." 
text_split=text.split(';')
print(text_split)
print(len(text_split))

#first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe

#Having the string r = '["E","W","C"]' #Manipulate it to display EWC
r='["E","W","C"]'
r=r.replace('[','')
