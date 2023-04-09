import bs4 as BS
import requests
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS \
          X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) \
          Chrome/71.0.3578.98 Safari/537.36"
           }
def weather (city):
    city = city.replace (" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}+weather&oq={city}+weather&aqs=chrome..69i57l2.3024j0j7&sourceid=chrome&ie=UTF-8',
        headers=headers
    )
    print(f'please wait we loading up {city}\'s weather for you ... \n')
    soup= BS.BeautifulSoup(res.text, 'html.parser')
    location= soup.select('#wob_loc')[0].getText().strip()
    time= soup.select('#wob_dts')[0].getText().strip()
    info= soup.select('#wob_dc')[0].getText().strip()
    weather= soup.select('#wob_tm')[0].getText().strip()
    print(location)
    print(time)
    print(info)
    print(weather)

city = input(" please Enter Your City ->  ")
city = city +" weather "
weather(city)
print(' Good Luck , Have A Nice Day')


"""
developed by mehrab mahmoudifar
Hope You enjoy it
♥
"""

