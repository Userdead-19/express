import requests
response=requests.get("https://psg-scapes-backend.onrender.com/api/attendance")
students=response.json()
print(len(students))
