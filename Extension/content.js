chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    console.log("Ge")
    let selectedText = document.body.innerText
    let message = {
      text: selectedText
    };
    console.log(selectedText);
    sendResponse(message);
  }
);