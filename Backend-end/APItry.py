import json
from urllib.request import Request, urlopen

#zb网站获取数据Api
url = 'https://opendata.paris.fr/api/records/1.0/search/?dataset=que-faire-a-paris-&facet=category&facet=tags&facet=address_zipcode&facet=address_city&facet=pmr&facet=blind&facet=deaf&facet=access_type&facet=price_type'
#包装头部
firefox_headers = {'User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}
#构建请求
request = Request( url, headers = firefox_headers )
html = urlopen( request )
#获取数据
data = html.read()
#转换成字符串
strs = str(data)
#截取字符串
print(len(strs))
strs_for_json = strs[44:]
strs_for_json= strs_for_json[:-2]
print(strs_for_json)
#转换成JSON
data = strs_for_json
datas = json.dumps(data)
#转换成字典数据
data_json = json.loads(data)
print(type(data_json))#<class 'dict'>
print(len(data_json['data']))
len = len(data_json['data'])
#输出价格表
# print("*****************************zb价格获取***************************************")
# for i in range(0,len):
#     print("币种\市场类型："+data_json['datas'][i]['market'], "^^^^^^^","实时价格："+data_json['datas'][i]['sell1Price'],"^^^^^^^","24小时最高价格："+data_json['datas'][i]['hightPrice'],"^^^^^^^","24小时最低价格："+data_json['datas'][i]['lastPrice'])
