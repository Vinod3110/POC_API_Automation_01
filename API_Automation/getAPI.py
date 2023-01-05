##-- Authentication

import requests
from API_Automation.utilities.configurations import *
from  API_Automation.utilities.resources import *


url = getConfig()['API']['endpoint'] + apiResources.getAllEmployees
header = {'Content-Type': 'application/json'}
try:
    re = requests.get(url, headers=header)
    print(re.status_code)
    response = re.json()
    print(response)
    succMessage = response["message"]
    succStatus = response["status"]
    print(succMessage)
    print(succStatus)
    employeeInfo = response["data"]
    # print(employeeInfo)
    for employee in employeeInfo:
        if employee["employee_age"] == 61 :
            print(employee)
    assert re.status_code == 200
    assert 'Success' in succMessage
    assert 'success' in succStatus

except Exception as e:
    print(e)
    print("Printing exception block")