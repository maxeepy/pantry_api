import requests as rq
import json

class Pantry:
  def __init__(self, id: str):
    self.id = id
  
  def info(self):
    '''
    shows pantry info
    '''
    url = f"https://getpantry.cloud/apiv1/pantry/{self.id}"
    
    payload = ""
    headers = {
      'Content-Type': 'application/json'
    }

    response = rq.get(url, headers = headers, data = payload)
    
    return response.json()
  
  def new_basket(self, name: str, content: dict = None):
    '''
    creates new basket
    '''
    url = f"https://getpantry.cloud/apiv1/pantry/{self.id}/basket/{name.replace(' ', '%20')}"
    
    payload = ""
    
    if content != None:
      payload = json.dumps(content)
    
    headers = {
      'Content-Type': 'application/json'
    }

    response = rq.post(url, headers = headers, data = payload)

    return response.text
  
  def push(self, basket: str, content: dict):
    '''
    appends item to basket
    '''
    url = f"https://getpantry.cloud/apiv1/pantry/{self.id}/basket/{basket.replace(' ', '%20')}"
    
    payload = json.dumps(content)
    
    headers = {
    'Content-Type': 'application/json'
    }
    
    response = rq.put(url, headers = headers, data = payload)
    
    try:
      return f"Appended {content} to {basket}: {response.json()}"
    except:
      return self.new_basket(basket, content)
  
  def pull(self, basket):
    '''
    gets items from basket
    '''
    url = f"https://getpantry.cloud/apiv1/pantry/{self.id}/basket/{basket.replace(' ', '%20')}"
    
    payload = ""
    
    headers = {
    'Content-Type': 'application/json'
    }
    
    response = rq.get(url, headers = headers, data = payload)
    
    try:
      return response.json()
    except:
      return f"{basket} does not exist!"
    
  def del_basket(self, basket):
    '''
    deletes selected basket
    '''
    url = f"https://getpantry.cloud/apiv1/pantry/{self.id}/basket/{basket.replace(' ', '%20')}"
    
    payload = ""
    
    headers = {
    'Content-Type': 'application/json'
    }
    
    response = rq.delete(url, headers = headers, data = payload)
    
    try:
      return response.text
    except:
      return f"{basket} does not exist!"