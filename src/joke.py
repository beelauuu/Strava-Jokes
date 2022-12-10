import requests
import config
import joke_list 

auth_url = 'https://www.strava.com/api/v3/oauth/token'
url = 'https://www.strava.com/api/v3'



#For initial authorization
# payload = {
#     'client_id' : config.client_id,
#     'client_secret': config.client_secret,
#     'grant_type':'authorization_code',
#     'code': config.code
# }
def update_joke(): 
    #Retrieving refresh token
    payload = {
        'client_id' : config.client_id,
        'client_secret': config.client_secret,
        'grant_type':'refresh_token',
        'refresh_token': config.refresh_token
    }
    response = requests.post(
        auth_url,
        data=payload,
    )
    access_token = response.json()['access_token']

    #Getting first (most recent) activity id
    headers= {
        'Authorization': 'Bearer ' + access_token 
    }
    param = {
    'page': 1,
    'per_page': 1
    }
    response = requests.get(
        url+'/athlete/activities',
        headers=headers,
        params=param
    )
    activity_id = response.json()[0]['id']

    #Get current description
    headers= {
        'Authorization': 'Bearer ' + access_token 
    }
    response = requests.get(
        url+'/activities/'+str(activity_id),
        headers=headers,
    )
    current_description = response.json()['description']
    if current_description is None:
        current_description = ''

    #Updating activity description
    if('🤡 Joke of the day 🤡' not in current_description):
        tuple = joke_list.check()
        setup = tuple[0].strip()
        punchline = tuple[1]
        headers= {
            'Authorization': 'Bearer ' + access_token 
        }
        updatableActivity = {
            'description': '🤡 Joke of the day 🤡\n' + setup + '\n' + punchline + '\n- by Joke.py' + '\n\n' + current_description
        }
        response = requests.put(
            url+'/activities/'+str(activity_id),
            headers=headers,
            params=updatableActivity
        )
    
update_joke()

