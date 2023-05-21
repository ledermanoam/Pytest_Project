import requests, json


# get API call and return response data
def getAPIData(url):
    headers = {"content-type": "application/json"}
    print("RequestsURL:", url)
    response = requests.get(url, verify=False, headers=headers)
    data = response.json()
    assert len(data) > 0, "empty response"
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken

#Put API call
def putData(url,body):
    headers = {"content-type": "application/json"}
    print("RequestsURL:", url)
    print("ReqBody:",json.dumps(body))
    response = requests.put(url, verify=False,json=body,headers=headers)
    data = response.json()
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code,timeTaken

#Delet api call
def deleteData(url,opHeader=None):
    headers = {"content-type": "application/json"}
    print("RequestsURL:", url)
    # value_when_true if condition else value_when_false e.g pass=true if marks>50 else fail
    headers = (headers | opHeader) if isinstance(opHeader,dict) else headers
    response = requests.delete(url,verify=False,headers=headers)
    print(response.request.headers)
    data = response.json()
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code,timeTaken
