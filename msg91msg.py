import http.client
import random
import json
def sendMsg():
    conn = http.client.HTTPConnection("api.msg91.com")
    num=input("enter mobno:")
    msg=input("enter msg:")
    payload="{\"sender\":\"@Raja@\", \"route\": \"4\", \"country\": \"91\", \"sms\": [{\"message\":\"" + msg + "\", \"to\": [\"" + num + "\"]}]}"
    headers={
        'authkey': "300681AoXgnUT65db19e51",
        'content-type': "application/json"
    }
    conn.request("POST","/api/v2/sendsms?country=91&sender=&route=&mobiles=&authkey=&encrypt=&message=&flash=&unicode=&schtime=&aferminute=&response=&campaign=",payload, headers)
    data=conn.getresponse()
    res=json.loads(data.read().decode("UTF-8"))
    print(res)
    if res["type"]=="success":
        print("msg sent")
    else:
        print("msg not sent")
if __name__=="__main__":
    sendMsg()
