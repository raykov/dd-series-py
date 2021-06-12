#!/usr/bin/env python3

import os
import requests
import json

def body(queries = []):
    result = {}

    for i, query in enumerate(queries):
        result.update({
            'requests[{}][q]'.format(i): query.get('q'),
            'requests[{}][from]'.format(i): query.get('from'),
            'requests[{}][to]'.format(i): query.get('to'),
            'requests[{}][interval]'.format(i): query.get('interval')
        })

    return result


def exec(app_key, api_key, queries):
    url = "https://app.datadoghq.eu/series/batch_query"
    data = {'resp_version': '2'}
    data.update(body(queries))
    response = requests.post(
        url,
        headers={
            'DD-APPLICATION-KEY': app_key,
            'DD-API-KEY': api_key,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Encoding': 'gzip, deflate, br'
        },
        data=data
    )

    if response.status_code != 200:
        print(response.content)

        return

    return json.loads(response.content)