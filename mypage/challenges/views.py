from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None,
}

# Create your views here.

# def january(request):
#     return HttpResponse("Eat no meat for the entire month!")

# def february(request):
#     return HttpResponse("Walk for at least 20 minutes every day!")

# def march(request):
#     return HttpResponse("Learn Django for at least 20 minutes every day!")

def index(request):
    # list_items = ""
    months = list(monthly_challenges.keys())
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month_challenge", args=[month])
    #     list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"
    # response_data = f"<ul>{list_items}</ul>"
    # # response_data = """
    # #     <ul>
    # #         <li><a href="/challenges/june">6</a></li>
    # #     </ul>
    # # """
    # return HttpResponse(response_data)
    return render(request, "challenges/index.html",{
        "months": months
    })

def month_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month") 

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # challenge/june
    return HttpResponseRedirect(redirect_path)

def month_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize(),
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        # response = render_to_string("404.html")
        # return HttpResponseNotFound(response) 
        raise Http404()
    # if month == 'january':
    #     challenge_text = 'Eat no meat for the entire month!'
    # elif month == 'february':
    #     challenge_text = 'Walk for at least 20 minutes every day!'
    # elif month == 'march':
    #     challenge_text = 'Learn Django for at least 20 minutes every day!'
    # else:
    #     return HttpResponseNotFound("This is month is not supported!")