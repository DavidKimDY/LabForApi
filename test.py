import os
import requests
import pprint

# URL = 'http://127.0.0.1:5000/'
# URL = 'http://0.0.0.0:8080/'
URL = 'http://0.0.0.0:49159'
USERS = 'users'
LOCATIONS = 'locations'

new_data = {
    'userId': '94040',
    'name': 'Dong',
    'city': 'si gol',

    'locations': [[]]
}

put_data = {
    'userId': '940420',
    'locations': [34]
}

delete_data = {
    'userId': '94040'
}
users_url = os.path.join(URL, USERS)

post_result = requests.post(users_url, data=new_data)
print(post_result)


put_result = requests.put(users_url, data=put_data)
print(put_result)

delete_result = requests.delete(users_url, data=delete_data)
print(delete_result)

get_result = requests.get(users_url)
print(get_result)
print(type(get_result))
result = get_result.json()
pprint.pprint(result)



