#project 9
import base64

while True:
    option=int(input('''----(options)----
1) Encode
2) Decode

choose a option:'''))

    if option ==1:
        msg = input(" type your message:")
        ascii_encode= msg.encode("ascii")
        msg_base64=base64.b64encode(ascii_encode)
        print(msg_base64)
    elif option ==2:
        msg_decode = input(" enter the message to decode:")
        dec_base64 =base64.b64decode(msg_decode)
        print(dec_base64)
    else:
         print("choose a correct option.")
    print(" ===================================================")    
 
