from django.shortcuts import render
def landing_pageView(request):
    return render(request,'landing_page.html')