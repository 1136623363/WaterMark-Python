import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import time
import yt_dlp

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


def youtube(url):
    # 设置下载参数
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
    }

    # 创建一个yt-dlp对象
    ydl = yt_dlp.YoutubeDL(ydl_opts)

    # 提取视频信息
    info_dict = ydl.extract_info(url, download=False)

    # 获取视频和音频的下载链接
    video_url = None
    thumbnail_url = None
    if 'formats' in info_dict:
        for format in info_dict['formats']:
            if format.get('acodec') != 'none' and format.get('vcodec') != 'none':
                video_url = format['url']
                break

    if 'thumbnail' in info_dict:
        thumbnail_url = info_dict['thumbnail']

    return video_url, thumbnail_url
def video_parse_url(url):
    if "youtube" in url:
        video_url,image_url = youtube(url)
    else:
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

        video_url = response.json()["data"]["playAddr"]
        image_url = response.json()['data']['cover']

    response_to_return = {
        'url': video_url,
        'image': image_url
    }
    return response_to_return