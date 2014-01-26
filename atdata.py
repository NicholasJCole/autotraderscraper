from bs4 import BeautifulSoup
import urllib2
import re
import mechanize

url = 'http://www.autotrader.com/cars-for-sale/Used+Cars/Toyota/Camry/Dallas+TX-75204?endYear=2015&listingType=used&listingTypes=used&makeCode1=TOYOTA&mmt=%5BTOYOTA%5BCAMRY%5B%5D%5D%5B%5D%5D&modelCode1=CAMRY&searchRadius=75&showcaseListingId=362401789&showcaseOwnerId=100025948&sortBy=derivedpriceASC&startYear=2008&Log=0'

#url = 'http://www.autotrader.com/cars-for-sale/Used+Cars/Toyota/Camry/Dallas+TX-75204?endYear=2015&listingType=used&listingTypes=used&makeCode1=TOYOTA&mmt=%5BTOYOTA%5BCAMRY%5B%5D%5D%5B%5D%5D&modelCode1=CAMRY&searchRadius=75&showcaseListingId=362401789&showcaseOwnerId=100025948&sortBy=derivedpriceASC&startYear=2002&Log=0'

br = mechanize.Browser()
br.set_handle_robots(False)

r = br.open(url)
html = r.read()

#response = urllib2.urlopen(url)
#html = response.read() 


car_data = BeautifulSoup(html)


#data = car_data.find_all('span', {'class':'atcui-truncate ymm'})
#get make and model
#make_model = re.findall(r'>(Used[a-zA-Z0-9 ]+)', str(data))


paragraph_data = car_data.find_all('div', {'class':'listing listing-findcar listing-dealer '})

make_models = []
prices = []
mm_prices = []
for section in paragraph_data:
    make_model = re.findall(r'>(Used[a-zA-Z0-9 ]+)', str(section))
    price_span = section.find_all('h4', {'class':'primary-price'})
    price = re.findall(r'span>([$,0-9]+)</span', str(price_span))
    mileage_span = section.find_all('span', {'class':'atcui-bold'})[0]
    mileage = re.findall(r'>([0-9,]+)<', str(mileage_span))[0]
    trim_span = section.find_all('span', {'class':'trim'})
    trim = re.findall(r'">([A-Za-z0-9]+)</span', str(trim_span))
    mm_prices.append(make_model[0] + " " + str(trim) + " " + price[0] + " " + mileage)

#remove commas and dollar signs
cleaned_mm_prices = []
for eachline in mm_prices:
	cleaned_mm_prices.append(eachline.replace(",", "").replace("$", ""))

   

#make_model = re.findall(r'>(Used[a-zA-Z0-9 ]+)', str(paragraph_data))

print(cleaned_mm_prices)
