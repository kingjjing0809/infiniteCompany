from curl_cffi import requests
import os

url = "https://videos.pexels.com/video-files/853889/853889-hd_1080_1920_25fps.mp4"
dest = "assets/bg_video/test_bamboo.mp4"

os.makedirs("assets/bg_video", exist_ok=True)
print("Downloading using curl_cffi with full browser header simulation...")
try:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "video/webm,video/ogg,video/*;q=0.9,application/ogg;q=0.7,audio/*;q=0.6,*/*;q=0.5",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6",
        "Referer": "https://www.pexels.com/",
        "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "video",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-site",
    }
    r = requests.get(url, headers=headers, impersonate="chrome120")
    print("Status code:", r.status_code)
    if r.status_code == 200:
        with open(dest, "wb") as f:
            f.write(r.content)
        print("Download successful! File size:", os.path.getsize(dest))
    else:
        print("Download failed with status:", r.status_code)
except Exception as e:
    print("Error occurred:", e)
