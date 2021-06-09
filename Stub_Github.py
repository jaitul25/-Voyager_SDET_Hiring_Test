from Stub_API import main
import requests
import unittest
import json


class Github_Stub(object):

    def __init__(self) -> None:
        self.base_url = "https://api.github.com/users" 


    def gateway_response_check(self, username):
        
        url = f"{self.base_url}/{username}"
        response = requests.get(url)
        return response.ok

    def response_status_check(self, username):
        
        url = f"{self.base_url}/{username}"
        response = requests.get(url)
        return response.status_code


    def get_user_info(self, username):
        
        
        url = f"{self.base_url}/{username}"
        return requests.get(url).json

    def get_user_repo_info(self, username):

        url = f"{self.base_url}/{username}/repos"
        return requests.get(url).json()








