from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Job
from .scraper import scrape_jobs

def job_form(request):
    if request.method == "POST":
        url = request.POST.get("url")
        count = int(request.POST.get("count", 10))
        results = scrape_jobs(url, count)
        return redirect('job_list')
    return render(request, "scraper/form.html")

def job_list(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, "scraper/job_list.html", {"jobs": jobs})

