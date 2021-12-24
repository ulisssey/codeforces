import requests
from bs4 import BeautifulSoup
# Request
link = 'https://browser-info.ru/'
response = requests.get(link).text
# Request Object
soup = BeautifulSoup(response, 'lxml')
block = soup.find('div', id='tool_padding')
# JavaScript
js = block.find('div', id='javascript_check')
check_js = js.find_all('span')[1].text
# Flash
fl = block.find('div', id='flash_version')
check_fl = fl.find_all('span')[1].text
# User Agent
ua = block.find('div', id='user_agent').text

print(check_js)
print(check_fl)
print(ua)
