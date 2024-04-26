#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 19:24:08 2024

@author: xwl
"""
import requests
import time
from faker import Faker
from eth_account import Account



def get_nocaptcha_token(no_captcha_api_token) :

    
    headers = {'User-Token': no_captcha_api_token, 'Content-Type': 'application/json', 'Developer-Id': 'CiKFW5'}
    json_data = {
    'sitekey': '06ee6b5b-ef03-4491-b8ea-01fb5a80256f',
    'referer': 'https://faucet.0g.ai',
    }


    response = requests.post(url='http://api.nocaptcha.io/api/wanda/hcaptcha/universal', headers=headers,
                             json=json_data).json()
    print(response)
    if response.get('status') == 1:
        if response.get('msg') == '验证成功':
            return response['data']['generated_pass_UUID']
    return False


def faucet(address,cap):
    
    proxy = {
                'all': '' 
            }
    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,ru;q=0.8',
        'content-type': 'text/plain;charset=UTF-8',
        'origin': 'https://faucet.0g.ai',
        'priority': 'u=1, i',
        'referer': 'https://faucet.0g.ai/',
        'user-agent': Faker().chrome()#'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }
    data = '{"address":"'+address+'","hcaptchaToken":"'+cap+'"}'
    status_code=502
    while status_code==502:
        response = requests.post('https://faucet.0g.ai/api/faucet', headers=headers, data=data,proxies=proxy,verify=False)
        print(address,response.text)
        if ('0x' in response.text or 'processed' in response.text ):
            with open('0g.txt','a') as f:
                f.writelines(address+':'+pk+'\n')
            f.close()
        status_code=response.status_code
        time.sleep(1)
for in range(1000):
    try:
        no_captcha_api_token=''    # https://www.nocaptcha.io/register?c=CiKFW5
        g0=get_nocaptcha_token(no_captcha_api_token)
        acc=Account.create()
        address=acc.address
        pk=acc.key.hex()
        faucet(address,g0)

    except Exception as e:
        print(e)

