greek = {'eya': 'hello', 'kalimera': 'good morning',
         'kalispera': 'good evening', 'kalinixta': 'good night'}
for greek_word, meaning in greek.items():
    print(f"{greek_word} means {meaning}")

# for greek_word in greek:
#     print(f"{greek_word} means {greek[greek_word]}")

# Exercise to create a dict of rivers and their countries
rivers = {'Amazon': 'Brazil',
          'Nile': 'Egypt',
          'Yangtze': 'China', }

for river, country in rivers.items():
    print(f"The river {river} runs through {country}")

# Exercise to create a dict of favorite languages
favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python', }
peopeles = ['jen', 'sarah', 'nebiyu', 'phil', 'john']

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

for name in peopeles:
    if name in favorite_languages.keys():
        print(f"{name.title()}, thank you for taking the poll.")
    else:
        print(f"{name.title()}, please take the poll.")
