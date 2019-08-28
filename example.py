from phonescrape import scrape

phones = ['10.131.194.6']

for phone in phones:
    details = scrape.allDetails('10.131.194.6')
    print(details)