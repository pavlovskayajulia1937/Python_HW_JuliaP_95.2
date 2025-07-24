import requests
from config import MY_CREDS, API_BASE_URL


class ProjectApi:
    def __init__(self):
        self.url = API_BASE_URL
        self.headers = {"Authorization": f"Bearer {self.get_token()}"}

    def get_token(self):
        creds = MY_CREDS
        resp = requests.post(self.url + 'auth/keys', json=creds)
        return resp.json()["key"]

    def create_project(self, title, users):
        projects = {
            "title": title,
            "users": users
        }
        resp = requests.post(
            self.url + 'projects', json=projects, headers=self.headers)
        return resp.json()
    
    def edit(self, new_title, new_id):
        projects = {
            "title": new_title
        }
        resp = requests.put(
            self.url + 'projects/' + new_id, json=projects,
            headers=self.headers)
        return resp

    def get_project(self, id):
        resp = requests.get(
            self.url + 'projects/' + str(id),
            headers=self.headers)
        return resp.json()
