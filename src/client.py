import requests
import json

api_key='sa_2d29e79fd565cf563bd307d3fe33781f778f2863d177e51416d1ad4ea005238e';
base_url='https://ca-seassessment-api-dev.happywater-190f264d.northcentralus.azurecontainerapps.io'
class AssessmentClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url.rstrip('/')
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "SE-Assessment-Client"
        }
        self.session = requests.Session()
    
    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        resp = self.session.get(url, headers=self.headers)
        print(f"[{resp.status_code}] {endpoint}")
        try:
            print(resp.json())
        except:
            print(resp.text[:500])
        return resp
    
    def post(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        resp = self.session.post(url, headers=self.headers, json=payload)
        print(f"[{resp.status_code}] {endpoint}")
        try:
            print(resp.json())
        except:
            print(resp.text)
        return resp