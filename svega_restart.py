#THIS SCRIPT IS RESPONISABILITY OF WHO USES IT
#THIS IS SCRIPT WAS CREATED TO AUTOMATE RESTART OF FXO APPLIANCES
#!/usr/bin/python
import requests

vega_ip = "0.0.0.0"

vega_data = ""

# Fill in your details here to be posted to the login form.
payload = {
    'username': 'redaer_user',
    'password': 'password'
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post('http://'+vega_ip+'/vs_login', data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    #print p.text

    # An authorised request.
    r = s.get('http://'+vega_ip+'/vsconfig?sid=0&form_name=95&dont_need_uri_decode=1&cli_command=reboot%20system', timeout=10)
    #print r.text
    vega_data = r.text
    p.close()
    r.close()
    s.close()

print('Answer:')
print(vega_data)