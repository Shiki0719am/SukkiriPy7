import requests as r
responce = r.get("http://www.python.org/downloads/")
text = responce.text
print(text)