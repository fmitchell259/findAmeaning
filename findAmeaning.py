import requests
import io
from bs4 import BeautifulSoup as bs

print('')
print('Find the meaning of a word, scraped from vocabulary.com')
print('=======================================================\n')

userContinue = True
while userContinue == True:

    word = input('Please type in a word you require the meaning for.\n')
    word = word.lower()

    webPage = requests.get('https://www.vocabulary.com/dictionary/' + str(word))
    meaningSoup = bs(webPage.text,'html.parser')

    rawMeaning = meaningSoup.find(class_='short')
    if rawMeaning == None:
        print('Word not found in dictionary, please try again.\n')
        pass
    else:
        meaning = rawMeaning.get_text()
        print(str(meaning) + '\n')
        print('Would you like to find another word meaning?\n')
        cont = input('Y or N:\n')
        cont = cont.lower()
        if cont == 'y':
            pass
        elif cont == 'n':
            print('Thanks for using my program.')
            userContinue = False
        else:
            print('I think you made a typo?\n\nSo try another word anyways :)\n')
            print('---------------\n')


