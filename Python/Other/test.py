def send_request_with_greeting(url, data=None):
    
    headers = {
        "Greeting": "老哥，你好"
    }
    response = requests.post(url, data=data, headers=headers)
    
    return response