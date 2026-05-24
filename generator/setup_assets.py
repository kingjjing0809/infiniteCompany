import os
import urllib.request

def setup():
    print("=== [코다리 부장의 에셋 세팅 자동화] ===")
    
    # 1. 필요한 디렉터리 생성
    dirs = [
        "assets/bg",
        "assets/fonts",
        "output"
    ]
    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)
            print(f"[생성 완료] 디렉터리: {d}")
            
    # 2. 고품질 시니어 서체 (Sawarabi Mincho Regular) 다운로드
    font_url = "https://github.com/google/fonts/raw/main/ofl/sawarabimincho/SawarabiMincho-Regular.ttf"
    font_dest = "assets/fonts/SawarabiMincho-Regular.ttf"
    
    if not os.path.exists(font_dest):
        print(f"[다운로드 시작] 시니어용 폰트 (Noto Serif JP)...")
        try:
            # User-Agent 추가하여 다운로드 거부 방지
            req = urllib.request.Request(
                font_url, 
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            with urllib.request.urlopen(req) as response, open(font_dest, 'wb') as out_file:
                out_file.write(response.read())
            print(f"[다운로드 완료] 폰트 저장 완료: {font_dest}")
        except Exception as e:
            print(f"[다운로드 실패] 폰트 다운로드 중 오류 발생: {e}")
            print("대체용 기본 시스템 폰트를 사용하도록 대비해야 합니다.")
    else:
        print("[세팅 완료] 이미 폰트 파일이 존재합니다.")

    # 3. 9:16 최적화 고화질 감성 배경 이미지 다운로드
    bg_templates = {
        "calm_forest": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=1080&h=1920&fit=crop",
        "sunset_ocean": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=1080&h=1920&fit=crop",
        "green_leaves": "https://images.unsplash.com/photo-1501854140801-50d01698950b?q=80&w=1080&h=1920&fit=crop",
        "morning_sun": "https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?q=80&w=1080&h=1920&fit=crop",
        "cozy_room": "https://images.unsplash.com/photo-1513694203232-719a280e022f?q=80&w=1080&h=1920&fit=crop",
        "night_stars": "https://images.unsplash.com/photo-1506318137071-a8e063b4bec0?q=80&w=1080&h=1920&fit=crop",
        "lake_mist": "https://images.unsplash.com/photo-1501785888041-af3ef285b470?q=80&w=1080&h=1920&fit=crop",
        "soft_clouds": "https://images.unsplash.com/photo-1534088568595-a066f410bcda?q=80&w=1080&h=1920&fit=crop",
        "windy_field": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?q=80&w=1080&h=1920&fit=crop",
        "default": "https://images.unsplash.com/photo-1469474968028-56623f02e42e?q=80&w=1080&h=1920&fit=crop"
    }
    
    print("\n[다운로드 시작] 9:16 감성 배경 템플릿 다운로드 중...")
    for key, url in bg_templates.items():
        dest = f"assets/bg/{key}.jpg"
        if not os.path.exists(dest):
            try:
                req = urllib.request.Request(
                    url, 
                    headers={'User-Agent': 'Mozilla/5.0'}
                )
                with urllib.request.urlopen(req) as response, open(dest, 'wb') as out_file:
                    out_file.write(response.read())
                print(f" -> [완료] {key}.jpg 저장 성공!")
            except Exception as e:
                print(f" -> [실패] {key}.jpg 다운로드 실패: {e}")
        else:
            print(f" -> [이미 존재] {key}.jpg")
            
    print("\n=== [에셋 세팅 프로세스 완료! 대표님 짱!] ===")

if __name__ == "__main__":
    setup()
