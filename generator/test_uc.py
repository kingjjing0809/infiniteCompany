import os
import time
import undetected_chromedriver as uc

def test_download():
    print("Testing undetected-chromedriver download...")
    
    # Create target directory
    download_dir = os.path.abspath("assets/bg_video")
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
        
    options = uc.ChromeOptions()
    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)
    
    # Run headlessly
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    
    driver = uc.Chrome(options=options, version_main=148)
    try:
        url = "https://www.pexels.com/download/videos/853889"
        driver.get(url)
        print("Navigation complete, waiting for download...")
        
        # Monitor directory for 15 seconds
        for i in range(15):
            files = os.listdir(download_dir)
            print(f"Files in directory: {files}")
            mp4_files = [f for f in files if f.endswith(".mp4")]
            crdownload_files = [f for f in files if f.endswith(".crdownload")]
            if mp4_files and not crdownload_files:
                print("Download successful!")
                break
            time.sleep(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_download()
