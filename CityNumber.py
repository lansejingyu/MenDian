import mysql.connector

mydb = mysql.connector.connect(host='rm-2ze0q80w59h4uyvx4rw.mysql.rds.aliyuncs.com', user='xin',
							   passwd='48sdf37EB7', database='uxin_fin')

mycursor = mydb.cursor()


def CityCode():
	CarCity = input("请输入城市：")
	City_Name = "SELECT city_name FROM credit_fund_city WHERE city_name = '%s' and valid=1 limit 1" % (CarCity)
	mycursor.execute(City_Name)
	City_Name = mycursor.fetchall()  # fetchall() 获取所有数据
	for x in City_Name:
		City_Name = x[0]

	if City_Name == CarCity:
		City_Code = "SELECT city_code FROM credit_fund_city WHERE city_name = '%s' and valid=1 limit 1" % (CarCity)
		mycursor.execute(City_Code)
		City_Code = mycursor.fetchall()  # fetchall() 获取所有数据
		for x in City_Code:
			City_Code = x[0]
			return City_Code
		# print(City_Code)
	else:
		print("请输入正确的城市")
