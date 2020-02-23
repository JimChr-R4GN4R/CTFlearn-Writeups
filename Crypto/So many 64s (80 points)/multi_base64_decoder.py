import base64

stop = 0

base64_message = 'HERE_PUT_YOUR_BASE64_ENCODED_TEXT'

while stop == 0:

  try: # that means there can be base64 decode
    print("Base64 decode available")
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    base64_message = message
  except: # that means there cannot be other base64 decode, so this should be the plaintext
    print(message)
    stop = 1

