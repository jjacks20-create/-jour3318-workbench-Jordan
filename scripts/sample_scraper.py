"""
JOUR 3318: Sample Ethical Web Scraper Template
Phase 3: Computational Journalism & Data Extraction

Best Practices:
1. Always check robots.txt before scraping.
2. Identify yourself via a respectful User-Agent string.
3. Include time.sleep() delays between requests to avoid overloading servers.
4. Save raw extracted HTML or CSV with cryptographic hash for chain of custody.
"""

import time
import hashlib
import requests
from bs4 import BeautifulSoup
import pandas as pd


def fetch_page(url: str, user_agent: str = "JOUR3318-Student-Investigator/1.0") -> str:
    """Fetch webpage content respectfully with custom User-Agent and delay."""
    headers = {"User-Agent": user_agent}
    print(f"[*] Requesting: {url}")
    
    # Throttle requests: 2-second polite delay
    time.sleep(2)
    
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.text


def calculate_sha256(content: str) -> str:
    """Generate SHA-256 hash of raw data for evidentiary chain of custody."""
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def parse_records(html_content: str):
    """Example parsing logic using BeautifulSoup."""
    soup = BeautifulSoup(html_content, "html.parser")
    records = []

    # Example selector (customize for your target registry)
    # for item in soup.select(".record-item"):
    #     records.append({
    #         "title": item.select_one(".title").get_text(strip=True),
    #         "date": item.select_one(".date").get_text(strip=True),
    #     })

    return records


if __name__ == "__main__":
    test_url = "https://example.com"
    
    try:
        raw_html = fetch_page(test_url)
        content_hash = calculate_sha256(raw_html)
        print(f"[+] Successfully fetched content. Evidence Hash (SHA-256): {content_hash}")
        
        data = parse_records(raw_html)
        # df = pd.DataFrame(data)
        # df.to_csv("extracted_evidence.csv", index=False)
        print(f"[+] Parsed {len(data)} records.")
    except Exception as e:
        print(f"[-] Scraping error: {e}")
