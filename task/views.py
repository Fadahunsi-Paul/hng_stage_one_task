from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from django.utils import timezone

# Create your views here.


def json_endpoint(request):
    #Query Parameters
    slack_name = request.GET.get('slack_name',"Fadahunsi Paul")

    #Weekday query Parameters
    current_weekday = datetime.now().strftime("%A")

    current_utc_time = datetime.utcnow().strftime("$Y-%m-%dT%H:%M:%SZ")

    #track queries
    track = request.GET.get('track','Backend')

    #File URL setup
    github_file_url = 'https://github.com/Fadahunsi-Paul/hng_stage_one_task/blob/main/task/views.py'

    #source code queries
    github_repo_url = 'https://github.com/Fadahunsi-Paul/hng_stage_one_task' 

    endpoint_response = {
        'slack_name':slack_name,
        'current_weekday':current_weekday,
        'current_utc_time':current_utc_time,
        'track':track,
        'github_file_url':github_file_url,
        'github_repo_url':github_repo_url,
        'status_code':200
    }

    return JsonResponse(endpoint_response)     