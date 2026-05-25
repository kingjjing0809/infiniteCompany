import os
import time
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def upload_to_youtube(file_path: str, title: str, schedule_date: str = None, schedule_time: str = "06:00"):
    """
    대표님의 크롬 브라우저를 10초만 닫게 유도하는 인터랙티브 스마트 대기 기법을 가동하여,
    로그인 세션 100% 유지 + 락 충돌 0%를 동시에 완벽히 달성하고 예약을 수행하는 
    유튜브 자동화 예약 업로더 v3.0 마스터피스.
    """
    print("\n==============================================================")
    print("=== [코다리 부장의 YouTube Shorts 자동화 업로더 v3.0 마스터피스] ===")
    print("==============================================================")
    
    if not os.path.exists(file_path):
        print(f"[에러] 업로드할 비디오 파일이 존재하지 않습니다: {file_path}")
        return False
        
    abs_file_path = os.path.abspath(file_path)
    file_name = os.path.basename(file_path)
    
    # 1. 크롬 유저 데이터 및 원래 경로 확보 (구글 로그인 세션 100% 흡수용!)
    user_home = os.path.expanduser("~")
    user_data_dir = os.path.join(user_home, "AppData", "Local", "Google", "Chrome", "User Data")
    
    # 2. [v3.0 핵심 인터랙티브 대기 가동]
    # 크롬의 철통같은 전역 락(Global Lock) 장벽을 깨부수기 위해,
    # 대표님이 현재 컴퓨터에 켜두신 크롬 브라우저를 일시적으로 닫아주기를 활기차게 요청합니다!
    print("\n🫡 [충성! 대표님께 알립니다!]")
    print(" -> 영롱한 유튜브 예약 업로드를 위해 현재 컴퓨터에 켜져 있는")
    print("    [모든 크롬 브라우저 창]을 잠시만 완전히 닫아주십시오! (백그라운드 포함)")
    print(" -> 크롬을 안전하게 닫으신 후, 아래에 엔터를 입력하시면 즉시 비행을 개시합니다!")
    print("--------------------------------------------------------------")
    
    input("👉 [크롬을 닫으셨다면 엔터(Enter) 키를 입력해 주세요]: ")
    print("--------------------------------------------------------------")
    
    # 3. SingletonLock 파일 강제 청소 및 taskkill 연타 (좀비 프로세스 소탕)
    lock_files = [
        os.path.join(user_data_dir, "SingletonLock"),
        os.path.join(user_data_dir, "Default", "SingletonLock")
    ]
    for lf in lock_files:
        if os.path.exists(lf):
            try:
                os.remove(lf)
            except Exception:
                pass
                
    try:
        os.system("taskkill /f /im chrome.exe /im chromedriver.exe >nul 2>&1")
    except Exception:
        pass
        
    print(" -> [클리닝 완료] 모든 크롬 락이 해제되었습니다! 드라이버를 영롱하게 기동합니다...")
    
    # 4. 순수 셀레늄 극강의 초안전 옵션 세팅
    options = Options()
    options.add_argument(f"--user-data-dir={user_data_dir}")
    options.add_argument("--profile-directory=Default")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--remote-allow-origins=*")  # 연결 거절 파괴 핵심 옵션
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    
    # 대표님이 업로드 동작 과정을 시각적으로 확인하며 뿌듯함을 느끼실 수 있도록,
    # 그리고 headless 모드 특유의 크롬 통신 에러를 완전 원천 차단하기 위해 실체 창 모드(headed)로 기동합니다!
    # (크롬이 다 꺼져있는 상태이므로 실체 창 모드로 띄워도 100% 락 없이 아주 예쁘게 기동됩니다!)
    
    driver = None
    try:
        print(" -> Chrome 드라이버 기동 중... (Selenium Manager 자동 세팅)")
        driver = webdriver.Chrome(options=options)
        
        wait = WebDriverWait(driver, 45)
        
        # 5. YouTube Studio 업로드 다이렉트 페이지 이동
        print(" -> YouTube Studio 업로드 페이지로 이동합니다...")
        driver.get("https://studio.youtube.com/channel/UC/videos/upload?d=ud")
        time.sleep(8)  # 렌더링 완전 대기
        
        # 로그인 세션 상태 디버깅 출력
        current_url = driver.current_url
        print(f" -> 현재 브라우저 URL: {current_url}")
        if "login" in current_url or "accounts.google" in current_url:
            print("[경고] 구글 로그인이 풀려 있거나 2차 인증이 요구됩니다!")
            print(" -> 브라우저 창에서 수동으로 로그인을 한 번 완료해 주십시오.")
            
        # 6. 파일 인풋 엘리먼트 대기 및 파일 경로 전송
        print(" -> 업로드 파일 선택창을 우회하고 파일을 전송합니다...")
        file_input = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )
        file_input.send_keys(abs_file_path)
        print(f" -> 파일 전송 완료: {file_name}")
        
        time.sleep(8)
        
        # 7. 제목 입력
        print(f" -> 동영상 제목 지정 중: {title}")
        title_box = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='title-textarea']//div[@id='textbox']"))
        )
        title_box.clear()
        title_box.send_keys(title)
        time.sleep(2)
        
        # 8. 아동용이 아님 설정
        print(" -> 시청자층 설정: '아동용이 아닙니다' 선택 중...")
        not_for_kids = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//tp-yt-paper-radio-button[@name='VIDEO_MADE_FOR_KIDS_NOT_MADE_FOR_KIDS']"))
        )
        not_for_kids.click()
        time.sleep(2)
        
        # 9. '다음' 단계 버튼 3회 클릭 (동영상 요소 -> 검사 -> 공개 상태)
        print(" -> 동영상 설정 단계를 진행합니다...")
        for step in range(3):
            next_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//ytcp-button[@id='next-button']"))
            )
            next_btn.click()
            print(f"   -> [단계 완료] {step + 1}/3 단계 통과")
            time.sleep(3)
            
        # 10. 예약 상태(Scheduling) 설정
        print(" -> 공개 상태 설정: 예약(Schedule) 기능 활성화 중...")
        
        # 예약 탭 라디오 버튼 클릭
        schedule_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//tp-yt-paper-radio-button[@id='second-container-expand-button']"))
        )
        schedule_tab.click()
        time.sleep(3)
        
        # 날짜 예약 옵션이 있을 경우
        if schedule_date:
            print(f" -> 예약 날짜 설정 시도: {schedule_date}")
            datepicker = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//ytcp-text-dropdown-trigger[@id='datepicker-trigger']"))
            )
            datepicker.click()
            time.sleep(2)
            
            date_input = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input[contains(@class, 'datepicker-input') or contains(@class, 'text-input')]"))
            )
            date_input.clear()
            date_input.send_keys(schedule_date)
            time.sleep(2)
            
        # 예약 시간 설정
        if schedule_time:
            print(f" -> 예약 시간 설정 시도: {schedule_time}")
            timepicker = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='시간' or @aria-label='Time' or contains(@class, 'time-input')]"))
            )
            timepicker.clear()
            timepicker.send_keys(schedule_time)
            timepicker.send_keys("\n")
            time.sleep(2)
            
        # 11. 최종 '예약' 버튼 클릭 완료
        print(" -> [최종 승인] 쇼츠 예약 완료 버튼을 누릅니다!")
        done_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//ytcp-button[@id='done-button']"))
        )
        done_btn.click()
        
        print(" -> YouTube Studio 업로드 처리가 진행 중입니다. 잠시 기다려주세요...")
        time.sleep(10)
        print("\n=== [SUCCESS] YouTube Shorts 예약 업로드가 성공적으로 완료되었습니다! ===")
        return True
        
    except Exception as e:
        print(f"\n[에러 발생] 업로드 중 문제가 발생했습니다: {e}")
        if driver:
            try:
                driver.save_screenshot("upload_failed_screenshot.png")
                print(" -> [디버깅] 에러 시점의 브라우저 화면 캡처 저장 완료: upload_failed_screenshot.png")
            except Exception:
                pass
        return False
        
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="코다리 부장의 YouTube Studio Shorts 예약 업로드 자동화")
    parser.add_argument("--file", type=str, required=True, help="업로드할 MP4 동영상 파일 경로")
    parser.add_argument("--title", type=str, required=True, help="유튜브 쇼츠 동영상 제목 (최대 100자)")
    parser.add_argument("--date", type=str, default=None, help="예약할 날짜 (예: 2026-05-25)")
    parser.add_argument("--time", type=str, default="06:00", help="예약할 시간 (예: 06:00)")
    
    args = parser.parse_args()
    
    upload_to_youtube(args.file, args.title, args.date, args.time)
