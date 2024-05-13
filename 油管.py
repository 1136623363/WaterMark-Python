import yt_dlp

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

# 视频链接
url = 'https://www.youtube.com/watch?v=1-jybnkMtpU'

# 调用函数获取下载链接
video_url, thumbnail_url = youtube(url)
print("视频下载链接:", video_url)
print("缩略图链接:", thumbnail_url)
