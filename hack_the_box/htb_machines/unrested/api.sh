curl --request POST \
         --url 'http://10.10.11.50/zabbix/api_jsonrpc.php' \
         --header 'Content-Type: application/json-rpc' \
         --data '{     "jsonrpc": "2.0", "auth":"d3fbd1c2c2f098640ec07a7a18c48e276141315ffadee9170c5ffc09f2bc577a", "sessionid":"442cedac139bf64f9d75a2de513d423d",   "method": "user.get",     "params": {         "output": ["userid", "username"],         "selectRole": "extend",         "userids": "3"     },     "id": 3 }' --proxy http://localhost:8080



         #"auth":"d3fbd1c2c2f098640ec07a7a18c48e276141315ffadee9170c5ffc09f2bc577a",
         #"sessionid":"442cedac139bf64f9d75a2de513d423d"