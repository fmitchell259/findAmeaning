import requests
from bs4 import BeautifulSoup as bs

print('')
print('Find the meaning of a word, scraped from dictionary.com')
print('=======================================================\n')

userContinue = True
slangFound = False

while userContinue == True:

    word = input('\nPlease type in a word you require the meaning for.\n')
    word = word.lower()

    webPage = requests.get('https://www.dictionary.com/browse/' + str(word))
    meaningSoup = bs(webPage.text,'html.parser')

    rawMeaning = meaningSoup.find(class_='one-click-content css-1e3ziqc e1q3nk1v4')

    if rawMeaning == None:
        print('Word not found in dictionary.\n')
        continueSlang = input('Shall I search urbandictionary.com for a slang term? Y/N?\n')
        cont = continueSlang.lower()
        if cont == 'y':
            slangPage = requests.get('https://www.urbandictionary.com/define.php?term=' + str(word))
            slangSoup = bs(slangPage.text,'html.parser')
            rawSlang = slangSoup.find(class_='meaning')
            if rawSlang != None:
                slangMeaning = rawSlang.get_text()
                print('----------------------------------------------------')
                print('\nFound some slang from urbandictionary.com, here what they have to say about it. :)')
                print('----------------------------------------------------\n')
                print('\n' + word + ': ' + str(slangMeaning) + '\n')
                print('Would you like to find another word meaning?\n ------------------------- ')
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
            else:
                pass
        else:
            userContinue = False
    else:
        meaning = rawMeaning.get_text()
        print('\n' + str(meaning) + '\n')
        print('Would you like to find know urbanDictionary definition, probably more meaningful?\n ------------------------- ')
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

