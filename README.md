##Execução do projeto
<br>criar venv: py -3 -m venv venv<br/>
<br>ativar: venv\Scripts\activate<br/>
<br>instalar dependencias: pip freeze > requirements.txt<br/>
<br>instalar dependencias: pip freeze > requirements.txt<br/>
<br>$env:FLASK_APP = "app:create_app()"<br/>
<br>flask run --host=0.0.0.0<br/>

#Migrações banco de dados

<br>flask db init<br/>
<br>flask db migrate -m "Initial migration."<br/>
<br>flask db upgrade<br/>



#ENDPOINTS
#exemplo parametro
<br>flask run --host=0.0.0.0<br/>
´´´python
{
 "role": "user", "content": "Ola",
  "max_tokens": 4000,
  "temperature": 0,
  "top_p": 1}
´´´

#Autenticando
´´´python
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    print(password)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)
´´´


