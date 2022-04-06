import requests as rq
from typing import Union

class Pantry:
  '''
  The pantry class
  
  Used for working with pantry api
  '''
  def __init__(self, id: str, _default_basket: str = None): 
    self.id = id
    self._start = _default_basket
    self.payload = ''
    self.headers = {
      "Content-Type": "application/json"
    }
  
  def get_default(self):
    return self._start
  
  def set_default(self, _default_basket):
    self._start = _default_basket
    
  def remove_default(self):
    del self._start
  
  def pantry(self):
    '''
    shows pantry info
    '''
    url = f"https://getpantry.cloud/apiv1/pantry/{self.id}"
    response = rq.get(url, headers = self.headers, data = self.payload)
    
    return response.json()
  
  def new_basket(self, name: str, content: Union[dict, str, list, int, float] = None):
    '''
    creates new basket
    '''
    url = f"https://getpantry.cloud/apiv1/pantry/{self.id}/basket/{name.replace(' ', '%20')}"
    
    payload = self.payload
    
    if content != None:
      payload = __import__("json").dumps(content)

    response = rq.post(url, headers = self.headers, data = payload)

    return response.text
  
  def push(self, *, basket: str = None, content: Union[dict, str, list, int, float]):
    '''
    appends item to basket
    '''
    if self._start != None and basket == None:
      basket = self._start
    
    url = f"https://getpantry.cloud/apiv1/pantry/{self.id}/basket/{basket.replace(' ', '%20')}"
    
    payload = __import__("json").dumps(content)
    
    response = rq.put(url, headers = self.headers, data = payload)
    
    try:
      return f"Appended {content} to {basket}: {response.json()}"
    except:
      return self.new_basket(basket, content)
  
  def pull(self, basket: str = None):
    '''
    gets items from basket
    '''
    if self._start != None and basket == None:
      basket = self._start
    
    url = f"https://getpantry.cloud/apiv1/pantry/{self.id}/basket/{basket.replace(' ', '%20')}"
    response = rq.get(url, headers = self.headers, data = self.payload)
    
    try:
      return response.json()
    except:
      return f"{basket} does not exist!"
    
  def edit(self, *, basket: str = None, keys: list = [], content: Union[dict, str, list, int, float]):
    '''
    edits content in basket
    '''
    if self._start != None and basket == None:
      basket = self._start
    
    info = self.pull(basket)
    code = f"info{''.join(f'[/{item}/]' for item in keys)} = {content}"
    exec(code.replace("/", "\""))
    # overwrites the contents
    return self.new_basket(basket, info)
      
  def remove(self, *, basket: str = None, keys: list = []):
    '''
    removes content from basket
    '''
    if self._start != None and basket == None:
      basket = self._start
      
    info = self.pull(basket)
    code = f"del info{''.join(f'[/{item}/]' for item in keys)}"
    exec(code.replace("/", "\""))
    # overwrites the contents
    return self.new_basket(basket, info)
  
  
  def del_basket(self, basket):
    '''
    deletes selected basket
    '''
    url = f"https://getpantry.cloud/apiv1/pantry/{self.id}/basket/{basket.replace(' ', '%20')}"
    response = rq.delete(url, headers = self.headers, data = self.payload)
    
    try:
      return response.text
    except:
      return f"{basket} does not exist!"
    
  def copy_basket(self, old: str, new: str):
    '''
    copies old basket to new one
    '''
    olddata = self.pull(old)
    return self.push(new, olddata)
  
  default = property(fget = get_default, fset = set_default, fdel = remove_default)
