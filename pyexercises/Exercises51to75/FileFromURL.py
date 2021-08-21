import requests

headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
response = requests.get("http://www.pythonhow.com/data/universe.txt", headers=headers)
text = response.text
count_letter_a = text.count("a")
print(count_letter_a)