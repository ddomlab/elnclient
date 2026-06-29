import os, requests



class ElnClient:
    def __init__(self, url: str, api_key: str):
        self.url = url
        self.api_key = api_key

        # Useful variables:
        self.title = ""
        self.desc = ""
        self.id = None

        self.headers = {
            "Authorization": f"{self.api_key}",
            "Content-Type": "application/json"
        }

    def init_experiment(self, title: str, desc: str):
        """Initalazes an experiment using a title and description, the minimal info needed to make an experiment

        Args:
            title (str): Title of experiment
            desc (str): Description of experiment

        Raises:
            RuntimeWarning: Error sending info to ELN

        Returns:
            int: ID of new experiment in ELN
        """
        self.title = title
        self.desc = desc

        data = {    #This defines who can read/write to the experiment in the ELN (30=anyone)
            "canwrite": "{\"base\":30,\"teams\":[],\"teamgroups\":[],\"users\":[]}",
            "title": title,
            "body": desc
        }

        r = requests.post(f"{self.url}/experiments/", headers=self.headers, json=data)
        if r.status_code != 201:
            raise RuntimeWarning(f"Error code: {r.status_code}\nCould not send this following data:\n{data}")
        
        self.id = int(r.headers["Location"].split('/')[-1]) # get the id from the last bit of the url
        return self.id
    
    def upload_image(self):
        pass