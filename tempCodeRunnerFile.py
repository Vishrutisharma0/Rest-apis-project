from flask import Flask

app=Flask(__name__)



stores=[{'name':'KP Store','items':[{'name':'pen','price':2200}]}]

@app.get("/stores")
def get_store():
    return{"stores":stores}
