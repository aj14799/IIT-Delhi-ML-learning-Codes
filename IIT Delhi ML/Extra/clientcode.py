import requests
import json
address = "http://127.0.0.1:5000"
data2 = {"msg":"""Hi yash, you have won $10000 if you just answer one question,
         and your question is  - what is capital of India? 
         you can claim your price by calling us at 08989897897 
         and deposit $2000."""}
data2 = json.dumps(data2)
response = requests.post(address,data2)
print(response.content.decode())