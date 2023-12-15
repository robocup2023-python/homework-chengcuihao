import socket

def send_request(text, lang_from='auto',lang_to='auto'):
    client = socket.socket()
    client.connect(("localhost",6666))
    msg = text+'|'+lang_from+'|'+lang_to
    client.send(msg.encode('utf-8'))
    response = client.recv(2048).decode('utf-8')
    print(response)
    client.close()

if __name__ == '__main__':
    send_request("你好，我是aaa")
    send_request('no no no')