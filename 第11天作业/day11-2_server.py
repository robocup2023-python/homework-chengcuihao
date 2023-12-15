import requests,hashlib,threading,random,time,socket,os

def api_translate(ori, lang_from,lang_to):
    time.sleep(random.random()*5)
    app_id = "20231006001838395"
    api_key = "2V2VIzuB8c8g8dI8VqLD"
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    salt = str(random.randint(1,65536))
    sign = hashlib.md5((app_id+ori+salt+api_key).encode('utf-8')).hexdigest()
    data = {
        'q': ori,
        'from': lang_from,
        'to': lang_to,
        'appid': app_id,
        'salt': salt,
        'sign': sign,
        'Content-Type':'application/x-www-form-urlencoded'
    }
    res = requests.post(data=data,url=url).json()
    try:
        res = res['trans_result'][0]['dst']
    except Exception:
        pass
    return res

def process_request(client):
    print(client, os.getpid())
    msg, lang_from, lang_to = client.recv(2048).decode('utf-8').split('|')
    result = api_translate(msg,lang_from=lang_from,lang_to=lang_to)
    client.send(bytes(result.encode('utf-8')))
    client.close()



if __name__ == "__main__":
    server = socket.socket()
    server.bind(("localhost",6666))
    server.listen()

    while True:
        client, addr = server.accept()
        subthread = threading.Thread(target=process_request,args=(client,))
        subthread.start()
    

