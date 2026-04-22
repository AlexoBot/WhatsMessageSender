# WhatsApp Message Scheduler

A Python-based automation tool for scheduling and sending WhatsApp messages and attachments using Selenium WebDriver. Designed for daily planning document distribution with built-in testing and anti-spam measures.

## Overview

This project automates the process of sending WhatsApp messages with document attachments at scheduled times. It was created to handle daily planning document distribution while avoiding WhatsApp's spam detection mechanisms through strategic timing and testing phases.

## Features

- **Automated Message Sending**: Send text messages to WhatsApp groups or contacts
- **Document Attachments**: Attach and send Excel files (.xlsx)
- **Template-Based Document Generation**: Automatically generate daily planning documents from templates
- **Chrome Profile Management**: Use dedicated Chrome profiles to avoid QR code scanning on each run
- **Built-in Testing**: Includes test phases to verify functionality before sending production messages
- **Anti-Spam Timing**: Implements wait timers between operations to prevent detection
- **Windows Task Scheduler Integration**: Designed for automated execution via Windows Task Scheduler

## Project Structure

```
WhatsMessageSender/
├── .env                    # User-specific environment variables
├── .env.defaults          # Default environment variables and XPaths
├── Functions.py           # Core utility functions
├── Main.py                # Main execution script
├── setup_scheduler.py     # Script to create BAT file and configure Task Scheduler
├── run_planner.bat        # Auto-generated BAT file (created by setup_scheduler.py)
└── README.MD              # This documentation
```

## Dependencies

- Python 3.7+
- Selenium WebDriver
- Chrome for Testing (latest version)
- ChromeDriver (matching Chrome for Testing version)
- openpyxl (for Excel file manipulation)
- python-dotenv (for environment variable management)

## Installation

1. **Install Python Dependencies**:
   ```bash
   pip install selenium openpyxl python-dotenv
   ```

2. **Download Chrome for Testing**:
   - Visit: https://googlechromelabs.github.io/chrome-for-testing/
   - Download the latest Chrome for Testing (chrome-win64.zip)
   - Download the matching ChromeDriver (chromedriver-win64.zip)
   - Extract both to a folder (e.g., `C:\ChromeForTestingPack\`)

3. **Set Up Chrome Profile**:
   - Create a new Chrome profile for WhatsApp automation
   - Open Chrome with the new profile and log into WhatsApp Web once
   - Note the profile directory path (usually `Profile 1`, `Profile 2`, etc.)

## Configuration

### Environment Variables

Create a `.env` file in the project root to override defaults:

```env
USERNAME = "YourUsername"
```

The `.env.defaults` file contains default paths and XPaths. Modify as needed for your system:

```env
PROFILENAME = "Profile 1"
CHROMETESTINGPATH = "C:\\ChromeForTestingPack\\chrome-win64\\chrome.exe"
CHROMEDRIVERPATH = "C:\\ChromeForTestingPack\\chromedriver-win64\\chromedriver.exe"
CHROMEUSERDIRPATH = "user-data-dir=C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\{profile_name}"

# WhatsApp Web XPaths (may need updates if WhatsApp changes UI)
SEARCHBOX = //div[@data-lexical-editor="true"][@class="x1hx0egp x6ikm8r x1odjw0f x6prxxf x1k6rcq7 x1whj5v"]
MESSAGEBOX = //div[@contenteditable="true"][@class="x1hx0egp x6ikm8r x1odjw0f x1k6rcq7 x6prxxf"]
ATTACHBUTTON = //div[@class="x100vrsf x1vqgdyp x78zum5 x6s0dn4 xpvyfi4"]
DOCUMENTBUTTON = //div[@class="x6s0dn4 xlr9sxt xvvg52n xwd4zgb xq8v1ta x78zum5 xu0aao5 xh8yej3"]
SENDATTACHMENT = //span[@data-icon="wds-ic-send-filled"][@aria-hidden="true"]
```

### Template Setup

1. Create a template Excel file named `DailyPlanning template.xlsx`
2. Place it in your configured template directory (defined by `ONEDRIVEPATH` in `.env` or `.env.defaults`)
3. The template should have placeholders for:
   - Date (cell B2)
   - Pending items (cell B12)
   - Follow-ups (cell B16)

## Workflow

The main workflow in `Main.py` follows these steps:

### 1. Initialization (0-25 seconds)
- Load environment variables
- Configure Chrome WebDriver with dedicated profile
- Launch WhatsApp Web and wait for loading

### 2. Document Generation (25-28 seconds)
- Generate daily planning document from template
- Update date and default content
- Save to target directory

### 3. Testing Phase (28-388 seconds)
- Wait 3 minutes to allow WhatsApp Web full loading
- Send test message to testing group
- Attach generated document
- Send confirmation message
- Wait additional 3 minutes 30 seconds

### 4. Production Phase (388-508 seconds)
- Send actual message to target group
- Attach generated document
- Wait 2 minutes for completion

### 5. Cleanup (508-511 seconds)
- Close browser
- Total execution time: ~8.5 minutes

## Usage

### Setting Up Automated Scheduling

```bash
python setup_scheduler.py
```

Follow the prompts to configure the daily execution time.

### Running the Main Script Manually

```bash
python Main.py
```

### Running Tests

```bash
python Functions.py
```

The test script runs a simplified version with shorter wait times for verification.

## Functions Reference

### Core Functions (Functions.py)

- **`WaitTimer(total_seconds)`**: Implements countdown timer with progress updates
- **`GeneratePlanning(template_path, file_path)`**: Creates daily planning document from template
- **`driverConfigure(user_dir_path, chrome_path, driver_path, profile_name)`**: Sets up Chrome WebDriver
- **`SearchGroupOrContact(driver, search_xpath, group_name)`**: Searches and selects WhatsApp group/contact
- **`SendMessage(driver, message_xpath, message)`**: Sends text message
- **`SendAttachment(driver, attach_xpath, doc_xpath, file_path, send_xpath)`**: Attaches and sends document

## Troubleshooting

### Common Issues

1. **XPath Errors**: WhatsApp UI changes may break XPaths. Update `.env.defaults` with current selectors.
2. **File Not Found**: Ensure template file exists and paths are correct.
3. **Chrome Profile Issues**: Verify profile directory and ensure WhatsApp is logged in.
4. **Driver Version Mismatch**: Ensure ChromeDriver matches Chrome for Testing version.

### Debugging

- Run `Functions.py` for isolated testing
- Check console output for detailed error messages
- Screenshots are automatically saved on attachment failures

## Security Notes

- Uses dedicated Chrome profile to avoid interfering with personal browsing
- Stores sensitive paths in environment variables
- Implements delays to avoid spam detection
- No credentials stored in code

## Future Enhancements

- Dynamic document templates
- Support for multiple file types (images, PDFs)
- Configurable recipient lists
- Web-based configuration interface
- Cross-platform support (Linux/Mac)

## License

This project is for personal use. Ensure compliance with WhatsApp's Terms of Service when automating interactions.