from requests import request, post

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

print("\n#1 Метод любого типа без параметров[POST]:")
response = post(url=url)
print(f"Response: status={response.status_code} body={response.text}")

print("\n#2 Метод не из списка[HEAD]:")
method_name = "HEAD"
response = request(method=method_name, url=url, data=method_name)
print(f"{method_name=}, Response: status={response.status_code} body={response.text}")


print("\n#3 Правильное значение метода[GET]:")
method_name = "GET"
response = request(method=method_name, url=url, params=method_name)
print(f"{method_name=}, Response: status={response.status_code} body={response.text}")

print("\n#4 Список методов:")
methods = ["GET", "POST", "PUT", "DELETE"]
for method in methods:
    for param in methods:
        if method == "GET":
            response = request(method=method, url=url, params=param)
        else:
            response = request(method=method, url=url, data=param)
        print(f"{method=}, {param=} Response: status={response.status_code} body={response.text}")



