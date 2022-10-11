from locust import HttpUser, task
            
class User(HttpUser):
    @task
    def mainPage(self):
        self.client.get("https://subhadeepapp11.azurewebsites.net/")
        self.client.post("https://subhadeepapp11.azurewebsites.net:443/predict")
