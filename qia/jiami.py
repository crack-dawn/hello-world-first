from Crypto.Cipher import AES  # 需要安装的包:pip install pycryptodome
import base64

def aes_encrypt(key, data):
    pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
    data = pad(str(data))
    cipher = AES.new(key.encode('utf8'), AES.MODE_ECB)
    encryptedbytes = cipher.encrypt(data.encode('utf8'))
    encodestrs = base64.b64encode(encryptedbytes)
    enctext = encodestrs.decode('utf8')
    return enctext


if __name__ == '__main__':
    xuehao = input("输入你的学号：")
    print("你的激活码是",aes_encrypt("Dk6sIhL825BD3jss", xuehao))