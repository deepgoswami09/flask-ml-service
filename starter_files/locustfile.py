from locust import HttpUser, task
            
class User(HttpUser):
    @task
    def mainPage(self):
        self.client.get("http://localhost:5000/")
        self.client.post("http://localhost:5000/predict")
