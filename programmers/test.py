import requests
a = ['3']
print(a[0][-1])
res = requests.get('https://google.com')
print(type(res.status_code))
