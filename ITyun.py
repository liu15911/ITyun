
import requests
import json
def hidden_danger_memory(DeviceIP):
    url = 'https://136.64.214.196:26335/rest/plat/smapp/v1/oauth/token'
    json_str={ "grantType": "password", "userName": "panshi", "value": "Tjdx@1234"}
    print(json.dumps(json_str))
    GetToken =requests.put(verify=False,url=url,data=json.dumps(json_str),headers={"Accept": "application/json", "Content-Type": "application/json;charset=UTF-8"}).json()

    Json_strs={
    "obj_type_id":"1407379178520576",
    "indicator_ids":[
      "1407379178651656"
    ], "obj_ids":[DeviceIP]}

    token=GetToken["accessSession"]
    url= 'https://136.64.214.196:26335/rest/performance/v1/data-svc/latest-data/action/query'
    result =requests.post(verify=False,url=url,data=json.dumps(Json_strs),headers={"Accept": "application/json", "Content-Type": "application/json;charset=UTF-8","X-Auth-Token":token}).json()
    res=result["data"][DeviceIP]["1407379178651656"]["last_collect_data"]
    result="{\"last_collect_data\":{\""+DeviceIP+"\":"+res+"},\"result_code\":1}"
    return json.loads(result)

import requests
import json
def hidden_danger(DeviceIP):
    url = 'https://136.64.214.196:26335/rest/plat/smapp/v1/oauth/token'
    json_str={ "grantType": "password", "userName": "panshi", "value": "Tjdx@1234"}
    print(json.dumps(json_str))
    GetToken =requests.put(verify=False,url=url,data=json.dumps(json_str),headers={"Accept": "application/json", "Content-Type": "application/json;charset=UTF-8"}).json()

    Json_strs={
    "obj_type_id":"1407379178520576",
    "indicator_ids":[
      "1407379178586113"
    ], "obj_ids":[DeviceIP]}

    token=GetToken["accessSession"]
    url= 'https://136.64.214.196:26335/rest/performance/v1/data-svc/latest-data/action/query'
    result =requests.post(verify=False,url=url,data=json.dumps(Json_strs),headers={"Accept": "application/json", "Content-Type": "application/json;charset=UTF-8","X-Auth-Token":token}).json()
    res=result["data"][DeviceIP]["1407379178586113"]["last_collect_data"]
    result="{\"last_collect_data\":{\""+DeviceIP+"\":"+res+"},\"result_code\":1}"
    return json.loads(result)

import requests
import json
def  IT_interface(DeviceIP):
    url = 'https://136.64.214.196:26335/rest/plat/smapp/v1/oauth/token'
    json_str={ "grantType": "password", "userName": "panshi", "value": "Tjdx@1234"}
    print(json.dumps(json_str))
    GetToken =requests.put(verify=False,url=url,data=json.dumps(json_str),headers={"Accept": "application/json", "Content-Type": "application/json;charset=UTF-8"}).json()

    Json_strs={
    "obj_type_id":"1407379178520576",
    "indicator_ids":[
      "1407379178717196"
    ], "obj_ids":[DeviceIP]}

    token=GetToken["accessSession"]
    url= 'https://136.64.214.196:26335/rest/performance/v1/data-svc/latest-data/action/query'
    result =requests.post(verify=False,url=url,data=json.dumps(Json_strs),headers={"Accept": "application/json", "Content-Type": "application/json;charset=UTF-8","X-Auth-Token":token}).json()
    res=result["data"][DeviceIP]["1407379178717196"]["last_collect_data"]
    result="{\"last_collect_data\":{\""+DeviceIP+"\":"+res+"},\"result_code\":1}"
    return json.loads(result)

