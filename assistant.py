# Patrick Apgar

import wolframalpha
app_id = '7RQEH5-E64LEQHTY8'  # get your own at https://products.wolframalpha.com/api/
client = wolframalpha.Client(app_id)


res = client.query('temperature in Washington, DC on October 3, 2012')
for pod in res.pods:
    for sub in pod.subpods:
        print(sub.plainText)