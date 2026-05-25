// Open side panel on extension icon click
chrome.sidePanel
  .setPanelBehavior({ openPanelOnActionClick: true })
  .catch((error) => console.error(error));

// Listen for tab updates and notify sidepanel
chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.status === 'complete' && tab.url) {
    chrome.runtime.sendMessage({
      type: 'TAB_UPDATED',
      tab: tab
    }).catch(() => {
      // Ignore error if sidepanel is not open
    });
  }
});

// Listen for active tab change and notify sidepanel
chrome.tabs.onActivated.addListener((activeInfo) => {
  chrome.tabs.get(activeInfo.tabId, (tab) => {
    if (tab && tab.url) {
      chrome.runtime.sendMessage({
        type: 'TAB_UPDATED',
        tab: tab
      }).catch(() => {
        // Ignore error if sidepanel is not open
      });
    }
  });
});
