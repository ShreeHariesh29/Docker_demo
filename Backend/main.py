from fastapi import FastAPI
from connector import DB_Connection

app = FastAPI()

@app.get("/home")
def home():
    connector = DB_Connection()
    cursor = connector.cursor()
    cursor.execute("""Select * from products""")
    data = cursor.fetchall()
    print(data)
    return data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)