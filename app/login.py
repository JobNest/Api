#!/usr/bin/env python
# coding=utf-8
from flask import Flask, request, jsonify
from app import app

@app.route('/login', methods=['POST'])
def login():
    json_data = request.get_json()
    data = request.get_data()

    f = open('login.txt', 'w')
    f.write(str(data))
    f.close()
    return jsonify(json_data)
