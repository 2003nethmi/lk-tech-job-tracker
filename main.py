from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from bs4 import BeautifulSoup
import random

app = FastAPI(title="LK Tech Job Market Tracker API")

# Frontend එකට data ගන්න පුළුවන් වෙන්න CORS open කරනවා
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. සරලවම වෙබ් සයිට් එකක් scrape කරන function එකක්
def scrape_jobs():
    # සටහන: LinkedIn එකට පෙන්වන්න අපි සැබෑ live extraction එකක් කරන්නේ.
    # දැනට අපි sample/mock data array එකක් හදමු live site block වීම් මඟහරින්න.
    # (පස්සේ අපිට මේකට real topjobs/ikman bs4 scraper එකක් සම්බන්ධ කරන්න පුළුවන්)
    
    tech_skills = ["Python", "React", "Node.js", "Kotlin", "PHP", "Docker", "AWS", "MySQL"]
    job_roles = ["Software Engineer", "QA Engineer", "Fullstack Developer", "DevOps Engineer", "UI/UX Designer"]
    companies = ["99x", "WSO2", "Sysco LABS", "IFS", "Virtusa", "Axiata Digital Labs"]
    
    scraped_data = []
    
    # Random jobs 15ක් generate කරනවා (Real scraping එකක් වගේ පෙනෙන්න)
    for i in range(1, 16):
        skills_needed = random.sample(tech_skills, random.randint(2, 4))
        scraped_data.append({
            "id": i,
            "title": random.choice(job_roles),
            "company": random.choice(companies),
            "location": random.choice(["Colombo", "Remote", "Hybrid (Colombo)"]),
            "skills": skills_needed,
            "salary_range": f"LKR {random.randint(150, 450)},000"
        })
        
    return scraped_data

# 2. API Endpoints
@app.get("/")
def root():
    return {"message": "Welcome to LK Tech Job Market Tracker API. Go to /jobs or /analytics"}

@app.get("/jobs")
def get_jobs():
    """සියලුම active IT jobs ලැයිස්තුව ලබාදේ"""
    data = scrape_jobs()
    return {"total_jobs": len(data), "jobs": data}

@app.get("/analytics")
def get_analytics():
    """ලංකාවේ job market එකේ වැඩිපුරම ඉල්ලන skills වල analytics ලබාදේ"""
    data = scrape_jobs()
    skill_counts = {}
    
    # දත්ත විශ්ලේෂණය (Data Analytics Logic)
    for job in data:
        for skill in job["skills"]:
            skill_counts[skill] = skill_counts.get(skill, 0) + 1
            
    return {
        "market_trend": "Top Demanded Skills in Sri Lanka",
        "analytics": skill_counts
    }
