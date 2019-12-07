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
"""
使用cookie和session鉴权的接口处理
鉴权：是指验证用户是否拥有访问系统的权利。


使用requests模块中的session对象来发请求


"""
##  -----------------使用requests直接发送请求，无法通过session鉴权-------

# # # 老版的前程贷登录接口
# login_url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
#
# #老板本前程贷请求体
# login_data = {
#     "mobilephone": "13367899876",
#     "pwd": "lemonban"
# }
#
# #老版本前程贷款发送请求
# res = requests.post(url=login_url, data=login_data)
# #接受请求
# login_json_data =res.json()
# #print(login_json_data)
# # print(res.cookies)#cookie不在data中需要单独获取出来

#-------------充值------------，没有进行鉴权可以随便登陆

##老版本充值接口
recharge_url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
recharge_data = {
    "mobilephone": "13367899876",
    "amount": 200000
}
res2 = requests.post(url=recharge_url,data=recharge_data)
recharge_data = res2.json()
#print(recharge_data)
print(res2.json()) #把上面的2行代码合并成一行



#-----------------使用requests模块中的session对象来发请求，进行鉴权后需要检验---------------

# # 创建一个session对象:se对象能够自动记录上一次请求中的cookie信息
# se = requests.session()
#
# # 老版的前程贷登录接口
# login_url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
# login_data = {
#     "mobilephone": "13367899876",
#     "pwd": "lemonban"
# }
#
# #使用se对象发送请求
# res3 =se.post(url=login_url, data=login_data)
# print(res3.json())
# #---------------------充值，直接使用登陆对象的cookie------------
# # 老版的前程贷充值接口
# recharge_url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
# recharge_data = {
#     "mobilephone": "13367899876",
#     "amount": 200000
# }
# #se对象能够自动记录上一次请求中的cookie信息
# res4 = se.post(url=recharge_url, data=recharge_data)
# print(res4.json())