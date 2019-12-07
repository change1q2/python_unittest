"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：
============================
"""
import requests

#注册url
register_url = "http://api.lemonban.com/futureloan/member/register"

#注册请求头,
# 会通用所以设置一个通用的header
header = {
    "X-Lemonban-Media-Type": "lemonban.v2",
    "Content-Type": "application/json"
}

#注册请求体
register_data = {
    "mobile_phone": "15867554850",
    "pwd": "123456qwe",
    "reg_name": "seak",
    "type": 0
}

# #请求注册接口
# response = requests.post(url=register_url,json=register_data,headers=header)
# #返回结果并获取json的数据放到json_data中
# json_data_register = response.json()
# print(json_data_register)
# #从返的结果中提取想要的数据,(从data中获取id)
# id = json_data_register["data"]["id"]
# print(id)
#注册过的数据再次注册会报错



# ------------------------登陆--------------------------

#登陆url
login_url = "http://api.lemonban.com/futureloan/member/login"

#登陆体
login_data = {
    "mobile_phone": "15867554850",
    "pwd": "123456qwe",
}

#请求登陆
response = requests.post(url=login_url, headers=header,json=login_data)
json_data_login = response.json()
#print(json_data_login)


#提取用id
login_id = json_data_login["data"]["id"]
#print(login_id)


#提取token类型
login_type = json_data_login["data"]["token_info"]["token_type"]
#print(login_type)


#提取token值
login_token = json_data_login["data"]["token_info"]["token"]
#print(login_token)



#拼接token数据,获取token数据(用于认证的请求头数据)
token_data = login_type + " " + login_token
#print(token_data)



#------------------------充值--------------
#充值url

#请求url
recharge_url = "http://api.lemonban.com/futureloan/member/recharge"

#请求头，需要token鉴权
header_token = {
    "X-Lemonban-Media-Type": "lemonban.v2",
    "Content-Type": "application/json",
    "Authorization":token_data
}

#请求体

recharge_data = {
        "member_id": login_id ,
        "amount": 100
}

#请求接口
recharge_response = requests.post(url=recharge_url,headers=header_token,json=recharge_data)
json_data_recharge = recharge_response.json()
print(json_data_recharge)