from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
site = "http://www.nehumanesociety.org/adopt/dogs/"

uClient = uReq(site)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

pup_tml = page_soup.findAll("div", {'class':'pet-box col-xs-12 col-sm-6 col-md-6'})

# first = pup_tml[0]
#
# attributes = first.findAll("span", {'class': 'js__pet-description'})
#
# plain_text = attributes[0].text
#
# #Patterns to get specific attributes
#
# name_pattern = re.compile(r'.+?(?=Bre)')
#
# breed_pattern = re.compile(r'.+?(?=Age)')
#
# age_pattern = re.compile(r'.+?(?=Color)')
#
# color_pattern = re.compile(r'.+(?=Sex)')
#
# sex_pattern = re.compile(r'.+(?=Weight)')
#
# weight_pattern = re.compile(r'.+(?=First)')
#
# fee_pattern = re.compile(r'.+(?=Exer)')
#
# exercise_pattern = re.compile(r'.+(?=Ease)')
#
# training_pattern = re.compile(r'.+(?=Friendliness)')
#
# friendliness_pattern = re.compile(r'.+(?=Playfulness)')
#
# playfulness_pattern = re.compile(r'.+(?=Dog)')
#
# skills_pattern = re.compile(r'.+(?=Leash)')
#
#
# #Match for specifics
# skills_group = skills_pattern.findall(plain_text)
#
# playfulness_group = playfulness_pattern.findall(plain_text)
#
# friendliness_group = friendliness_pattern.findall(plain_text)
#
# exercise_group = exercise_pattern.findall(plain_text)
#
# fee_group = fee_pattern.findall(plain_text)
#
# weight_group = weight_pattern.findall(plain_text)
#
# color_group = color_pattern.findall(plain_text)
#
# age_group = age_pattern.findall(plain_text)
#
# breed_group = breed_pattern.findall(plain_text)
#
# dog_group = name_pattern.findall(plain_text)
#
# sex_group = sex_pattern.findall(plain_text)
#
# training_group = training_pattern.findall(plain_text)
#
#
# #Get final attribute values
# dog_weight = str(weight_group[0].partition("Weight: ")[-1])
#
# dog_name = str(dog_group[0].partition("Name: ")[-1])
#
# dog_breed = str(breed_group[0].partition("Breed: ")[-1])
#
# dog_age = str(age_group[0].partition("Age: ")[-1])
#
# dog_color = str(color_group[0].partition("Color: ")[-1])
#
# dog_sex = str(sex_group[0].partition("Sex: ")[-1])
#
# dog_fee = str(fee_group[0].partition("Fee: ")[-1])
#
# dog_exercise_needs = str(exercise_group[0].partition("Exercise Needs: ")[-1])
#
# dog_training = str(training_group[0].partition("Ease of Training: ")[-1])
#
# dog_friendliness = str(friendliness_group[0].partition("Friendliness: ")[-1])
#
# dog_playfulness = str(playfulness_group[0].partition("Playfulness: ")[-1])
#
# dog_skills = str(skills_group[0].partition("Dog Skills: ")[-1])
#
# dog_leash_manners = plain_text.partition("Leash Manners: ")[-1]
#
filename = 'dogs.csv'

f = open(filename, "w")

headers = "dog_name, dog_id, breed, age, sex, color, weight, exercise_needs, training, fee, friendliness, playfulness, skills, leash_manners"

f.write(headers + "\n")

for i in pup_tml:
    attributes = i.findAll("span", {'class': 'js__pet-description'})

    plain_text = attributes[0].text

    name_pattern = re.compile(r'.+?(?=Bre)')

    breed_pattern = re.compile(r'.+?(?=Age)')

    age_pattern = re.compile(r'.+?(?=Color)')

    color_pattern = re.compile(r'.+(?=Sex)')

    sex_pattern = re.compile(r'.+(?=Weight)')

    weight_pattern = re.compile(r'.+(?=First)')

    fee_pattern = re.compile(r'.+(?=Exer)')

    exercise_pattern = re.compile(r'.+(?=Ease)')

    training_pattern = re.compile(r'.+(?=Friendliness)')

    friendliness_pattern = re.compile(r'.+(?=Playfulness)')

    playfulness_pattern = re.compile(r'.+(?=Dog)')

    skills_pattern = re.compile(r'.+(?=Leash)')

    skills_group = skills_pattern.findall(plain_text)

    playfulness_group = playfulness_pattern.findall(plain_text)

    friendliness_group = friendliness_pattern.findall(plain_text)

    exercise_group = exercise_pattern.findall(plain_text)

    fee_group = fee_pattern.findall(plain_text)

    weight_group = weight_pattern.findall(plain_text)

    color_group = color_pattern.findall(plain_text)

    age_group = age_pattern.findall(plain_text)

    breed_group = breed_pattern.findall(plain_text)

    dog_group = name_pattern.findall(plain_text)

    sex_group = sex_pattern.findall(plain_text)

    training_group = training_pattern.findall(plain_text)

    dog_id = i.div.div.span.text
    try:
        dog_weight = str(weight_group[0].partition("Weight: ")[-1])
    except IndexError:
        print("Data Unavailable at this time")

    try:
        dog_name = str(dog_group[0].partition("Name: ")[-1])
    except IndexError:
        print("Data Unavailable at this time")

    try:
        dog_breed = str(breed_group[0].partition("Breed: ")[-1])
    except IndexError:
        print("Data Unavailable at this time")

    try:
        dog_age = str(age_group[0].partition("Age: ")[-1])
    except IndexError:
        print("Data Unavailable at this time")

    try:
        dog_color = str(color_group[0].partition("Color: ")[-1])
    except IndexError:
        print("Data Unavailable at this time")

    try:
        dog_sex = str(sex_group[0].partition("Sex: ")[-1])
    except IndexError:
        print("Data Unavailable at this time")
    try:
        dog_fee = str(fee_group[0].partition("Fee: ")[-1])
    except IndexError:
        print("Data Unavailable at this time")

    try:
        dog_exercise_needs = str(exercise_group[0].partition("Exercise Needs: ")[-1])
    except IndexError:
        print("Data Unavailable at this time")

    try:
        dog_training = str(training_group[0].partition("Ease of Training: ")[-1])
    except IndexError:
        print("Data Unavailable at this time")
    try:
        dog_friendliness = str(friendliness_group[0].partition("Friendliness: ")[-1])
    except IndexError:
        print("Data Unavailable at this time")
    try:
        dog_playfulness = str(playfulness_group[0].partition("Playfulness: ")[-1])
    except IndexError:
        print("Data Unavailable at this time")
    try:
        dog_skills = str(skills_group[0].partition("Dog Skills: ")[-1])
    except IndexError:
        print("Data Unavailable at this time")

    dog_leash_manners = plain_text.partition("Leash Manners: ")[-1]

    print(dog_name, dog_id, dog_breed, dog_age, dog_sex, dog_color, dog_weight, dog_exercise_needs, dog_training, dog_fee, dog_friendliness, dog_playfulness, dog_skills, dog_leash_manners)

    f.write(dog_name + ',' + dog_id + ',' + dog_breed + ',' + dog_age + ',' + dog_sex + ','+ dog_color + ',' + dog_weight + ',' + dog_exercise_needs + ',' + dog_training + ',' + dog_fee + ',' + dog_friendliness + ',' + dog_playfulness + ',' + dog_skills + ',' + dog_leash_manners + "\n")

f.close()


