from django.shortcuts import render, redirect
import requests, urllib.parse, json

# Create your views here.

def redirect(request):

    get_code = request.GET.get('code')
    get_state = request.GET.get('state')
    redir_uri = "http://165.227.21.26/redirect"
    c_id = "V2InkOOq4XaUIX5H9rwj8caoK986ppBlMR4kqtsl"
    c_secret = "uIv8MTGGSnND9LRT0yN0vrg3o1dy7ARHf7eSHkTTNij7bkkZFFmwq7aAYXCr8beQ1XKQrqfqq5yz9ZGR4gcUdNlolHhAhNYeC1PH5uLsjK4iu2nXNASAZA6Ok7jdZV2x"

    payload = {'grant_type':"authorization_code", 'client_id':c_id, 'client_secret':c_secret, 'code':get_code, 'redirect_uri':redir_uri, 'state':get_state}
    token_url = 'http://165.227.62.232/oauth2/token/'


    req = requests.post(token_url, data = payload)

    trans = json.loads(req.text)
    token = trans.get('access_token')
    token_string = str(token)


    headers = {'Authorization': 'Bearer ' + token_string}

    api_url = 'http://165.227.62.232/api/hello'
    get_api = requests.get(api_url, headers = headers)


    user_url = 'http://165.227.62.232/posts/userpage'
    get_user = requests.get(user_url, headers = headers)
    user = get_user.text

    # return redirect('redirect')
    # return render(request, 'redirect_endpoint/redirect.html', {'code':get_code, 'state': get_state, 'redirect_uri': redir_uri, 'req':req.text})

    return render(request, 'redirect_endpoint/redirect.html', {'req':req.text, 'token':token, 'api':get_api.text, 'user':user})
