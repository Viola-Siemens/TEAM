import requests

from src.app.service.references import PORT

print("Input format: <request route> [<arg-key1>=<arg-value1> [<arg-key2>=<arg-value2> [...]]]")

while True:
    s = input()
    if s == "":
        break
    args = s.split()
    url = f"http://localhost:{PORT}/{args[0]}"
    if len(args) > 1:
        url += "?" + args[1]
        for i in range(2, len(args)):
            url += "&" + args[i]
    res = requests.post(url)
    print(res.content)
