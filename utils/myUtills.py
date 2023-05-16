import requests, json


# het API call and return response data
def getAPIData(url):
    header = {"content-type": "application/json"}
    print("RequestsURL:", url)
    response = requests.get(url, verify=False, headers=header)
    data = response.json()
    assert len(data) > 0, "empty response"
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken
