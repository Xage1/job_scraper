import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from .models import Job
import time


def scrape_jobs(base_url, max_jobs=20):
    print("🔄 Starting scraper with pagination, retries, and BeautifulSoup")

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    job_links = []
    page = 1

    try:
        # Step 1: Get job links from paginated result pages
        while len(job_links) < max_jobs:
            paginated_url = f"{base_url}&page={page}"
            print(f"🌍 Visiting: {paginated_url}")
            driver.get(paginated_url)
            time.sleep(4)

            prerender_links = driver.find_elements(By.XPATH, "//link[@rel='prerender']")
            if not prerender_links:
                print("⚠️ No more job links found. Stopping.")
                break

            page_links = [link.get_attribute("href") for link in prerender_links]
            job_links.extend(page_links)
            if len(page_links) == 0:
                break

            page += 1

        driver.quit()
        print(f"🔗 Collected {len(job_links)} job URLs")

        # Step 2: Scrape each job detail using requests + BeautifulSoup
        for link in job_links[:max_jobs]:
            print(f"🔎 Scraping job: {link}")

            success = False
            for attempt in range(3):  # Retry up to 3 times
                try:
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                    }
                    response = requests.get(link, headers=headers, timeout=15)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.text, "html.parser")

                        title = soup.find("h1").get_text(strip=True) if soup.find("h1") else "N/A"
                        company_tag = soup.find(attrs={"data-testid": "company-name"})
                        company = company_tag.get_text(strip=True) if company_tag else "N/A"
                        desc_tag = soup.find(attrs={"data-testid": "job-description"})
                        description = desc_tag.get_text(strip=True)[:500] if desc_tag else "No description available."

                        print(f"✅ Scraped: {title} | {company}")

                        if not Job.objects.filter(title=title, company=company).exists():
                            Job.objects.create(
                                title=title,
                                company=company,
                                location="Nairobi",  # Default fallback
                                description=description,
                                source_url=link
                            )
                            print("📝 Job saved to DB")
                        success = True
                        break
                    else:
                        print(f"⚠️ Attempt {attempt+1}: Failed to fetch {link} — Status code: {response.status_code}")
                except Exception as e:
                    print(f"❌ Attempt {attempt+1}: Error scraping {link} → {e}")

            if not success:
                print(f"⛔ Failed all 3 attempts: {link}")

    except Exception as e:
        print(f"❌ Global error during scraping: {e}")

    finally:
        print("🚪 Done scraping.")