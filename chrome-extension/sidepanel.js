let currentTabInfo = null;

// UI 업데이트
function updateUI(tab) {
    if (!tab || !tab.url) return;
    
    // 크롬 내부 페이지 등에서는 비활성화
    if (tab.url.startsWith('chrome://') || tab.url.startsWith('edge://')) {
        document.getElementById('page-title').textContent = '지원되지 않는 페이지';
        document.getElementById('page-url').textContent = tab.url;
        document.getElementById('send-btn').disabled = true;
        document.getElementById('send-btn').style.opacity = '0.5';
        return;
    }
    
    document.getElementById('send-btn').disabled = false;
    document.getElementById('send-btn').style.opacity = '1';
    
    currentTabInfo = tab;
    document.getElementById('page-title').textContent = tab.title || 'No Title';
    document.getElementById('page-url').textContent = tab.url;
}

// 초기 로드 시 현재 탭 가져오기
async function init() {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    updateUI(tab);
}

// 탭 이동 또는 업데이트 감지
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.type === 'TAB_UPDATED' && message.tab) {
        chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
            if (tabs[0] && tabs[0].id === message.tab.id) {
                updateUI(message.tab);
            }
        });
    }
});

// 전송 버튼 이벤트
document.getElementById('send-btn').addEventListener('click', async () => {
    if (!currentTabInfo) return;

    const btn = document.getElementById('send-btn');
    const statusMsg = document.getElementById('status-message');

    // 로딩 상태 UI 처리
    btn.disabled = true;
    btn.textContent = '전송 중...';

    try {
        // 실제로는 여기서 안티그래비티 서버로 fetch 요청을 보냅니다.
        // 임시로 성공한 것처럼 Mocking 합니다.
        await new Promise(resolve => setTimeout(resolve, 800));

        statusMsg.textContent = '안티그래비티로 전송되었습니다! ✨';
        statusMsg.className = 'status success';
        
        // 3초 후 메시지 숨김
        setTimeout(() => {
            statusMsg.className = 'status hidden';
        }, 3000);
        
    } catch (error) {
        console.error('Failed to send:', error);
        statusMsg.textContent = '전송에 실패했습니다.';
        statusMsg.className = 'status error';
    } finally {
        btn.disabled = false;
        btn.textContent = '안티그래비티로 전송';
    }
});

// 스크립트 시작
document.addEventListener('DOMContentLoaded', init);
