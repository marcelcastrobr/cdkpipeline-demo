import requests
import os

def test_200_response():
    with requests.get(os.environ['URL']) as response:
        assert response.status_code == 200