import requests

print(
    requests.post(
        "http://0.0.0.0:10000",
        json={
            "query": "what is meta's new product in metaverse called?"
        }
    ).json()
)
