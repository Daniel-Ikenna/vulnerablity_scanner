## Vulnerability Scanner

This Python vulnerability scanner is designed to find potential security weaknesses in a web application. Specifically, it can identify Cross-Site Scripting (XSS) vulnerabilities in URLs and HTML forms by crawling the target URL, extracting forms, and testing for XSS injections.

### Features

- **Crawler**: Recursively discovers and records links within the target website.
- **Form Extraction**: Detects forms on each crawled page to locate input points.
- **XSS Testing**: Checks URLs and forms for XSS vulnerabilities by injecting a test script.
- **Session Handling**: Supports authentication sessions to access pages that require login.

### How It Works

The scanner starts by crawling through the website's pages and extracting any links and forms. It then performs an XSS vulnerability test by injecting a small test script into each form and link parameter to detect if a script can be executed.

### Scripts Overview

1. **`Scanner.py`**: Contains the `Scanner` class with methods for crawling, form extraction, XSS testing, and form submission.
2. **`vulnerability_scanner.py`**: Main script that sets up the target URL, login credentials, and scanner instance to run the XSS tests.

### Usage

1. **Configure Target URL and Links to Ignore**  
   Update `target_url` and `links_to_ignore` with the target application URL and any specific links to ignore during scanning.

   ```python
   target_url = "http://192.168.**.**/dvwa/"
   links_to_ignore = ["http://192.168.**.**/dvwa/logout.php"]
   ```

2. **Run the Script**
   ```bash
   python vulnerability_scanner.py
   ```

### Requirements

- **Python 3.x**
- **Requests Library**: `pip install requests`
- **BeautifulSoup**: `pip install beautifulsoup4`

### Example

The scanner will output results for each form and URL it tests:
```plaintext
[+] Testing form in http://192.168.**.**/dvwa/page
[***] XSS discovered in http://192.168.**.**/dvwa/page in the following form
<form>...</form>
[+] Testing http://192.168.**.**/dvwa/page?id=1
[***] Discovered XSS in http://192.168.**.**/dvwa/page?id=1
```

### Important Note

This script is for **authorized penetration testing** or **self-assessment only**. Unauthorized use against systems is illegal and may violate ethical and legal standards.

### Authors

- [Zaid Sabih](https://ie.linkedin.com/in/zaid-sabih-al-quraishi-5444a6127)
- [Uzoeshi Daniel](https://www.linkedin.com/in/daniel-ikenna-33b709235)
