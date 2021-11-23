"""
  json形式
  以下、内容を想定
  {
    "employee":
    [
      {"id":100, "name": "Mike"},
      {"id":200, "name": "Tom"}
    ]
  }
"""
import json

# json_text = {
#     "employee":
#     [
#         {"id": 100, "name": "Mike"},
#         {"id": 200, "name": "Tom"}
#     ]
# }

# print(json_text)
# print('############')
# # jsonの形式で出力していく
# print(json.dumps(json_text))
# print('############')
# ファイル書き込み
# with open('test.json', 'w') as json_file:
#     json.dump(json_text, json_file)

# ファイル読み込み
with open('test.json', 'r') as json_file:
  # ファイルの中身を全部取得する
    json_values = json.load(json_file)
    print(json_values)
    # jsonファイルのキーを取得する(第一引数)
    for json_key in json_values:
        print(json_key)

    # jsonファイルの値を取得する
    for json_values in json_values.values():
        print(json_values)
        for json_value in json_values:
          # keyのみ取得したい場合
            # for key in json_value.keys():
          # valueのみ取得したい場合
            # for value in json_value.values():
          # key,valueを取得したい場合
            for key, value in json_value.items():
                print(key, value)
