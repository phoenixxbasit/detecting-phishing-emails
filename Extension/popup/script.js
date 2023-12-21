const checkScoreButton = document.getElementById("check-score");
const scoreHeading = document.querySelector(".scoreheading");
const scoreparagraph = document.querySelectorAll(".scoreparagraph")[1];

const execScript = async () => {
  await chrome.tabs.executeScript(
    { code: "document.body.innerText;" },
    function (result) {
      const text = JSON.stringify(result[0]);
      console.log(text);
      processText(text);
    }
  );
};

const getCurrentTab = () => {
  return new Promise((resolve, reject) => {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      var currentTab = tabs[0];
      resolve(currentTab.url);
    });
  });
};


const makeServerReq = async (text) => {
  // const response = await fetch(`http://127.0.0.1:5000/predict?q="${Text}"`);
  try {
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: text }),
    });

    const scoredata = await response.json();
    console.log(scoredata.prediction);
    return scoredata;
  } catch (error) {
    console.error("Error:", error);
  }
};

const processText = async (text) => {
  const currentTabUrl = await getCurrentTab();
  if (
    currentTabUrl.startsWith("https://mail.google.com") ||
    currentTabUrl.startsWith("https://outlook")
  ) {
    const score = await makeServerReq(text);
    scoreHeading.textContent = `${score.prediction.toFixed(3)}`;
    if (score.prediction.toFixed(3) > 0.5) {
      scoreparagraph.textContent = "Probably Looks Fishy😱";
    } else {
      scoreparagraph.textContent = "Probably Looks Safe 😀";
    }
  } else {
    scoreHeading.textContent = "0.00";
    scoreparagraph.textContent = "Current Url Not Supported"
  }
};

checkScoreButton.addEventListener("click", execScript);
