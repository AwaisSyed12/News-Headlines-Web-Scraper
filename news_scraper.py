"""
News Headlines Web Scraper
==========================
A professional web scraper for extracting news headlines from public websites
Author: Awais Syed
Email: awaissyed1212@gmail.com
Features: HTTP requests, HTML parsing, file output, ethical scraping practices
"""

import requests
from bs4 import BeautifulSoup
import time
import csv
from datetime import datetime
from urllib.robotparser import RobotFileParser
from urllib.parse import urljoin, urlparse
import os
import sys

class NewsHeadlineScraper:

    def __init__(self, user_agent="NewsScraperBot/1.0 (+Educational Purpose)"):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        })
        self.headlines = []
        self.scraped_urls = set()

    def check_robots_txt(self, base_url):
        try:
            rp = RobotFileParser()
            robots_url = urljoin(base_url, '/robots.txt')
            rp.set_url(robots_url)
            rp.read()

            user_agent = self.session.headers.get('User-Agent', '*')
            can_fetch = rp.can_fetch(user_agent, base_url)

            # Get crawl delay if specified
            crawl_delay = rp.crawl_delay(user_agent)
            if crawl_delay is None:
                crawl_delay = rp.crawl_delay('*')

            print(f"🤖 Robots.txt check for {base_url}:")
            print(f"   ✅ Can fetch: {can_fetch}")
            print(f"   ⏱️  Crawl delay: {crawl_delay} seconds" if crawl_delay else "   ⏱️  No crawl delay specified")

            return can_fetch, crawl_delay or 1

        except Exception as e:
            print(f"⚠️ Warning: Could not check robots.txt: {e}")
            print("   Proceeding with caution (1 second delay)")
            return True, 1

    def fetch_page(self, url, delay=1):
        try:
            # Rate limiting - be respectful
            time.sleep(delay)

            print(f"🌐 Fetching: {url}")
            response = self.session.get(url, timeout=10)
            response.raise_for_status()

            print(f"✅ Successfully fetched {url} (Status: {response.status_code})")
            return response.text

        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching {url}: {e}")
            return None
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return None

    def parse_headlines(self, html_content, selectors=None):
        if not html_content:
            return []

        if selectors is None:
            selectors = [
                'h1',  
                'h2',   
                'h3',  
                '.headline',  
                '.title',
                '.news-title',
                '.article-title',
                '[class*="headline"]',  
                '[class*="title"]'
            ]

        soup = BeautifulSoup(html_content, 'html.parser')
        headlines = []

        print("🔍 Parsing headlines using multiple strategies...")

        for selector in selectors:
            try:
                elements = soup.select(selector)
                for element in elements:
                    text = element.get_text(strip=True)

                    if text and len(text) > 10 and len(text) < 200:
                        link_element = element.find('a') or element.find_parent('a')
                        link = link_element.get('href') if link_element else None

                        headline_data = {
                            'text': text,
                            'link': link,
                            'selector': selector,
                            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        }

                        if text not in [h['text'] for h in headlines]:
                            headlines.append(headline_data)

                if elements:
                    print(f"   📰 Found {len(elements)} elements with selector '{selector}'")

            except Exception as e:
                print(f"   ⚠️ Error with selector '{selector}': {e}")
                continue

        unique_headlines = []
        seen_texts = set()

        for headline in headlines:
            if headline['text'] not in seen_texts:
                unique_headlines.append(headline)
                seen_texts.add(headline['text'])

        print(f"📊 Total unique headlines found: {len(unique_headlines)}")
        return unique_headlines

    def scrape_news_site(self, url, custom_selectors=None):
        print(f"\n🚀 Starting to scrape: {url}")
        print("="*60)

        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

        can_fetch, delay = self.check_robots_txt(base_url)

        if not can_fetch:
            print(f"❌ Robots.txt disallows scraping {url}")
            print("   Respecting robots.txt and skipping this URL")
            return []

        html_content = self.fetch_page(url, delay)

        if not html_content:
            print(f"❌ Failed to fetch content from {url}")
            return []

        headlines = self.parse_headlines(html_content, custom_selectors)

        self.headlines.extend(headlines)
        self.scraped_urls.add(url)

        return headlines

    def save_headlines_txt(self, filename="news_headlines.txt"):
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(f"News Headlines Scraped on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write("="*60 + "\n\n")

                for i, headline in enumerate(self.headlines, 1):
                    file.write(f"{i}. {headline['text']}\n")
                    if headline['link']:
                        file.write(f"   Link: {headline['link']}\n")
                    file.write(f"   Found with: {headline['selector']}\n")
                    file.write(f"   Scraped at: {headline['timestamp']}\n\n")

                file.write("\n" + "="*60 + "\n")
                file.write(f"SUMMARY\n")
                file.write(f"Total Headlines: {len(self.headlines)}\n")
                file.write(f"URLs Scraped: {len(self.scraped_urls)}\n")
                file.write(f"Scraped URLs: {', '.join(self.scraped_urls)}\n")

            print(f"💾 Headlines saved to: {filename}")
            return True

        except Exception as e:
            print(f"❌ Error saving to {filename}: {e}")
            return False

    def save_headlines_csv(self, filename="news_headlines.csv"):
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)

                writer.writerow(['Index', 'Headline', 'Link', 'Selector', 'Timestamp'])

                for i, headline in enumerate(self.headlines, 1):
                    writer.writerow([
                        i,
                        headline['text'],
                        headline['link'] or 'N/A',
                        headline['selector'],
                        headline['timestamp']
                    ])

            print(f"📊 Headlines saved to CSV: {filename}")
            return True

        except Exception as e:
            print(f"❌ Error saving CSV {filename}: {e}")
            return False

    def display_headlines(self, limit=10):
        if not self.headlines:
            print("📭 No headlines found to display")
            return

        print(f"\n📰 SCRAPED HEADLINES (Showing {min(limit, len(self.headlines))} of {len(self.headlines)})")
        print("="*60)

        for i, headline in enumerate(self.headlines[:limit], 1):
            print(f"\n{i}. {headline['text']}")
            if headline['link']:
                print(f"   🔗 {headline['link']}")
            print(f"   📅 {headline['timestamp']}")

def main():
    print("🗞️  NEWS HEADLINE SCRAPER")
    print("========================")
    print("Professional web scraper following ethical practices")
    print()

    scraper = NewsHeadlineScraper()

    news_sites = [
        {
            'name': 'Quotes to Scrape (Demo Site)',
            'url': 'http://quotes.toscrape.com/',
            'selectors': ['.text']  
        },
        {
            'name': 'Example News Site',
            'url': 'https://example.com',
            'selectors': ['h1', 'h2', 'h3']
        }
    ]

    print("🎯 Available demo sites:")
    for i, site in enumerate(news_sites, 1):
        print(f"   {i}. {site['name']}")
    print("   3. Enter custom URL")

    try:
        choice = input("\nSelect an option (1-3): ").strip()

        if choice == "1":
            url = news_sites[0]['url']
            selectors = news_sites[0]['selectors']
            headlines = scraper.scrape_news_site(url, selectors)

        elif choice == "2":
            url = news_sites[1]['url']
            headlines = scraper.scrape_news_site(url)

        elif choice == "3":
            url = input("Enter news website URL: ").strip()
            if not url:
                print("❌ No URL provided")
                return

            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url

            headlines = scraper.scrape_news_site(url)

        else:
            print("❌ Invalid choice")
            return

        scraper.display_headlines()

        if scraper.headlines:
            save_files = input("\n💾 Save headlines to files? (y/n): ").strip().lower()
            if save_files in ['y', 'yes']:
                scraper.save_headlines_txt()
                scraper.save_headlines_csv()
                print("\n✨ Scraping completed successfully!")
        else:
            print("\n📭 No headlines were found to save")

    except KeyboardInterrupt:
        print("\n\n⏹️  Scraping interrupted by user")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
