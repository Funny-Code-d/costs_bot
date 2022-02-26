import requests

res = requests.get('http://195.140.147.137/api/v1/user/settings/')

for item in res.json():
    print(f"ID: {item['user_id']}")
    print(f"First name: {item['first_name']}")
    print(f"Last_name: {item['last_name']}")
# for item in res.text:
#     print(f"ID: {item['user_id']}")
#     print(f"First name: {item['first_name']}")
#     print(f"Last_name: {item['last_name']}")

# for item in res.text:
#     print("---")
#     print(item)