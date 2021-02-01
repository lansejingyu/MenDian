#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import json
from CityNumber import CityCode

# url = "http://uxin-fin.fat.xin.com/app/creditFundCity/getFundName"
# payload = {"fundBuyingCity": CityCode(), "fundLicenseCity": CityCode(), "fundDeliverCity": CityCode()}
# headers = {
# 	'Content-Type': 'application/json'
# }
#
# response = requests.request("POST", url, headers=headers, data=json.dumps(payload))  # 用 dumps 方法转化成 json 格式
# print(response.json())
# # print(json.dumps(payload))


url = "http://uxin-fin.fat.xin.com/app/creditCustomerInfo/xySubmitFirstInfo"

payload = {"fundBuyingCityCode": 110000, "fundBuyingCityName": "北京", "fundDeliverCityCode": 110000,
		   "fundDeliverCityName": "北京", "fundLicenseCityCode": 110000, "fundLicenseCityName": "北京", "fundName": "xy",
		   "mobile": "15185452581", "userName": "卫滢东", "idCard": "420101196204209920",
		   "bankAccount": "6222021884372429532"}
headers = {
	'Content-Type': 'application/json;charset=UTF-8'
}

response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

print(response.text)
