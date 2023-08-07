import requests
import json
from time import sleep
from newspaper import Article

# Monster API setup
API_KEY = "YOUR_MONSTER_API_KEY"
AUTHORIZATION = "YOUR_MONSTER_AUTH_TOKEN"
url = "https://api.monsterapi.ai/apis/add-task"
fetch_url = "https://api.monsterapi.ai/apis/task-status"

headers = {
    "x-api-key": API_KEY,
    "Authorization": f"Bearer {AUTHORIZATION}",
    "Content-Type": "application/json",
}

# Read URL from the user
article_url = input("Enter the URL of the article: ")

# Use newspaper3k to extract article content
article = Article(article_url)
article.download()
article.parse()

# Prepare data for Monster API
data = {
    "model": "llama2-7b-chat",
    "data": {
        "prompt": f"Please summarize the following article:\n\n{article.text[:2048]}",
        "top_k": 10,
        "top_p": 0.9,
        "temp": 0.1,
        "max_length": 1000,
        "beam_size": 1
    }
}

# Post to Monster API and get process_id
response = requests.post(url, headers=headers, data=json.dumps(data))
process_id = response.json()["process_id"]

# Polling to get the result from Monster API
status = None
while True:
    response = requests.post(
        fetch_url,
        headers=headers,
        data=json.dumps({
            "process_id": process_id,
        })).json()

    status = response["response_data"]["status"]
    if status not in ("COMPLETED", "FAILED"):
        sleep(2)
    else:
        break

# Print out the result
if status == "COMPLETED":
    print(response["response_data"]["result"]["text"])
else:
    print("Error:", response["response_data"]["result"]["errorMessage"])
