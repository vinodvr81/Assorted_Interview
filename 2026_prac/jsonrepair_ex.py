from json_repair import repair_json
import json

string = """{
'a':{'name':'Vinod','age':45}
'a':{'name':'Vinod','age':45}
'a':{'name':'Vinod','age':45}
}"""

try:
    bad_json_string = json.loads(string)
    print(bad_json_string)
except json.JSONDecodeError as e:
    good_json_string = repair_json(string, return_objects=True)
    print(good_json_string, type(good_json_string))
    print(json.dumps(good_json_string))