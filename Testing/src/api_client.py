import requests

def get_location(ip):
    url = f"https://freeipapi.com/api/json/{ip}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return {
        "countryName" : data["countryName"],
        "countryCode" : data["countryCode"]
    }

if __name__ == "__main__":
    print(get_location('186.103.48.124'))