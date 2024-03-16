import base64
encoded_string = "m)5}݄ͩͭ|'
decoded_binary = base64.b64decode(encoded_string)
decoded_string = decoded_binary.decode()