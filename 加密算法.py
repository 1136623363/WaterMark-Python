from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import time

def signature_create(data):
    # 将密钥和数据转换为字节类型
    key = 'yytkjfgzmnklfgyy'.encode('utf-8')
    # data = '4.66 复制打开抖音，看看【不是猪婆_的作品】好 我会改# 今天长这样 # 今天先长这样明天我再... https://v.douyin.com/i2aPnD7d/ V@y.tE 08/05 eBg:/######1715522015######6640c2fce4b025c9c340557c64956404######12'.encode('utf-8')
    # data = '4.87 08/18 j@p.Dh vfo:/ “你是花，才会觉得春天离开你。你是春天，就永远有花。”# 那拉提草原 # 治愈系风景  https://v.douyin.com/i2ucv2Lc/ 复制此链接，打开Dou音搜索，直接观看视频！######1715524840######6640c2fce4b025c9c340557c64956404######12'.encode('utf-8')
    # 创建 AES 加密器，使用 ECB 模式和 PKCS7 填充
    cipher = AES.new(key, AES.MODE_ECB)
    # print(data)
    # 对数据进行填充
    padded_data = pad(data, AES.block_size)

    # 加密数据
    ciphertext = cipher.encrypt(padded_data)

    # 将加密后的数据转换为 base64 编码字符串
    ciphertext_str = base64.b64encode(ciphertext).decode('utf-8')

    # print(ciphertext_str)
    return ciphertext_str

def generate_timestamp():
    return str(int(time.time()))

def signature_encrypt(url):
    return signature_create((url + "######" + generate_timestamp() + "######" + '6640c2fce4b025c9c340557c64956404' + "######" + "12").encode('utf-8'))