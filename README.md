# DataDog series (python)
Undocumented DataDog features

Param `interval` in the request helps us to get result calculated for provided time period (in seconds).
Passing `interval: 60` helps us to get "per minute" representation of the metrics. 

## Disclaimer, or, Use at your own risk

This is **NOT** an official API from DataDog. You will not find any documentation regarding this code and usage.
The author assumes no responsibility or liability for any errors or problems regarding this API.
The information received with this API is provided on an "as is" basis with no guarantees of completeness, accuracy, usefulness or timeliness...

### Usage

```python
# set DATADOG_HOST, DATADOG_APP_KEY and DATADOG_API_KEY

import ddseries

data = request.exec(
           app_key,
           api_key,
           [
                   {
                       'q': 'sum:trace.rack.request.hits{service:my-lovely-service}.as_count()',
                       'from': '1619954820000',
                       'to': '1619958660000',
                       'interval': 60
                   }
           ]
       )
```

or with retry

```python
import ddseries

data = request.exec_with_retry(
           app_key,
           api_key,
           [
                   {
                       'q': 'sum:trace.rack.request.hits{service:my-lovely-service}.as_count()',
                       'from': '1619954820000',
                       'to': '1619958660000',
                       'interval': 60
                   }
           ],
           3
       )
```


### Example response

```json
{
  "responses":[
    {
      "status":"ok",
      "resp_version":2,
      "series":[
        {
          "unit":[
            {
              "family":"cache",
              "scale_factor":1.0,
              "name":"hit",
              "short_name":null,
              "plural":"hits",
              "id":39
            },
            null
          ],
          "query_index":0,
          "aggr":"sum",
          "scope":"service:my-lovely-service",
          "metric":"trace.http.request.hits",
          "expression":"sum:trace.http.request.hits{service:my-lovely-service}.as_count()",
          "tag_set":[

          ]
        }
      ],
      "to_date":1619958723000,
      "timing":"0.0662128925323",
      "query":"sum:trace.http.request.hits{service:my-lovely-service}.as_count()",
      "message":"",
      "res_type":"time_series",
      "interval":60,
      "times":[
        1619954820000.0,
        
        ...,
        
        1619958660000.0
      ],
      "from_date":1619955123000,
      "group_by":[

      ],
      "values":[
        [
          12345.0,
          
          ...,
          
          54321.0
        ]
      ]
    }
  ]
}

```

