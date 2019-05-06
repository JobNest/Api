#!/usr/bin/env python
# coding=utf-8
from flask import Flask, request, jsonify
from app import app

@app.route('/search', methods=['POST'])
def search():
    req = request.get_json()

    f = open('search.txt', 'w')
    f.write(str(req['query']))
    f.close()
    return jsonify(req)
