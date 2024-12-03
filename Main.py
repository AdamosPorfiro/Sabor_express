from fastapi import FastAPI, Query

app = FastAPI() #Como se fosse uma classe

from fastapi import FastAPI
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    return {'Hello':'World'}

#Endpoint
@app.get('/api/restaurante/')
def get_restaurantes(restaurante: str = Query(None)):
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados' : dados_json}
        
        dados_restaurante = []
        for item in dados_json:
           if item['Company'] == restaurante:
                dados_restaurante.append ({
                    'item' : item['Item'],
                    'price' : item['price'],
                    'description' : item['description']
            })
        return {'Restaurante' : restaurante,'Cardápio' : dados_restaurante}

    else:
        return {f'Erro' : f'{response.status_code} - {response.text}'}
