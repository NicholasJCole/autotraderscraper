from bs4 import BeautifulSoup
import urllib2
import re

url = 'http://www.autotrader.com/cars-for-sale/Used+Cars/Toyota/Camry/Dallas+TX-75204?endYear=2015&listingType=used&listingTypes=used&makeCode1=TOYOTA&mmt=%5BTOYOTA%5BCAMRY%5B%5D%5D%5B%5D%5D&modelCode1=CAMRY&searchRadius=75&showcaseListingId=362401789&showcaseOwnerId=100025948&sortBy=derivedpriceASC&startYear=2008&Log=0'

response = urllib2.urlopen(url)

html = response.read() 


car_data = BeautifulSoup(html)


#data = car_data.find_all('span', {'class':'atcui-truncate ymm'})
#get make and model
#make_model = re.findall(r'>(Used[a-zA-Z0-9 ]+)', str(data))


paragraph_data = car_data.find_all('div', {'class':'listing listing-findcar listing-dealer '})

make_models = []
prices = []
mm_prices = []
for section in paragraph_data:
    make_models.append(re.findall(r'>(Used[a-zA-Z0-9 ]+)', str(section)))
    price_span = section.find_all('h4', {'class':'primary-price'})
    prices.append(re.findall(r'span>([$,0-9]+)</span', str(price_span)))


#make_model = re.findall(r'>(Used[a-zA-Z0-9 ]+)', str(paragraph_data))

print(paragraph_data[0])
