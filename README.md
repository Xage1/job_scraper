# 🚀 Job Scraper (Kenya Edition) 🌍  
A Django + Selenium + BeautifulSoup powered web app that scrapes job listings from top Kenyan job boards (starting with [BrighterMonday](https://www.brightermonday.co.ke)), stores them in a database, and lets you search, manage, and export them — all from a clean web interface.

---

## 🎯 Project Goal

Build a smart, automated job scraper dashboard that:

✅ Accepts job search URLs (e.g. BrighterMonday, MyJobMag)  
✅ Scrapes jobs using dynamic browser automation  
✅ Stores them in a structured backend  
✅ Makes them searchable, manageable, and exportable  

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Scraper**: Selenium WebDriver + BeautifulSoup + Requests
- **Database**: SQLite (Dev) | PostgreSQL (Ready for prod)
- **Frontend**: Django Templates (light HTML)
- **Dev Tools**: VS Code, ChromeDriver, pipenv/venv

---

## 🧠 Core Features

### 🧾 User Input  
- Paste job search URL (e.g. `https://www.brightermonday.co.ke/jobs?q=python`)
- Select how many jobs to scrape

### 🤖 Smart Web Scraper  
- Handles JavaScript-rendered content with Selenium
- Supports pagination (page 1, 2, 3…)
- Scrapes:
  - ✅ Job Title  
  - ✅ Company  
  - ✅ Job Description  
  - ✅ Link to original job  
  - ✅ Location (static fallback for now: `Nairobi`)

### 🔁 Retry Logic  
- 3 retry attempts per job URL  
- Continues scraping even if some fail

### 📤 Dashboard  
- Lists all saved jobs  
- Clean search & display  
- Delete individual entries  
- Ready to expand into filters/tags (remote, internship, etc.)

### 🧹 Data Cleanup  
- Prevents duplicates based on `title + company`

### 📦 Export (Coming Soon)  
- CSV export for downloading scraped results

### 🧪 Tested & Optimized  
- Handles dynamic content and timeouts  
- Logs each step of the process
- Saves failed HTML files for debugging (`scraped_page.html`)

---

## 📷 Screenshots

> _Add screenshots of form submission + dashboard view here if available_

---

## 🚀 How It Works (Behind the Scenes)

1. **User submits**: job search URL + count  
2. **Selenium loads**: the job board page in headless Chrome  
3. **Selenium scrapes**: `<link rel="prerender">` elements (actual job URLs)  
4. **Requests + BS4**: fetch and parse each job’s HTML  
5. **Django saves**: valid, deduplicated jobs to the DB  
6. **View**: All jobs in `/jobs/` dashboard

---

## 🗺️ Planned Features

- [ ] 🌍 Multi-platform support (e.g. MyJobMag, JobsKenya)
- [ ] 📦 CSV export button
- [ ] 🧠 Auto-tagging (Remote, Contract, Internship)
- [ ] 📧 Email scraped jobs to yourself
- [ ] ⏱️ Scheduled scraping via `cron` or Celery
- [ ] 🕵️‍♀️ Full-text search on description

---

## 🧑‍💻 How to Run It Locally

```bash
# 1. Clone the repo
git clone https://github.com/your-username/job-scraper.git
cd job-scraper

# 2. Create & activate a virtual environment
python -m venv venv
venv\Scripts\activate    # On Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Start the server
python manage.py runserver

# 6. Open the app
Visit http://127.0.0.1:8000/


🤝 Author
Kenneth Kiarie Muketha
📫 kennethkiarie555@gmail.com
📞 +254 746 155 994
🔗 LinkedIn

📄 License
MIT — open for use and contribution.
