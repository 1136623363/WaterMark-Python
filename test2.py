import struct

def Utf8_parse(s):
    # 将字符串转换为 UTF-8 编码的字节序列
    utf8_bytes = s.encode('utf-8')
    result = []
    i = 0
    while i < len(utf8_bytes):
        # 解析字节序列中的每4个字节为一个有符号整数
        if i + 4 <= len(utf8_bytes):
            value = struct.unpack('>i', utf8_bytes[i:i+4])[0]
        else:
            # 处理剩余不足4个字节的情况
            padding = b'\x00' * (4 - (len(utf8_bytes) - i))
            padded_bytes = utf8_bytes[i:] + padding
            value = struct.unpack('>i', padded_bytes)[0]
        result.append(value)
        i += 4
    return result

# # 测试
# s = '4.66 复制打开抖音，看看【不是猪婆_的作品】好 我会改# 今天长这样 # 今天先长这样明天我再... https://v.douyin.com/i2aPnD7d/ V@y.tE 08/05 eBg:/######1715522015######6640c2fce4b025c9c340557c64956404######12'
# result = Utf8_parse(s)
# print(result)
