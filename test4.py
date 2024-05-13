import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import time


def signature_create(data, cipher):
    # start_time = time.time()
    padded_data = pad(data.encode('utf-8'), AES.block_size)
    ciphertext = cipher.encrypt(padded_data)
    ciphertext_str = base64.b64encode(ciphertext).decode('utf-8')
    # end_time = time.time()
    # print(f'signature_create() {end_time - start_time}')
    # print(f'ciphertext_str: {ciphertext_str}')
    return ciphertext_str

def generate_timestamp():
    return str(int(time.time()))

def signature_encrypt(url, cipher):
    return signature_create(
        (url + "######" + generate_timestamp() + "######" + '6640c2fce4b025c9c340557c64956404' + "######" + "12"),
        cipher)


def video_parse_url(url):
    key = 'yytkjfgzmnklfgyy'.encode('utf-8')
    cipher = AES.new(key, AES.MODE_ECB)

    data = {
        'link': url,
        'source': 12,
        'timestamp': generate_timestamp(),
        'signature': signature_encrypt(url, cipher),
        'version': 1
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/9115',
        'Content-Type': 'application/json',
        'xweb_xhr': '1',
        'token': '6640c2fce4b025c9c340557c64956404',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://servicewechat.com/wx47d026b451350289/58/page-frame.html',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    # print(data)
    response = requests.post('https://analyse.layzz.cn//lyz/platWeChatAnalyse', headers=headers, json=data)
    response_to_return = {
        'url': response.json()["data"]["playAddr"],
        'image': response.json()['data']['cover']
    }
    return response_to_return


url = '4.66 复制打开抖音，看看【不是猪婆_的作品】好 我会改# 今天长这样 # 今天先长这样明天我再... https://v.douyin.com/i2aPnD7d/ V@y.tE 08/05 eBg:/'
for i in range(1000):
    print(video_parse_url(url))