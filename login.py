import requests
from WXBizDataCrypt import WXBizDataCrypt

def get_openid(js_code):
    appid = 'wx1e4a6d8d42cb0b35'
    secret = 'd73e8479f9981b5dd1e153a869eec8e7'
    url = 'https://api.weixin.qq.com/sns/jscode2session'
    params = {
        'appid': appid,
        'secret': secret,
        'js_code': js_code,
        'grant_type': 'authorization_code'
    }
    response = requests.get(url, params=params)
    # print(response.json())
    return response.json()


def login(code,encryptedData,iv):
    appId = 'wx1e4a6d8d42cb0b35'
    # sessionKey = 'tiihtNczf5v6AKRyjwEUhQ=='
    sessionKey = get_openid(code)['session_key']
    # encryptedData = 'CiyLU1Aw2KjvrjMdj8YKliAjtP4gsMZMQmRzooG2xrDcvSnxIMXFufNstNGTyaGS9uT5geRa0W4oTOb1WT7fJlAC+oNPdbB+3hVbJSRgv+4lGOETKUQz6OYStslQ142dNCuabNPGBzlooOmB231qMM85d2/fV6ChevvXvQP8Hkue1poOFtnEtpyxVLW1zAo6/1Xx1COxFvrc2d7UL/lmHInNlxuacJXwu0fjpXfz/YqYzBIBzD6WUfTIF9GRHpOn/Hz7saL8xz+W//FRAUid1OksQaQx4CMs8LOddcQhULW4ucetDf96JcR3g0gfRK4PC7E/r7Z6xNrXd2UIeorGj5Ef7b1pJAYB6Y5anaHqZ9J6nKEBvB4DnNLIVWSgARns/8wR2SiRS7MNACwTyrGvt9ts8p12PKFdlqYTopNHR1Vf7XjfhQlVsAJdNiKdYmYVoKlaRv85IfVunYzO0IKXsyl7JCUjCpoG20f0a04COwfneQAGGwd5oa+T8yO5hzuyDb/XcxxmK01EpqOyuxINew=='
    # iv = 'r7BXXKkLb8qrSNn05n0qiA=='

    pc = WXBizDataCrypt(appId, sessionKey)
    UserInfo = pc.decrypt(encryptedData, iv)
    # print (UserInfo)
    return UserInfo
# # js_code = '0e3Lao000xT76S1ihW100q2CQ43Lao0n'
# # openid = get_openid(js_code)
#
# if __name__ == '__main__':
#     code = '0a34oB0w3rVfM23EHX3w3BoOsi34oB0H'
#     encryptedData = 'dd+WzL6c3uqtlTLcvJLWI9yY8Lgo0TSupqaV1PAqHEIS7bB0lOm68rXB35ieBwGxJ9vnULtKi7I/95rD+2pXiBZr/fqJxTqJ0lED9zywLq6h3/dhIDhcgLs+30FYApPNjbxwuqHaWe2g0wB9uHCpGfe/qx+i+042BTVoYXhAVYH1C9Lp8LQthbmyke+Fh9z/4TiWoQZTkGqP5Iw7ag29Sf8g9bMmayOCo4A9Tw+piJA0lvJICtPDMdUGSaAkOrwe/TeBrr3LIvW2xTvC1bKofmXpLJ5mhVE2wP5CV1wNcEECNmx0+902icYBZNJDjrA/DKGFXtXAiZGuGKxjf0aatT7cVUKWAyGTXtFPnOrL/0+IO7dg5TzNmlIoADG8eVtfgmn1JnS+ZFy7ZITptlPOC3KwWycHcX8vX/gLqkfmoRP0x4eSTjpkL4V6WeNPaqea8RF3gYYKN1YWz8adsko82w=='
#     iv = 'Ovm3OlLGIzfm/qhQI5f8uw=='
#     login(code,encryptedData,iv)

