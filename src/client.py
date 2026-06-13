import requests
from constants import API_KEY,BASE_URL

class AssessmentClient:
    def __init__(self, BASE_URL, API_KEY):
        self.BASE_URL = BASE_URL.rstrip('/')
        self.headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "User-Agent": "SE-Assessment-Client"
        }
        self.session = requests.Session()
    
    def get(self, endpoint):
        url = f"{self.BASE_URL}{endpoint}"
        resp = self.session.get(url, headers=self.headers)
        print(f"[{resp.status_code}] {endpoint}")
        try:
            print(resp.json())
        except:
            print(resp.text[:500])
        return resp
    
    def post(self, endpoint, payload):
        url = f"{self.BASE_URL}{endpoint}"
        resp = self.session.post(url, headers=self.headers, json=payload)
        print(f"[{resp.status_code}] {endpoint}")
        try:
            print(resp.json())
        except:
            print(resp.text)
        return resp