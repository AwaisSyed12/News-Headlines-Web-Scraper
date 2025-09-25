# News Headlines Web Scraper

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Requests](https://img.shields.io/badge/Requests-2.31+-green.svg)](https://docs.python-requests.org/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.12+-orange.svg)](https://www.crummy.com/software/BeautifulSoup/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A professional web scraper for extracting news headlines from public websites, built with Python using the `requests` and `BeautifulSoup` libraries. This project demonstrates ethical web scraping practices while automating data collection from news sources.

## 🎯 Project Overview

This web scraper showcases professional Python development practices for data collection from public websites. Built with ethical scraping principles, the application respects robots.txt files, implements rate limiting, and provides comprehensive error handling for reliable data extraction.

### ✨ Key Features

- **HTTP Requests**: Professional request handling with proper headers and session management
- **HTML Parsing**: Advanced BeautifulSoup parsing with multiple selector strategies  
- **Ethical Scraping**: Robots.txt compliance checking and rate limiting
- **Multiple Output Formats**: Save headlines to both TXT and CSV files
- **Error Handling**: Comprehensive exception handling and graceful failure recovery
- **Interactive Interface**: User-friendly CLI for URL selection and configuration
- **Professional Headers**: Proper User-Agent identification and request headers

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- Terminal/Command Prompt
- Internet connection for web requests

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AwaisSyed12/News-Headlines-Web-Scraper.git
   cd news-headlines-scraper
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the scraper:**
   ```bash
   python news_scraper.py
   ```

## 💻 Usage Examples

### Interactive Mode
```
🗞️  NEWS HEADLINE SCRAPER
========================
Professional web scraper following ethical practices

🎯 Available demo sites:
   1. Quotes to Scrape (Demo Site)
   2. Example News Site  
   3. Enter custom URL

Select an option (1-3): 1
```

### Example Output
```
🚀 Starting to scrape: http://quotes.toscrape.com/
============================================================
🤖 Robots.txt check for http://quotes.toscrape.com:
   ✅ Can fetch: True
   ⏱️  No crawl delay specified
🌐 Fetching: http://quotes.toscrape.com/
✅ Successfully fetched http://quotes.toscrape.com/ (Status: 200)
🔍 Parsing headlines using multiple strategies...
📊 Total unique headlines found: 10

📰 SCRAPED HEADLINES (Showing 3 of 10)
============================================================

1. Quote 1: "The world as we have created it is a process of our thinking..."
   📅 2025-09-25 09:30:15

2. Quote 2: "It is our choices, Harry, that show what we truly are..."
   📅 2025-09-25 09:30:15

3. Quote 3: "There are only two ways to live your life..."
   📅 2025-09-25 09:30:15
```

## 🏗️ Project Structure

```
News-Headlines-Web-Scraper/
│
├── news_scraper.py        # Main professional scraper
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── news_headlines.txt    # Output file (generated)
├── news_headlines.csv    # CSV output (generated)
└── screenshots/          # Demo screenshots
    ├── scraper-interface.png
    ├── output-example.png
    └── ethical-practices.png
```

## ⚙️ Technical Implementation

### Core Components

**NewsHeadlineScraper Class:**
```python
class NewsHeadlineScraper:
    def __init__(self, user_agent="NewsScraperBot/1.0")
    def check_robots_txt(self, base_url)
    def fetch_page(self, url, delay=1) 
    def parse_headlines(self, html_content, selectors=None)
    def scrape_news_site(self, url, custom_selectors=None)
    def save_headlines_txt(self, filename="news_headlines.txt")
    def save_headlines_csv(self, filename="news_headlines.csv")
```

### Ethical Scraping Features

| Feature | Implementation | Benefits |
|---------|----------------|----------|
| **Robots.txt Compliance** | Automatic robots.txt checking | Respects website policies |
| **Rate Limiting** | Configurable delays between requests | Prevents server overload |
| **Proper Headers** | Professional User-Agent identification | Transparent bot identification |
| **Error Handling** | Comprehensive exception management | Graceful failure recovery |
| **Session Management** | Persistent session with keep-alive | Efficient connection reuse |

### Parsing Strategies

The scraper uses multiple CSS selectors to find headlines:

```python
selectors = [
    'h1',              # Main headlines
    'h2',              # Secondary headlines  
    'h3',              # Tertiary headlines
    '.headline',       # Class-based selectors
    '.title',
    '.news-title',
    '.article-title',
    '[class*="headline"]',  # Partial class matches
    '[class*="title"]'
]
```

## 🛡️ Ethical Web Scraping Practices

### Legal and Ethical Compliance

- **Robots.txt Respect**: Always check and follow robots.txt directives
- **Rate Limiting**: Implement delays to avoid overwhelming servers
- **Proper Identification**: Use descriptive User-Agent strings
- **Terms of Service**: Respect website terms and conditions
- **Data Usage**: Use scraped data responsibly and ethically

### Best Practices Implemented

```python
# Professional headers
self.session.headers.update({
    'User-Agent': 'NewsScraperBot/1.0 (+Educational Purpose)',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive'
})

# Rate limiting
time.sleep(delay)  # Respectful delays between requests

# Robots.txt compliance
rp = RobotFileParser()
can_fetch = rp.can_fetch(user_agent, base_url)
```

## 📊 Output Formats

### TXT File Format
```
News Headlines Scraped on 2025-09-25 09:30:15
============================================================

1. Sample headline from news website
   Link: https://example.com/article1
   Found with: h2
   Scraped at: 2025-09-25 09:30:15

2. Another interesting news headline
   Link: https://example.com/article2
   Found with: .headline
   Scraped at: 2025-09-25 09:30:16
```

### CSV File Format
```csv
Index,Headline,Link,Selector,Timestamp
1,"Sample headline from news website","https://example.com/article1","h2","2025-09-25 09:30:15"
2,"Another interesting news headline","https://example.com/article2",".headline","2025-09-25 09:30:16"
```

## 🔧 Advanced Features

### Professional Enhancements

- **Multiple Selector Strategies**: Fallback selectors for different site structures
- **Duplicate Detection**: Automatic removal of duplicate headlines
- **Link Extraction**: Capture both headline text and associated URLs
- **Timestamp Tracking**: Record when each headline was scraped
- **Session Persistence**: Efficient connection reuse for multiple requests

### Error Handling

```python
try:
    response = self.session.get(url, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"❌ Error fetching {url}: {e}")
    return None
```

## 📈 Key Concepts Demonstrated

### Core Requirements Met ✅
- [x] Use requests to fetch HTML content
- [x] Use BeautifulSoup to parse HTML and extract headlines
- [x] Save extracted headlines to .txt file
- [x] Automate data collection from public websites

### Professional Enhancements ✅
- [x] Ethical scraping with robots.txt compliance
- [x] Rate limiting and respectful request patterns
- [x] Professional error handling and logging
- [x] Multiple output formats (TXT and CSV)
- [x] Interactive user interface with clear feedback
- [x] Session management and proper HTTP headers

## 🧪 Testing & Validation

### Safe Testing Sites
- **quotes.toscrape.com**: Educational scraping practice site
- **httpbin.org**: HTTP testing service
- **example.com**: Basic HTML structure testing

### Testing Scenarios
- ✅ Basic HTML parsing with standard selectors
- ✅ Error handling for unreachable websites  
- ✅ Robots.txt compliance verification
- ✅ Rate limiting effectiveness
- ✅ File output generation and formatting
- ✅ Duplicate headline detection and removal

## 🤝 Contributing

Contributions are welcome! Please follow ethical scraping guidelines:

1. **Respect robots.txt files** in all scraping activities
2. **Implement rate limiting** to avoid server overload  
3. **Use descriptive User-Agent strings** for transparency
4. **Test with safe, educational websites** like quotes.toscrape.com
5. **Document any new features** with clear ethical guidelines

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/EthicalFeature`)
3. Commit changes (`git commit -m 'Add ethical scraping feature'`)
4. Push to branch (`git push origin feature/EthicalFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Legal Disclaimer

This software is for educational and research purposes only. Users are responsible for:

- Checking and complying with website terms of service
- Respecting robots.txt files and scraping policies  
- Using scraped data in accordance with applicable laws
- Implementing appropriate rate limiting and ethical practices

The authors are not liable for any misuse of this software.

## 👤 Author

**Awais Syed**
- 🔗 GitHub: [@AwaisSyed12](https://github.com/AwaisSyed12)
- 📧 Email: awaissyed1212@gmail.com
- 💼 LinkedIn: [Awais Syed](https://linkedin.com/in/awais-syed-686b46376)

## 🙏 Acknowledgments

- Built as part of Python Developer technical assessment
- Demonstrates proficiency in web scraping and HTTP protocols
- Follows industry best practices for ethical data collection
- Thanks to the web scraping community for establishing ethical guidelines

## 📚 Learning Resources

- [Requests Documentation](https://docs.python-requests.org/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Robots.txt Specification](https://www.robotstxt.org/)
- [Ethical Web Scraping Guidelines](https://blog.apify.com/is-web-scraping-legal/)

---

⭐ **Star this repository if you found it helpful!**

🚀 **Ready to start ethical web scraping? Clone the repo and try the demo!**

**Remember: Always scrape responsibly and respect website policies! 🤖✨**
