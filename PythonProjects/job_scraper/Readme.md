# Job Scraper

Web scraper that extracts job listings and saves to CSV.

## Features

- ✅ Scrapes job listings from websites
- ✅ Filters by job title keyword
- ✅ Saves results to CSV
- ✅ Error handling for failed requests

## Usage

```bash
python job_scraper.py
```

## Technologies

- Python 3
- BeautifulSoup4 (HTML parsing)
- Requests (HTTP)
- CSV (data export)

## What I Learned (Day 4)

- Web scraping with BeautifulSoup
- HTTP requests with headers
- CSS selectors for data extraction
- CSV file writing
- List comprehensions for filtering

## Sample Output

```
🕷️  JOB SCRAPER
==================
Enter job title to search: Python
🔍 Found 5 jobs matching 'Python'

1. Senior Python Developer
   🏢 Company: TechCorp
   📍 Location: Remote
   📅 Posted: 2024-12-15
...
```

## Future Improvements

- [ ] Scrape multiple pages
- [ ] Add email notifications
- [ ] Support more job sites
- [ ] Database storage
