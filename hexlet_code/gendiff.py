import json


def generate_diff(filepath1, filepath2):
    with open(filepath1) as file1, open(filepath2) as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

    keys = sorted(set(data1.keys()).union(data2.keys()))
    
    diff = []
    
    for key in keys:
        if key in data1 and key not in data2:
            diff.append(f"- {key}: {json.dumps(data1[key])}")
        elif key not in data1 and key in data2:
            diff.append(f"+ {key}: {json.dumps(data2[key])}")
        elif data1[key] != data2[key]:
            diff.append(f"- {key}: {json.dumps(data1[key])}")
            diff.append(f"+ {key}: {json.dumps(data2[key])}")
        else:
            diff.append(f"  {key}: {json.dumps(data1[key])}")
    
    diff_str = "{\n"
    for line in diff:
        diff_str += f"  {line}\n"
    diff_str += "}\n"
    
    return diff_str
