"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：
============================
jsonpath:用来解析多层嵌套的json数据


"""
import requests
import jsonpath

#---------------------登陆接口----------------

#登陆url
login_url = "http://api.lemonban.com/futureloan/member/login"

#登陆头文件,头文件可以公用所以命名为heard
header = {
    "X-Lemonban-Media-Type": "lemonban.v2",
    "Content-Type": "application/json"
}

#登陆体

login_data = {
    "mobile_phone": "15867554850",
    "pwd": "123456qwe",
}

#登陆数据获取
#1发送登陆的数据
response = requests.post(url=login_url, headers=header,json=login_data)
#2获取登陆的数据
login_json_respone_data = response.json()
#print(login_json_respone_data)

#用jsonpath来获取数据,$表示{} ..表示找到符合条件的字段如id,[0]迭代表示器，
# 不加[]这个会把取数来的值放在列表中list，加上[]表示找到对应的值int
# res_data = jsonpath.jsonpath(login_json_respone_data,"$..id")[0]
# print(res_data,type(res_data))

#取登陆的id值
login_id = jsonpath.jsonpath(login_json_respone_data,"$..id")[0]
#print(login_id,type(login_id))

#取登陆的token_type类型值
login_token_type = jsonpath.jsonpath(login_json_respone_data,"$..token_type")[0]
#print(login_token_type,type(login_token_type))

#取登陆的token值
login_token = jsonpath.jsonpath(login_json_respone_data,"$..token")[0]
#print(login_token,type(login_token))

#拼接token数据
token_data = login_token_type + ' ' + login_token
#print(token_data)
#-------充值----------

#充值url
recharge_url = "http://api.lemonban.com/futureloan/member/recharge"


#充值头文件
header_token = {
    "X-Lemonban-Media-Type": "lemonban.v2",
    "Content-Type": "application/json",
    "Authorization":login_token
}


#充值体
recharge_data = {
        "member_id": login_id ,
        "amount": 100
}

#请求充值
#1.发送请求
response = requests.post(url=recharge_url,headers=header_token,json=recharge_data)
#2.获取请求的json数据
recharge_json_data = response.json()
print(recharge_json_data,type(recharge_json_data))