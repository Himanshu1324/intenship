import requests


url = input("Enter url of text file : ")
res = requests.get(url)
print(res.text)
input("Press any key....")
