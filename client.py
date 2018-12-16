import socket
import sys
import random

def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 8899
    randide = random.randint(0, 65536) #產生隨機16bit identifier
    sequenceNum = 1
    messageFormat = {"type": "8","identifier": randide}

    try:
        
        soc.connect((host, port))
        
    except:
        print("Connection error")
        sys.exit()
    
        
    print("Enter 'quit' to exit")
    message = input(" -> ")
    print (soc.recv(1024))
    print('your idetifier is '+str(messageFormat.get('identifier')))
    while message != 'quit':
        soc.sendall(message.encode("utf8"))
        sequenceNum = 1
        seq = 'Sequence Number: '+ str(sequenceNum)+' '
        ide = ' Random identifier is ' + str(messageFormat.get('identifier'))
        # 將sequenceNum轉成byte格式
        byte_seq = bytes(seq, encoding="utf8")
        byte_type= bytes('type: 8 ', encoding='utf8')
        byte_ide = bytes(ide,encoding='utf8')
        soc.send(byte_seq)
        soc.send(byte_type)
        soc.send(byte_ide)
        if soc.recv(5120).decode("utf8") == "-":
            pass        # null operation

        message = input(" -> ")
        


    soc.send(b'--quit--')


if __name__ == "__main__":
    main()
