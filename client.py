import requests
import sys
import json
print(requests.get("http://localhost:5000/square",params={"number":sys.argv[1]}).json()["result"])