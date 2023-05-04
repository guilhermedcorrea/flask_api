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
        

@GPT.route("/api/v1/completion/gpt")
def return_completions():
    """Realizando Pedidos"""
    url = r"https://api.openai.com/v1/models"

    payload = json.dumps({
    "model": f"{ID_MODEL}",
    "prompt": "create story: Write a short story on cyndrela",
    "max_tokens": 4000,
    "temperature": 0,
    "top_p": 1,
    "n": None,
    "stream": False,
    "logprobs": None,
    "stop": None
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
    
