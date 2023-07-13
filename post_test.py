import requests, json

# request = requests.post("http://localhost:8080/api/ending/",
#                         data={
#                             "data": json.dumps({
#                                 "sname": "陈思宇",
#                                 "cname": "周日 14:45",
#                                 "date": "2023-7-13",
#                                 "tname": "杨斌"
#                             })
#                         }
#                     )
r = requests.post("http://127.0.0.1:8000/api/ending/",
                  data=json.dumps({
                        "sname": "陈思宇",
                        "cname": "周日 14:45",
                        "date": "2023-7-13",
                        "tname": "杨斌"
                    })
                  )

print(r.status_code)