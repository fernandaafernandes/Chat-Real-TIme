import requests

URL = "http://localhost:5000"

def testar_ping():
    r = requests.get(f"{URL}/ping")
    print("Ping:", r.json())

if __name__ == "__main__":
    testar_ping()