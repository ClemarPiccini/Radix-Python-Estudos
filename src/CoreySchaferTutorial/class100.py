import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(response.status_code)
print(response.json())


url = 'https://httpbin.org/cookies'
cookies = {'cookie_name': 'cookie_value'}
response = requests.get(url, cookies=cookies)
print(response.json())

url = 'https://jsonplaceholder.typicode.com/posts'
data = {'title': 'foo', 'body': 'bar', 'userId': 1}
response = requests.post(url, json=data)
print(response.json())

url = 'https://www.example.com/image.jpg'
response = requests.get(url)
with open('image.jpg', 'wb') as f:
    f.write(response.content)