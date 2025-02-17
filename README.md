# Browser Agent

A Python-based browser automation agent that can take natural language commands to navigate websites, extract data, and present results in a clean web interface.

## Features

* Takes natural language commands
* Navigates websites automatically
* Extracts and presents data cleanly
* Saves hours of manual browsing

## Tech Stack

* Backend: Python & Flask
* Browser Automation: Playwright
* Frontend: HTML/CSS
* Development Environment: Cursor

## Prerequisites

* Python 3.9+
* pip (Python package manager)
* A modern web browser (Firefox recommended)

## Installation

1. Clone the repository:
```bash
git clone [your-repo-url]
cd browser_agent
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Install Playwright browsers:
```bash
python3 -m playwright install firefox
```

## Project Structure

```
browser_agent/
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── agent.py
├── app.py
└── requirements.txt
```

## Usage

1. Start the application:
```bash
python3 app.py
```

2. Open your web browser and navigate to `http://localhost:5000`

3. Enter a command in the prompt box. For example:
   ```
   go to amazon.com and type computer, show me the first five results
   ```

4. The agent will:
   - Navigate to the specified website
   - Perform the requested actions
   - Extract and display the results

## Example Commands

Currently supported commands:
- Amazon product search and result extraction
- More commands coming soon!

## Troubleshooting

Common issues and solutions:

1. Browser launch fails:
   - Try using Firefox instead of Chromium
   - Clear Playwright browser cache: `rm -rf ~/Library/Caches/ms-playwright/`
   - Reinstall browsers: `python3 -m playwright install`

2. Timeout errors:
   - Check your internet connection
   - The site might be blocking automated access
   - Try increasing the timeout values in the code

## Contributing

Contributions are welcome! Feel free to:
- Add support for new websites
- Improve error handling
- Enhance the user interface
- Add new features


## Acknowledgments

- Built with [Cursor](https://cursor.so/)
- Powered by [Playwright](https://playwright.dev/)
- Flask web framework
