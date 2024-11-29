from fastapi import FastAPI

app = FastAPI() #Como se fosse uma classe

from fastapi import FastAPI

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    return {'Hello':'World'}