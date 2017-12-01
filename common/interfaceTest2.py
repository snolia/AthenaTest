# -*- coding: utf-8 -*-
import requests
import json
from AthenaTest.common.readConfig import ReadConfig

def interfaceTest2(num, api_purpose, api_host,request_url, request_method,request_data_type,header_data, request_data,encryption,check_point, s=None):

    # 表示收货仓且只传token
    headersA10 = {
                'Content-Type' : 'application/json',
                'tokenCode' : 'A1',
                'tokenSecret' : '123456'
    }

    # 表示收货仓且需要传pagenum等
    headersA11 = {
                'Content-Type': 'application/json',
                'tokenCode': 'A1',
                'tokenSecret': '123456',
                'pagenum': "1",
                'pagesize': "20"
    }

    # 表示客服且只传token
    headersA20 = {
                'Content-Type' : 'application/json',
                'tokenCode': 'A2',
                'tokenSecret': '123456'
    }

    # 表示客服且需要传pagenum等
    headersA21 = {
                'Content-Type' : 'application/json',
                'tokenCode': 'A2',
                'tokenSecret': '123456',
                'pagenum':'1',
                'pagesize':'20'
    }

    # 表示网点且只传token
    headersA30 = {
                'Content-Type' : 'application/json',
                'tokenCode': 'A3',
                'tokenSecret': '123456'
    }

    # 表示网点且需要传pagenum等
    headersA31 = {
                'Content-Type' : 'application/json',
                'tokenCode': 'A3',
                'tokenSecret': '123456',
                'pagenum':'1',
                'pagesize':'20',
    }

    # 表示宜家web且只传token
    headersA40 = {
                'Content-Type' : 'application/json',
                'tokenCode': 'A4',
                'tokenSecret': '123456'
    }

    # 表示宜家web且需要传pagenum等
    headersA41 = {
                'Content-Type' : 'application/json',
                'tokenCode': 'A4',
                'tokenSecret': '123456',
                'pagenum':'1',
                'pagesize':'20',
    }

    # 表示宜家app配送且只传token
    headersA50 = {
                'Content-Type' : 'application/json',
                'tokenCode': 'A5',
                'tokenSecret': '123456'
    }

    # 表示宜家app配送且需要传pagenum等
    headersA51 = {
                'Content-Type' : 'application/json',
                'tokenCode': 'A5',
                'tokenSecret': '123456',
                'pagenum':'1',
                'pagesize':'20',
    }

    # 表示宜家app安装且只传token
    headersA60 = {
                'Content-Type' : 'application/json',
                'tokenCode': 'A6',
                'tokenSecret': '123456'
    }

    # 表示宜家app安装且需要传pagenum等
    headersA61 = {
                'Content-Type' : 'application/json',
                'tokenCode': 'A6',
                'tokenSecret': '123456',
                'pagenum':'1',
                'pagesize':'20',
    }

    # 表示宜家app的sams且只传token
    headersA70 = {
                'Content-Type' : 'application/json',
                'tokenCode': 'A7',
                'tokenSecret': '123456'
    }

    # 表示宜家app的sams且需要传pagenum等
    headersA71 = {
                'Content-Type' : 'application/json',
                'tokenCode': 'A7',
                'tokenSecret': '123456',
                'pagenum':'1',
                'pagesize':'20',
    }

    # 测试环境
    # api_host = '192.168.10.56:3000'

    if request_method == 'POST':  # POST请求
        if request_data == '':
            if header_data == '':
                r = requests.request("POST", url='http://' + api_host + request_url)
            else:
                #r = requests.request("POST", url='http://' + api_host + request_url, headers=json.loads(header_data))  # json.dumps : dict转成str; json.loads:str转成dict (从excel取的数据需要转换一下）
                if header_data == 'A10':
                    r = requests.request("POST", url='http://' + api_host + request_url, headers=headersA10)
                elif header_data == 'A11':
                    r = requests.request("POST", url='http://' + api_host + request_url, headers=headersA11)
                elif header_data == 'A20':
                    r = requests.request("POST", url='http://' + api_host + request_url, headers=headersA20)
                elif header_data == 'A21':
                    r = requests.request("POST", url='http://' + api_host + request_url, headers=headersA21)
                elif header_data == 'A30':
                    r = requests.request("POST", url='http://' + api_host + request_url, headers=headersA30)
                elif header_data == 'A31':
                    r = requests.request("POST", url='http://' + api_host + request_url, headers=headersA31)
                elif header_data == 'A40':
                    r = requests.request("POST", url='http://' + api_host + request_url, headers=headersA40)
                elif header_data == 'A41':
                    r = requests.request("POST", url='http://' + api_host + request_url, headers=headersA41)
                elif header_data == 'A50':
                    r = requests.request("POST", url='http://' + api_host + request_url, headers=headersA50)
                elif header_data == 'A51':
                    r = requests.request("POST", url='http://' + api_host + request_url, headers=headersA51)
                elif header_data == 'A60':
                    r = requests.request("POST", url='http://' + api_host + request_url, headers=headersA60)
                elif header_data == 'A61':
                    r = requests.request("POST", url='http://' + api_host + request_url, headers=headersA61)
                elif header_data == 'A70':
                    r = requests.request("POST", url='http://' + api_host + request_url, headers=headersA70)
                elif header_data == 'A71':
                    r = requests.request("POST", url='http://' + api_host + request_url, headers=headersA71)
                else:
                    print("没有对应的headers,请核对excel中的header_data数据是否正确！")

        else:
            if request_data_type == 'formData':  # 请求数据格式为formData
                if header_data == '':
                    r = requests.request("POST", url='http://' + api_host + request_url,
                                         files=json.loads(request_data))
                else:
                    #r = requests.request("POST", url='http://' + api_host + request_url,files=json.loads(request_data), headers=json.loads(header_data))
                    if header_data == 'A10':
                        r = requests.request("POST", url='http://' + api_host + request_url, files=json.loads(request_data),headers=headersA10)
                    elif header_data == 'A11':
                        r = requests.request("POST", url='http://' + api_host + request_url, files=json.loads(request_data),headers=headersA11)
                    elif header_data == 'A20':
                        r = requests.request("POST", url='http://' + api_host + request_url, files=json.loads(request_data),headers=headersA20)
                    elif header_data == 'A21':
                        r = requests.request("POST", url='http://' + api_host + request_url, files=json.loads(request_data),headers=headersA21)
                    elif header_data == 'A30':
                        r = requests.request("POST", url='http://' + api_host + request_url, files=json.loads(request_data),headers=headersA30)
                    elif header_data == 'A31':
                        r = requests.request("POST", url='http://' + api_host + request_url, files=json.loads(request_data),headers=headersA31)
                    elif header_data == 'A40':
                        r = requests.request("POST", url='http://' + api_host + request_url,
                                             files=json.loads(request_data), headers=headersA40)
                    elif header_data == 'A41':
                        r = requests.request("POST", url='http://' + api_host + request_url,
                                             files=json.loads(request_data), headers=headersA41)
                    elif header_data == 'A50':
                        r = requests.request("POST", url='http://' + api_host + request_url,
                                             files=json.loads(request_data), headers=headersA50)
                    elif header_data == 'A51':
                        r = requests.request("POST", url='http://' + api_host + request_url,
                                             files=json.loads(request_data), headers=headersA51)
                    elif header_data == 'A60':
                        r = requests.request("POST", url='http://' + api_host + request_url,
                                             files=json.loads(request_data), headers=headersA60)
                    elif header_data == 'A61':
                        r = requests.request("POST", url='http://' + api_host + request_url,
                                             files=json.loads(request_data), headers=headersA61)
                    elif header_data == 'A70':
                        r = requests.request("POST", url='http://' + api_host + request_url,
                                             files=json.loads(request_data), headers=headersA70)
                    elif header_data == 'A71':
                        r = requests.request("POST", url='http://' + api_host + request_url,
                                             files=json.loads(request_data), headers=headersA71)
                    else:
                        print("没有对应的headers,请核对excel中的header_data数据是否正确！")

            elif request_data_type == 'raw':  # 请求数据格式为raw，需要以json格式传递数据
                if header_data == '':
                    r = requests.request("POST", url='http://' + api_host + request_url, data=json.dumps(json.loads(request_data)))
                else:
                    #r = requests.request("POST", url='http://' + api_host + request_url,data=json.dumps(json.loads(request_data)), headers=json.loads(header_data))
                    if header_data == 'A10':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.dumps(json.loads(request_data)), headers=headersA10)
                    elif header_data == 'A11':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.dumps(json.loads(request_data)), headers=headersA11)
                    elif header_data == 'A20':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.dumps(json.loads(request_data)), headers=headersA20)
                    elif header_data == 'A21':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.dumps(json.loads(request_data)), headers=headersA21)
                    elif header_data == 'A30':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.dumps(json.loads(request_data)), headers=headersA30)
                    elif header_data == 'A31':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.dumps(json.loads(request_data)), headers=headersA31)
                    elif header_data == 'A40':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.dumps(json.loads(request_data)), headers=headersA40)
                    elif header_data == 'A41':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.dumps(json.loads(request_data)), headers=headersA41)
                    elif header_data == 'A50':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.dumps(json.loads(request_data)), headers=headersA50)
                    elif header_data == 'A51':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.dumps(json.loads(request_data)), headers=headersA51)
                    elif header_data == 'A60':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.dumps(json.loads(request_data)), headers=headersA60)
                    elif header_data == 'A61':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.dumps(json.loads(request_data)), headers=headersA61)
                    elif header_data == 'A70':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.dumps(json.loads(request_data)), headers=headersA70)
                    elif header_data == 'A71':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.dumps(json.loads(request_data)), headers=headersA71)
                    else:
                        print("没有对应的headers,请核对excel中的header_data数据是否正确！")

            else:
                if header_data == '':
                    r = requests.request("POST", url='http://' + api_host + request_url,
                                         data=json.dumps(json.loads(request_data)))
                else:
                    #r = requests.request("POST", url='http://' + api_host + request_url,data=json.loads(request_data), headers=json.loads(header_data))
                    if header_data == 'A10':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.loads(request_data), headers=headersA10)
                    elif header_data == 'A11':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.loads(request_data), headers=headersA11)
                    elif header_data == 'A20':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.loads(request_data), headers=headersA20)
                    elif header_data == 'A21':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.loads(request_data), headers=headersA21)
                    elif header_data == 'A30':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.loads(request_data), headers=headersA30)
                    elif header_data == 'A31':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.loads(request_data), headers=headersA31)
                    elif header_data == 'A40':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.loads(request_data), headers=headersA30)
                    elif header_data == 'A41':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.loads(request_data), headers=headersA31)
                    elif header_data == 'A50':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.loads(request_data), headers=headersA30)
                    elif header_data == 'A51':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.loads(request_data), headers=headersA31)
                    elif header_data == 'A60':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.loads(request_data), headers=headersA30)
                    elif header_data == 'A61':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.loads(request_data), headers=headersA31)
                    elif header_data == 'A70':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.loads(request_data), headers=headersA30)
                    elif header_data == 'A71':
                        r = requests.request("POST", url='http://' + api_host + request_url, data=json.loads(request_data), headers=headersA31)
                    else:
                        print("没有对应的headers,请核对excel中的header_data数据是否正确！")

    elif request_method == 'GET':  # GET请求
        if request_data == '':
            if header_data == '':
                r = requests.request("GET", url='http://' + api_host + request_url)
            else:
                #r = requests.request("GET", url='http://' + api_host + request_url, headers=json.loads(header_data))
                if header_data == 'A10':
                    r = requests.request("GET", url='http://' + api_host + request_url, headers=headersA10)
                elif header_data == 'A11':
                    r = requests.request("GET", url='http://' + api_host + request_url, headers=headersA11)
                elif header_data == 'A20':
                    r = requests.request("GET", url='http://' + api_host + request_url, headers=headersA20)
                elif header_data == 'A21':
                    r = requests.request("GET", url='http://' + api_host + request_url, headers=headersA21)
                elif header_data == 'A30':
                    r = requests.request("GET", url='http://' + api_host + request_url, headers=headersA30)
                elif header_data == 'A31':
                    r = requests.request("GET", url='http://' + api_host + request_url, headers=headersA31)
                elif header_data == 'A40':
                    r = requests.request("GET", url='http://' + api_host + request_url, headers=headersA40)
                elif header_data == 'A41':
                    r = requests.request("GET", url='http://' + api_host + request_url, headers=headersA41)
                elif header_data == 'A50':
                    r = requests.request("GET", url='http://' + api_host + request_url, headers=headersA50)
                elif header_data == 'A51':
                    r = requests.request("GET", url='http://' + api_host + request_url, headers=headersA51)
                elif header_data == 'A60':
                    r = requests.request("GET", url='http://' + api_host + request_url, headers=headersA60)
                elif header_data == 'A61':
                    r = requests.request("GET", url='http://' + api_host + request_url, headers=headersA61)
                elif header_data == 'A70':
                    r = requests.request("GET", url='http://' + api_host + request_url, headers=headersA70)
                elif header_data == 'A71':
                    r = requests.request("GET", url='http://' + api_host + request_url, headers=headersA71)
                else:
                    print("没有对应的headers,请核对excel中的header_data数据是否正确！")

        else:
            if header_data == '':
                r = requests.request("GET", url='http://' + api_host + request_url, params=json.loads(request_data))
            else:
                #r = requests.request("GET", url='http://' + api_host + request_url, params=json.loads(request_data),headers=json.loads(header_data))
                if header_data == 'A10':
                    r = requests.request("GET", url='http://'+api_host+request_url, headers=headersA10, params=json.loads(request_data))
                elif header_data == 'A11':
                    r = requests.request("GET", url='http://'+api_host+request_url, headers=headersA11, params=json.loads(request_data))
                elif header_data == 'A20':
                    r = requests.request("GET", url='http://'+api_host+request_url, headers=headersA20, params=json.loads(request_data))
                elif header_data == 'A21':
                    r = requests.request("GET", url='http://'+api_host+request_url, headers=headersA21, params=json.loads(request_data))
                elif header_data == 'A30':
                    r = requests.request("GET", url='http://'+api_host+request_url, headers=headersA30, params=json.loads(request_data))
                elif header_data == 'A31':
                    # r = requests.request("GET", url="http://192.168.10.56:8763/ms-order-data/appOrder/topieces-pieces", headers=headersA31, params=json.loads(request_data))
                    r = requests.request("GET", url='http://' + api_host + request_url, headers=headersA31,params=json.loads(request_data))
                elif header_data == 'A40':
                    r = requests.request("GET", url='http://' + api_host + request_url, headers=headersA40,
                                         params=json.loads(request_data))
                elif header_data == 'A41':
                    r = requests.request("GET", url='http://' + api_host + request_url, headers=headersA41,
                                         params=json.loads(request_data))
                elif header_data == 'A50':
                    r = requests.request("GET", url='http://' + api_host + request_url, headers=headersA50,
                                         params=json.loads(request_data))
                elif header_data == 'A51':
                    r = requests.request("GET", url='http://' + api_host + request_url, headers=headersA51,
                                         params=json.loads(request_data))
                elif header_data == 'A60':
                    r = requests.request("GET", url='http://' + api_host + request_url, headers=headersA60,
                                         params=json.loads(request_data))
                elif header_data == 'A61':
                    r = requests.request("GET", url='http://' + api_host + request_url, headers=headersA61,
                                         params=json.loads(request_data))
                elif header_data == 'A70':
                    r = requests.request("GET", url='http://' + api_host + request_url, headers=headersA70,
                                         params=json.loads(request_data))
                elif header_data == 'A71':
                    r = requests.request("GET", url='http://' + api_host + request_url, headers=headersA71,
                                         params=json.loads(request_data))
                else:
                    print("没有对应的headers,请核对excel中的header_data数据是否正确！")

    elif request_method == 'DELETE':  # DELETE请求
        if request_data == '':
            if header_data == '':
                r = requests.request('DELETE', url='http://' + api_host + request_url, params=request_data)
            else:
                # r = requests.request('DELETE', url='http://' + api_host + request_url, params=request_data, headers=json.loads(header_data))
                if header_data == 'A10':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=request_data, headers=headersA10)
                elif header_data == 'A11':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=request_data, headers=headersA11)
                elif header_data == 'A20':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=request_data, headers=headersA20)
                elif header_data == 'A21':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=request_data, headers=headersA21)
                elif header_data == 'A30':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=request_data, headers=headersA30)
                elif header_data == 'A31':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=request_data, headers=headersA31)
                elif header_data == 'A40':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=request_data, headers=headersA40)
                elif header_data == 'A41':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=request_data, headers=headersA41)
                elif header_data == 'A50':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=request_data, headers=headersA50)
                elif header_data == 'A51':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=request_data, headers=headersA51)
                elif header_data == 'A60':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=request_data, headers=headersA60)
                elif header_data == 'A61':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=request_data, headers=headersA61)
                elif header_data == 'A70':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=request_data, headers=headersA70)
                elif header_data == 'A71':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=request_data, headers=headersA71)
                else:
                    print("没有对应的headers,请核对excel中的header_data数据是否正确！")

        else:
            if header_data == '':
                r = requests.request('DELETE', url='http://' + api_host + request_url, params=json.loads(request_data))
            else:
                #r = requests.request('DELETE', url='http://' + api_host + request_url, params=json.loads(request_data), headers=json.loads(header_data))
                if header_data == 'A10':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=json.loads(request_data), headers=headersA10)
                elif header_data == 'A11':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=json.loads(request_data), headers=headersA11)
                elif header_data == 'A20':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=json.loads(request_data), headers=headersA20)
                elif header_data == 'A21':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=json.loads(request_data), headers=headersA21)
                elif header_data == 'A30':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=json.loads(request_data), headers=headersA30)
                elif header_data == 'A31':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=json.loads(request_data), headers=headersA31)
                elif header_data == 'A40':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=json.loads(request_data), headers=headersA40)
                elif header_data == 'A41':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=json.loads(request_data), headers=headersA41)
                elif header_data == 'A50':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=json.loads(request_data), headers=headersA50)
                elif header_data == 'A51':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=json.loads(request_data), headers=headersA51)
                elif header_data == 'A60':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=json.loads(request_data), headers=headersA60)
                elif header_data == 'A61':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=json.loads(request_data), headers=headersA61)
                elif header_data == 'A70':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=json.loads(request_data), headers=headersA70)
                elif header_data == 'A71':
                    r = requests.request('DELETE', url='http://' + api_host + request_url, params=json.loads(request_data), headers=headersA71)
                else:
                    print("没有对应的headers,请核对excel中的header_data数据是否正确！")
    else:
        print(num + ' ' + api_purpose + '  HTTP请求方法错误，请确认[Request Method]字段是否正确！！！')
        s = None
        return 400, s

    status = r.status_code  # 返回状态
    resp = r.text  # 返回数据
    # print(resp)
    #
    # respjson = json.loads(resp)
    #
    # prepaid = respjson['data']['orderData']
    # print(prepaid)

    print("测试接口：" + request_url)
    print("返回的状态：" + str(status))

    # self.assertEqual(resp['success'], check_point)

    if status == 200:  # 判断返回状态是否为A200
        if check_point in resp:  # 检查测试用例中的检查点是否包含在返回的数据里面
            result = "pass"
            print("测试结果：成功！！！  " + str(status))
            # print('返回的数据：' + str(r.text))
            return status, resp, s, result
        else:
            result = "fail"
            print("测试结果：失败！！！  " + str(status))
            print('返回的数据：' + str(r.text))
            return 200, resp, None, result
    else:
        result = "fail"
        print("测试结果：失败！！！  " + str(status))
        print('返回的数据：' + str(r.text))
        #return status, resp.decode('utf-8'), None, result
        return status, resp, None, result
