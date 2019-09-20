from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import sqlite3
site = "http://www.nehumanesociety.org/adopt/dogs/"

uClient = uReq(site)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

pup_tml = page_soup.findAll\
    ("div", {'class': 'pet-box col-xs-12 col-sm-6 col-md-6'})

conn = sqlite3.connect('dog.db')

cursr = conn.cursor()

cursr.execute("""CREATE TABLE dogs (
                name text,
                id blob,
                breed text,
                age blob,
                sex text,
                color text,
                weight blob,
                exercise text,
                training text,
                fee integer,
                friendliness text,
                playfulness text,
                dog_friendliness text,
                manners text
                )""")

conn.commit()

dog_count = 0

dogs_dict = {}

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
        dog_weight = "Data Unavailable at this time"

    try:
        dog_name = str(dog_group[0].partition("Name: ")[-1])
    except IndexError:
        dog_name = "Data Unavailable at this time"

    try:
        dog_breed = str(breed_group[0].partition("Breed: ")[-1])
    except IndexError:
        dog_breed = "Data Unavailable at this time"

    try:
        dog_age = str(age_group[0].partition("Age: ")[-1])
    except IndexError:
        dog_age = "Data Unavailable at this time"

    try:
        dog_color = str(color_group[0].partition("Color: ")[-1])
    except IndexError:
        dog_color = "Data Unavailable at this time"

    try:
        dog_sex = str(sex_group[0].partition("Sex: ")[-1])
    except IndexError:
        dog_sex = "Data Unavailable at this time"
    try:
        dog_fee = str(fee_group[0].partition("Fee: ")[-1])
    except IndexError:
        dog_fee = "Data Unavailable at this time"

    try:
        dog_exercise_needs = \
            str(exercise_group[0].partition("Exercise Needs: ")[-1])
    except IndexError:
        dog_exercise_needs = "Data Unavailable at this time"

    try:
        dog_training = \
            str(training_group[0].partition("Ease of Training: ")[-1])
    except IndexError:
        dog_training = "Data Unavailable at this time"
    try:
        dog_friendliness = \
            str(friendliness_group[0].partition("Friendliness: ")[-1])
    except IndexError:
        dog_friendliness = "Data Unavailable at this time"
    try:
        dog_playfulness = \
            str(playfulness_group[0].partition("Playfulness: ")[-1])
    except IndexError:
        dog_playfulness = "Data Unavailable at this time"
    try:
        dog_skills = \
            str(skills_group[0].partition("Dog Skills: ")[-1])
    except IndexError:
        dog_skills = "Data Unavailable at this time"

    try:
        dog_leash_manners = plain_text.partition("Leash Manners: ")[-1]
    except IndexError:
        dog_leash_manners = "Data Unavailable at this time"

    dogs_dict[dog_count] = \
        {'name': dog_name, 'id': dog_id, 'breed': dog_breed, 'age': dog_age,
         'sex': dog_sex, 'color': dog_color, 'weight': dog_weight,
         'exercise': dog_exercise_needs, 'training': dog_training,
         'fee': dog_fee, 'friendliness': dog_friendliness,
         'playfulness': dog_playfulness, 'dog_friendliness': dog_skills,
         'manners': dog_leash_manners}
    dog_count += 1

for dog in dogs_dict:
    cursr.execute\
        ("INSERT INTO dogs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
         [dogs_dict[dog]['name'], dogs_dict[dog]['id'],
         dogs_dict[dog]['breed'], dogs_dict[dog]['age'],
         dogs_dict[dog]['sex'], dogs_dict[dog]['color'],
         dogs_dict[dog]['weight'], dogs_dict[dog]['exercise'],
         dogs_dict[dog]['training'], dogs_dict[dog]['fee'],
         dogs_dict[dog]['friendliness'], dogs_dict[dog]['playfulness'],
         dogs_dict[dog]['dog_friendliness'], dogs_dict[dog]['manners']])
    conn.commit()

cursr.execute("SELECT * FROM dogs WHERE sex='Neutered Male'")
conn.commit()
print(cursr.fetchall())
conn.close()
