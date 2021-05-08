let color = '#3aa757';

chrome.runtime.onInstalled.addListener(() => {
  chrome.storage.sync.set({ color });
  console.log('Default background color set to %cgreen', `color: ${color}`);
  
});

chrome.commands.onCommand.addListener(function (command) {
    switch (command) {
        case 'duplicate-tab':
            duplicateTab();
            break;
        default:
            console.log(`Command ${command} not found`);
    }
});

/**
* Gets the current active tab URL and opens a new tab with the same URL.
*/
function duplicateTab() {
    const query = { active: true, currentWindow: true };
    let [tab] = await chrome.tabs.query(query);
    chrome.scripting.executeScript({
        target: { tabId: tab.id },
        function: createEntry,
      });
}

function createEntry(){
    console.log("Creating entry...")
}