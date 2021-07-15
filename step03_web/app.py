from flask import Flask, request, render_template
from dao import bank_get2

app= Flask(__name__)

# index.html 단순실행
@app.route("/", methods=['get'])
def index_view():
    return render_template("index.html")

# 버튼 클릭시에 비동기로 응답
@app.route("/dataget", methods=['get'])
def req_res():
    data = bank_get2()
    # print('=========', data)
    #TypeError: The view function did not return a valid response. The return type must be a string, dict, tuple, Response instance, or WSGI callable, but it was a list. 
    print('=========', data) #list
    # 
    # return dict(data)
    # return tuple(data)
    return str(data)

# 지현언니 코드

# def req_res():
#     data = bank_get2()
#     # print(data)
#     str_data = ""
#     for i in range(len(data)):
#         str_data += str(data[i]) + ","
#     # print("-------", type(str_data)) 
#     return str_data


if __name__ == "__main__":
    # req_res()
    app.run(debug=True, host="127.0.0.1", port=5000)