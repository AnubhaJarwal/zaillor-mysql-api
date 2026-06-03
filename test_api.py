print("TEST FILE STARTED")
import requests

data = {
    "leadId": "TEST001",
    "websiteUrl": "https://test.com",
    "email": "test@test.com",
    "phone": "9999999999",
    "overallScore": 75,
    "leadStatus": "Warm"
}

response = requests.post(
    "http://127.0.0.1:5000/saveLead",
    json=data
)

print(response.text)