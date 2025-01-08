# Bing Points Automater

An automation script that performs Bing searches to help accumulate Microsoft Rewards points.

## Features
- Works on both Windows and macOS
- Uses existing Microsoft Edge profile
- Configurable delay between searches
- Random search term generation
- Automatic profile path detection

## Requirements
- Python 3.x
- Selenium
- Microsoft Edge browser
- Microsoft Edge WebDriver (place in project directory)

## Usage
1. Setup a virtual environment: `python3 -m venv venv`
2. Activate the virtual environment: `source venv/bin/activate`
3. Install requirements: `pip install -r requirements.txt`
4. Place appropriate Edge WebDriver in project directory:
   - Windows: `msedgedriver.exe`
   - macOS: `msedgedriver`
5. Kill all Edge processes: `taskkill /IM msedge.exe /F` (Only on Windows)
6. Run the script: `python auto-searcher.py`

## Author
Created by Krishna Teja Mekala

GitHub: https://github.com/krishna18developer

LinkedIn: https://www.linkedin.com/in/krishna18developer