# Phisher.AI

## Chrome Extension for Detecting Phishing Emails

### Table of Contents

1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [Components](#components)
4. [Usage](#usage)
   - [Set Up the Flask API](#set-up-the-flask-api)
   - [Load Extension in Chrome](#load-extension-in-chrome)
   - [Test the Extension](#test-the-extension)
5. [Additional Notes](#additional-notes)
   - [Important Note for Contribution](#important-note-for-contribution)
6. [Contributing](#contributing)
7. [License](#license)

### Overview

This project provides a Chrome extension that leverages a machine learning model to detect phishing emails. The extension communicates with a Flask API hosted on the backend, which utilizes a pre-trained model for predicting the legitimacy of emails.

### Project Structure

```
- Extension
  - assets
  - popup
    - index.html
    - script.js
    - style.css
  - background.js
  - content.js
  - manifest.json
- SpamAI
  - dataset.csv
  - model.py
  - server.py
  - TrainedModel.pkl
  - Vectorizer.pkl
- SpamAI-v2
  - labels
  - model.h5
  - model.py
  - server.py
- Project-Presentation.pptx
- requirements.txt
```

### Components

- **Extension**: The Chrome extension files responsible for the user interface and interaction with the backend.

  - `assets`: Contains images or other assets used by the extension.
  - `popup`: HTML, JavaScript, and CSS files for the extension's popup.
  - `background.js`: JavaScript code running in the background.
  - `content.js`: JavaScript code injected into web pages.
  - `manifest.json`: Manifest file specifying extension details.

- **SpamAI**: Contains files related to the Flask API and the machine learning model for detecting phishing emails.

  - `dataset.csv`: Dataset used for training the model.
  - `model.py`: Script for training the machine learning model.
  - `server.py`: Flask API serving predictions to the extension.
  - `TrainedModel.pkl`: Pre-trained machine learning model.
  - `Vectorizer.pkl`: Vectorizer used for feature transformation.

- **SpamAI-v2**: An updated version of the SpamAI model with additional features or improvements.

### Usage

#### Set Up the Flask API

1. Navigate to the `SpamAI` directory.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Flask server: `python server.py`.

#### Load Extension in Chrome

1. Open Chrome and go to `chrome://extensions/`.
2. Enable "Developer mode" and click "Load unpacked".
3. Select the `Extension` directory.

#### Test the Extension

- Open an email or web page and use the extension's popup to analyze the content.


### Contributing

> [!Important]
> If you'd like to contribute to this project, please follow the standard GitHub workflow:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

---
