import requests

def news(tag,fromdate,todate):
    url = 'https://api.stackexchange.com/2.3/questions?fromdate='+fromdate+'&todate='+todate+'&order=desc&sort=activity&tagged='+tag+'&site=stackoverflow'
    resp = requests.get(url)
    itog = resp.json()['items']
    for key in itog:
        print(key['link'])

tag = str(input('Введите запрос\n'))
print('Даты вводятся в формате год-месяц-число')
fromdate = str(input('Введите дату с\n'))
todate = str(input('Введите дату по\n'))

print(news(tag, fromdate, todate))
