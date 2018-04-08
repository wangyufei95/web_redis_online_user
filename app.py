from flask import Flask, request, render_template, jsonify
import redis
import json
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/redisdata", methods=["POST"])
def data():
    redis_client = redis.Redis(host='127.0.0.1', port=6379)
    strJson = request.json
    strTime = strJson.get("date")
    print(strTime)
    all_keys = redis_client.hgetall(strTime)

    key_value = list(all_keys.keys())
    value_list = list(all_keys.values())
    # 初始化
    i = 0
    lkey = list(key_value)
    lvalue = list(value_list)
    listlen = key_value.__len__()
    pylist2json = {}
    # 遍历循环
    while i < listlen:
        lkey[i] = key_value[i].decode()
        lvalue[i] = value_list[i].decode()
        i += 1
    # 转换成json字符串
    pylist2json["lkey"] = lkey
    pylist2json["lvalue"] = lvalue
    return jsonify(data = pylist2json)

if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=True)

