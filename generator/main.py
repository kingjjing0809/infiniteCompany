import os
import json
import asyncio
import argparse
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import edge_tts
from moviepy import VideoFileClip, ImageClip, AudioFileClip, CompositeAudioClip, CompositeVideoClip, concatenate_videoclips

# 기본 설정값
DEFAULT_FONT_PATH = "assets/fonts/SawarabiMincho-Regular.ttf"
DEFAULT_BG_VIDEO_DIR = "assets/bg_video"
OUTPUT_DIR = "output"
DEFAULT_VOICE = "ja-JP-NanamiNeural"  # 자상하고 따뜻한 일본어 여성 AI 비서 목소리

async def generate_tts(text: str, voice: str, output_path: str):
    """edge-tts를 사용하여 자연스러운 신경망 일본어 오디오를 생성합니다."""
    # TTS 가독성을 높이기 위해 줄바꿈은 띄어쓰기로 변환하여 인공지능이 자연스럽게 읽도록 처리합니다.
    clean_text = text.replace("\n", " ").replace("『", "").replace("』", "")
    communicate = edge_tts.Communicate(clean_text, voice)
    await communicate.save(output_path)
    print(f" -> [TTS 완료] 음성 합성 성공! 저장 경로: {output_path}")

def render_glass_card(quote_data: dict, output_path: str):
    """Pillow를 사용해 시니어들의 눈 피로를 덜어주는 대형 글래스모피즘 자막 카드를 렌더링합니다."""
    # 9:16 세로형 표준 해상도 (1080 x 1920)
    width, height = 1080, 1920
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 폰트 로드 (Sawarabi Mincho 사용, 없을 시 기본 폰트 대비)
    font_path = DEFAULT_FONT_PATH
    if not os.path.exists(font_path):
        font_path = "arial.ttf"  # 윈도우 시스템 기본 폰트 대비
        print("[경고] 전용 폰트가 발견되지 않아 시스템 기본 폰트를 사용합니다.")
        
    try:
        font_date = ImageFont.truetype(font_path, 28)  # v2.0 날짜 폰트
        font_title = ImageFont.truetype(font_path, 36)
        font_topic = ImageFont.truetype(font_path, 28)
        font_text = ImageFont.truetype(font_path, 42)
        font_logo = ImageFont.truetype(font_path, 30)
    except IOError:
        # 폰트 에러 발생 시 기본 폰트로 폴백
        font_date = font_title = font_topic = font_text = font_logo = ImageFont.load_default()
        
    # --- 1. 중앙 글래스 카드 배경 그리기 (v2.0 확장 레이아웃) ---
    # 카드 크기: 가로 880px, 세로 940px (날짜 추가로 인해 세로 크기 90px 확장)
    # 위치: x=100, y=480 ~ 1420
    card_x1, card_y1 = 100, 480
    card_x2, card_y2 = 980, 1420
    
    # 프리미엄 딥 슬레이트 반투명 카드 (RGB: 15, 23, 42, Alpha: 210)
    # 둥근 모서리 사각형 그리기
    draw.rounded_rectangle(
        [card_x1, card_y1, card_x2, card_y2], 
        radius=40, 
        fill=(15, 23, 42, 210), 
        outline=(255, 199, 44, 255),  # 인피니트 골드 테두리선
        width=3
    )
    
    # --- 2. [신규 v2.0 스펙] 상단 날짜 표시 (실행일 기준 매일 갱신) ---
    now = datetime.now()
    month = str(now.month)
    day = str(now.day)
    date_text = f"{month}月 {day}日"  # "5月 24日" 형태
    
    # 날짜 텍스트 중앙 맞춤 정렬
    left, top, right, bottom = draw.textbbox((0, 0), date_text, font=font_date)
    d_width = right - left
    draw.text(
        (540 - d_width / 2, card_y1 + 35),  # 카드 상단에서 35px 내려온 지점
        date_text,
        fill=(255, 199, 44, 200),  # 은은한 골드 투명 컬러
        font=font_date
    )
    
    # --- 3. 주제(Topic) 및 타이틀(Title) 그리기 (날짜 아래 배치) ---
    # 상단 뱃지 배경 (RGB: 255, 199, 44, Alpha: 230)
    badge_x1, badge_y1 = 160, 590
    badge_x2, badge_y2 = 450, 650
    draw.rounded_rectangle(
        [badge_x1, badge_y1, badge_x2, badge_y2],
        radius=15,
        fill=(255, 199, 44, 230)
    )
    
    # 뱃지 내부 텍스트 그리기 (검정색)
    topic_text = quote_data.get("topic", "こころの時間")
    left, top, right, bottom = draw.textbbox((0, 0), topic_text, font=font_topic)
    t_width = right - left
    t_height = bottom - top
    badge_center_x = (badge_x1 + badge_x2) / 2
    badge_center_y = (badge_y1 + badge_y2) / 2
    draw.text(
        (badge_center_x - t_width / 2, badge_center_y - t_height / 2 - 5),
        topic_text,
        fill=(0, 0, 0),
        font=font_topic
    )
    
    # 타이틀 그리기 (뱃지 옆에 흰색으로 표시)
    title_text = quote_data.get("title", "今日の知恵")
    draw.text(
        (480, 600),
        title_text,
        fill=(255, 255, 255),
        font=font_title
    )
    
    # 상단 장식용 골드 분할선
    draw.line([(160, 690), (920, 690)], fill=(255, 199, 44, 150), width=2)
    
    # --- 4. 명언 본문 텍스트 그리기 (화이트) ---
    text_content = quote_data.get("text", "")
    lines = text_content.split("\n")
    
    # 줄 간격 계산하여 중앙 배치
    line_y = 740
    for line in lines:
        left, top, right, bottom = draw.textbbox((0, 0), line, font=font_text)
        line_w = right - left
        # 가로 중앙 정렬
        draw.text(
            (540 - line_w / 2, line_y),
            line,
            fill=(255, 255, 255),
            font=font_text
        )
        line_y += 75  # 줄 간격
        
    # --- 5. 하단 브랜드 워터마크 그리기 ---
    draw.line([(160, 1260), (920, 1260)], fill=(255, 199, 44, 150), width=2)
    
    logo_text = "こころの時間"
    left, top, right, bottom = draw.textbbox((0, 0), logo_text, font=font_logo)
    l_width = right - left
    draw.text(
        (540 - l_width / 2, 1300),
        logo_text,
        fill=(255, 199, 44, 255),  # 따뜻한 골드 로고
        font=font_logo
    )
    
    # 파일로 저장
    img.save(output_path, "PNG")
    print(f" -> [자막 렌더링 완료] 글래스 자막 카드 생성 성공: {output_path}")

def build_video(bg_name: str, audio_path: str, overlay_path: str, output_path: str):
    """배경 비디오 루프, 로컬 음성, 자막 카드를 하나의 영롱한 쇼츠 영상(.mp4)으로 컴파일합니다."""
    print("[비디오 컴파일 시작] 동영상 합성 작업을 시작합니다...")
    
    # 1. 오디오 클립 로드 및 시간 추출
    audio_clip = AudioFileClip(audio_path)
    duration = audio_clip.duration + 0.8
    print(f" -> 오디오 길이: {audio_clip.duration:.2f}초, 비디오 길이: {duration:.2f}초")
    
    # 2. [v2.0 에셋 업그레이드] 고품질 9:16 모션 그래픽스 비디오 배경 로드
    bg_path = f"{DEFAULT_BG_VIDEO_DIR}/{bg_name}.mp4"
    if not os.path.exists(bg_path):
        bg_path = f"{DEFAULT_BG_VIDEO_DIR}/default.mp4"
        print(f"[알림] 특정 배경 비디오가 없어 기본 비디오({bg_path})를 사용합니다.")
        
    bg_clip = VideoFileClip(bg_path)
    
    # 3. 비디오가 오디오 길이보다 짧다면 루프(Looping) 적용
    if bg_clip.duration < duration:
        try:
            # MoviePy 내장 루프 적용 시도
            bg_clip = bg_clip.loop(duration=duration)
        except Exception:
            # 예외 대비: 필요한 길이만큼 비디오를 이어붙여서 커팅
            repeat_count = int(duration / bg_clip.duration) + 1
            clips_to_concat = [bg_clip] * repeat_count
            bg_clip = concatenate_videoclips(clips_to_concat)
            
    # 정밀한 커팅
    bg_clip = bg_clip.subclipped(0, duration)
    
    # 4. 투명 글래스 자막 카드 overlay clip 로드
    overlay_clip = ImageClip(overlay_path).with_duration(duration).with_position("center")
    
    # 5. 오디오 통합
    combined_audio = CompositeAudioClip([audio_clip])
    
    # 6. 비디오 및 오디오 컴포지트
    final_video = CompositeVideoClip([bg_clip, overlay_clip])
    final_video = final_video.with_audio(combined_audio)
    
    # 7. 최종 렌더링 출력 (libx264 고코덱 최적화 및 모바일 친화 모드)
    final_video.write_videofile(
        output_path,
        fps=24,
        codec="libx264",
        audio_codec="aac",
        temp_audiofile="temp-audio.m4a",
        remove_temp=True
    )
    
    # 메모리 해제
    audio_clip.close()
    bg_clip.close()
    overlay_clip.close()
    final_video.close()
    
    print(f"\n== [SUCCESS] [쇼츠 비디오 완성] 숏폼 동영상이 빌드 완료되었습니다! 저장 위치: {output_path} ==")

def main():
    parser = argparse.ArgumentParser(description="코다리 부장의 'こころの時間' v2.0 숏폼 자동 생성기")
    parser.add_argument("--day", type=int, default=1, help="제작할 30일 중의 일차 (1~30)")
    parser.add_argument("--voice", type=str, default=DEFAULT_VOICE, help="음성 합성용 일본어 Neural 목소리")
    args = parser.parse_args()
    
    # 1. DB 로드
    db_path = "content_db.json"
    if not os.path.exists(db_path):
        print(f"[에러] 명언 데이터베이스({db_path})가 없습니다!")
        return
        
    with open(db_path, "r", encoding="utf-8") as f:
        database = json.load(f)
        
    # 일차에 맞는 명언 선택 (1-indexed)
    day_idx = args.day - 1
    if day_idx < 0 or day_idx >= len(database):
        print(f"[경고] {args.day}일차 데이터를 찾을 수 없어 1일차로 기본 로드합니다.")
        day_idx = 0
        
    quote_data = database[day_idx]
    current_day = quote_data["day"]
    print(f"\n==========================================")
    print(f"[SYSTEM] [코다리 부장 쇼츠 빌더 v2.0] 제 {current_day}일차 쇼츠 제작 가동!")
    print(f" - 주제: {quote_data['topic']}")
    print(f" - 타이틀: {quote_data['title']}")
    print(f" - 배경 키워드: {quote_data['bg_keyword']}")
    print(f"==========================================\n")
    
    # 2. 임시 파일 및 출력 경로 정의
    temp_audio = f"temp_tts_{current_day}.mp3"
    temp_overlay = f"temp_overlay_{current_day}.png"
    
    date_str = datetime.now().strftime("%Y-%m-%d")
    output_filename = f"daily_shorts_day_{current_day}_{date_str}.mp4"
    final_output_path = os.path.join(OUTPUT_DIR, output_filename)
    
    try:
        # 디렉터리 안전장치
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
            
        # TTS 음성 합성 비동기 실행
        asyncio.run(generate_tts(quote_data["text"], args.voice, temp_audio))
        
        # 글래스모피즘 자막 이미지 렌더링
        render_glass_card(quote_data, temp_overlay)
        
        # 배경 매칭 및 비디오/오디오 최종 컴파일
        build_video(quote_data["bg_keyword"], temp_audio, temp_overlay, final_output_path)
        
    finally:
        # 3. 리소스 정리 (임시 파일 제거)
        print("\n[임시 파일 정리 중...]")
        if os.path.exists(temp_audio):
            try:
                os.remove(temp_audio)
                print(f" -> 임시 음성 삭제 완료: {temp_audio}")
            except Exception as e:
                print(f" -> 임시 음성 삭제 실패: {e}")
        if os.path.exists(temp_overlay):
            try:
                os.remove(temp_overlay)
                print(f" -> 임시 이미지 삭제 완료: {temp_overlay}")
            except Exception as e:
                print(f" -> 임시 이미지 삭제 실패: {e}")

if __name__ == "__main__":
    main()
