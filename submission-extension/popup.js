// Initialize button with user's preferred color
let createEntry = document.getElementById("createEntry");




chrome.storage.sync.get("color", ({ color }) => {
  createEntry.style.backgroundColor = color;
});

// When the button is clicked, inject setPageBackgroundColor into current page
createEntry.addEventListener("click", async () => {
    let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    chrome.storage.sync.set({ tab });
    let textElement = document.getElementById("text");
    let linkElement = document.getElementById("link");
    textElement.value = tab.title;
    linkElement.value = tab.url;
    
    // chrome.scripting.executeScript({
    //   target: { tabId: tab.id },
    //   function: setEntryData,
    // });
  });

function submitEntry(){
  console.log('hello')
}


  // // The body of this function will be executed as a content script inside the
  // // current page
  // function setEntryData() {
  //   console.log('hi')
  //   chrome.storage.sync.get("tab", ({ tab }) => {
      
  //     chrome.storage.sync.get("textElement", ({ textElement }) => {
  //       console.log(tab)
      
  //       console.log(textElement.value);
  //       textElement.value = "hi"
  //     //   document.body.style.backgroundColor = color;
  //     });
      
  //   //   document.body.style.backgroundColor = color;
  //   });
    
  //   // linkElement.value = tab.url;
  //   //   textElement.value = tab.title;
  // }

 