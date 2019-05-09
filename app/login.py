#!/usr/bin/env python
# coding=utf-8
import requests
from flask import Flask, request, jsonify
from app import app


@app.route('/login', methods=['POST'])
def login():
    req = request.get_json()
    code = req['code'].strip()
    wx_conf = app.config['wx']

    params = {}
    params['appid'] = wx_conf['appid']
    params['secret'] = wx_conf['secret']
    params['js_code'] = code
    params['grant_type'] = 'authorization_code'

    url = wx_conf['api']['code2session']
    response = requests.get(url, params=params)
    resp = response.text

    return resp
