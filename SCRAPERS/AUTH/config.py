import json

login_info= {
    "USER": "TEST",
    "PASS": "TEST",
}

json_string = json.dumps(login_info, indent=3)
with open('config_str.json', 'w') as f:
    f.write(json_string)
    #

json_dict = json.dumps(login_info, indent=3)
with open('config_dict.json', 'w') as fp:
    json.dump(login_info, fp)

