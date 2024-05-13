import requests

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json',
    'Authorization': 'Bearer',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.3 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1 wechatdevtools/1.06.2402040 MicroMessenger/8.0.5 Language/zh_CN webview/',
    'content-type': 'application/json',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://servicewechat.com/wx1e4a6d8d42cb0b35/devtools/page-frame.html',
}

json_data = {
    'url': 'https://v.douyin.com/i21yGjjX/',
}

response = requests.post('http://127.0.0.1:8000/api/video-parse', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"url":"https://v.douyin.com/JxHkvPT/"}'
#response = requests.post('http://127.0.0.1:8000/api/video-parse', headers=headers, data=data)
print(response.text)