import jwt
from datetime import datetime, timedelta

def creat_token(openId,minutes=10,secret_key="1136623363"):
    # 定义过期时间（10分钟后过期）
    expiry = datetime.utcnow() + timedelta(minutes=minutes)
    # 定义 payload
    payload = {
        "openId": openId,
        "exp": expiry
    }
    # 生成 token
    token = jwt.encode(payload, secret_key, algorithm="HS256")
    return token

def validate_token(token, secret_key="1136623363"):
    try:
        # 解码 JWT
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        # print(payload)
        # 转换 exp 字段为 datetime 对象
        exp = datetime.fromtimestamp(payload["exp"])

        # 验证签名和有效期
        if exp >= datetime.utcnow():
            return payload["openId"]
    except jwt.ExpiredSignatureError:
        # token 已过期
        return False
    except jwt.InvalidSignatureError:
        # 签名无效
        return False
    except jwt.InvalidTokenError:
        # token 格式不正确
        return False

    return False


# # 要验证的 token
# token = creat_token('this is openid')
#
# print(token)
# # 验证 token
# if validate_token(token):
#     print("Token is valid.")
# else:
#     print("Token is invalid.")

# print(validate_token('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVuSWQiOiJvYlBWRTVOMThGSFZ3T05IUllhRHZrczhFU3h3IiwiZXhwIjoxNzE1NjY3MDE0fQ.ws2bfEnvSljOMdEPoI9Xuax-Nlb3sG3xhLRMmJ7m9Q8'))