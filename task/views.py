from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
import datetime
from django.utils import timezone

# Create your views here.

class first_stage(APIView):
    def get(self,request): 
        #Query Parameters
        slack_name = request.query_params.get('slack_name',"Fadahunsi_Paul")

        #Weekday query Parameters
        current_weekday = datetime.datetime.now().strftime("%A")

        current_utc_time = timezone.now()
        utc_time_format = "%Y-%m-%dT%H:%M:%SZ"

        #track queries
        track = request.query_params.get('track','backend')

        #File URL setup
        github_file_url = 'https://github.com/Fadahunsi-Paul/hng_stage_one_task/blob/main/task/views.py'

        #source code queries
        github_repo_url = 'https://github.com/Fadahunsi-Paul/hng_stage_one_task' 

        endpoint_response = {
            'slack_name':slack_name,
            'current_weekday':current_weekday,
            'current_utc_time':current_utc_time.strftime(utc_time_format),
            'track':track,
            'github_file_url':github_file_url,
            'github_repo_url':github_repo_url,
            'status_code':status.HTTP_200_OK
        }

        return Response(endpoint_response, status=status.HTTP_200_OK)      