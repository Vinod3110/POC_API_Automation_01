import requests

from API_Automation.utilities.addEmployeePayload import *
from API_Automation.utilities.configurations import *
from  API_Automation.utilities.resources import *


url = getConfig()['API']['endpoint'] + apiResources.createEmployee
url1 = getConfig()['API']['endpoint'] + apiResources.getAllEmployees
header = {'Content-Type': 'application/json'}
try:
    createEmpResponse = requests.get(url, json=addEmployeePayload("Vinod Pawar",40000, 27), headers=header, )
    print(createEmpResponse.status_code)
    # json_res = createEmpResponse.json()
    # print(json_res)
    re = requests.get(url1, headers=header)
    print(re.status_code)
    response = re.json()
    print(response)
    succMessage = response["message"]
    succStatus = response["status"]
    print(succMessage)
    print(succStatus)
    employeeInfo = response["data"]
    # print(employeeInfo)

except Exception as e:
    print(e)
    print("Printing exception block")