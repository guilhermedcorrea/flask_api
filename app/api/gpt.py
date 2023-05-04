from flask import Blueprint, jsonify, request
import os
import openai
import requests
import json

GPT = Blueprint("gpt",__name__)

openai.organization = os.getenv("ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()
ID_MODEL = 'gpt-3.5-turbo'


@GPT.route("/api/v1/models/gpt")
def get_gpt_models():
    url = r"https://api.openai.com/v1/models"

    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}'
        }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()
    print(data)

    def get_models(*args, **kwargs):
        """teste request"""
        return 
        
    return jsonify(data)


@GPT.route("/api/v1/msgs/gpt", methods=['GET','POST'])
def return_msgs():
    store_data = request.get_json()
    print(store_data['Mensagem'])
    url = r"https://api.openai.com/v1/models"

    payload = json.dumps({
                "model": f"{ID_MODEL}",
                "messages": [
                {
                    "role": "user",
                    "content": f"{store_data['Mensagem']}"
                }
                ]
            })
    headers = {
                'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}',
                'Content-Type': 'application/json'
            }

    response = requests.request("POST", url, headers=headers, data=payload)
    response = response.json()
        
        
    def msgs(response):
        """Recebe mensagens vindas pela requisição"""
        print(response)
        
    
    return response
        

@GPT.route("/api/v1/completion/gpt/top_p", methods=['GET','POST'])
def return_completions():
    store_data = request.get_json()
    print(store_data)
    
    """Realizando Pedidos"""
 
    url = "https://api.openai.com/v1/chat/completions"

    payload = json.dumps({
    "model": f"{ID_MODEL}",
    "messages": [{"role": f"{store_data['role']}", "content": f"{store_data['content']}"}],
    "temperature" : 1.0,
    "top_p":1.0,
    "n" : 1,
    "stream": False,
    "presence_penalty":0,
    "frequency_penalty":0,
    })

    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}'
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    data = response.json()
    print(data)
    
    
    def completions(*args, **kwargs):
        """
        curl https://api.openai.com/v1/chat/completions \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $OPENAI_API_KEY" \
        -d '{
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": "Say this is a test!"}],
            "temperature": 0.7
        }'
        """
        return
  
    return jsonify(data)
    
