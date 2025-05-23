# RERA Odisha Project Scraper

This Python script uses Selenium to scrape details of the first 6 projects listed on the Odisha RERA website.

## Prerequisites

Before running the script, ensure you have the following installed:

1.  **Python 3.x**: Download from [python.org](https://www.python.org/downloads/).
2.  **Google Chrome Browser**: The script is designed to work with Chrome.
3.  **ChromeDriver**: Selenium requires a `webdriver` executable to control the browser.
    * **Automatic Installation (Recommended):** The `selenium` library often attempts to manage ChromeDriver automatically.
    * **Manual Installation (If automatic fails):**
        * Check your Chrome browser version (Go to Chrome Menu -> Help -> About Google Chrome).
        * Download the corresponding ChromeDriver from the official site: [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads).
        * Place the downloaded `chromedriver.exe` (Windows) or `chromedriver` (macOS/Linux) executable file in your system's PATH, or in the same directory as this Python script (`scrape_rera_projects.py`).

## Installation

1.  Clone or download this repository/folder to your local machine.
2.  Navigate to the project directory in your terminal or command prompt:
    ```bash
    cd your_project_folder
    ```
3.  Install the required Python libraries using pip:
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

1.  Ensure all prerequisites and installation steps are completed.
2.  From your terminal or command prompt, run the Python script:
    ```bash
    python project1.py
    ```

## Output

The script will:
* Print progress messages to the console.
* Create a CSV file named `first_6_projects.csv` in the same directory. This file will contain the scraped project name, RERA registration number, promoter's name, promoter's address, and GST number for the first 6 projects.

**Note on CSV Output:** The 'Promoters Address' field might contain commas and newlines. While it may appear unstructured in a basic text editor (like Notepad), it is correctly formatted according to CSV standards. It will display properly in spreadsheet software like Microsoft Excel, Google Sheets, or LibreOffice Calc.

---

Feel free to reach out if you have any questions!
