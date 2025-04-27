import json

with open("table.json", "r") as f:
    c = f.read()
    j = json.loads(c)
    outf = open(f'syscall_{j["kernel"]["abi"]["name"]}_{j["kernel"]["version"]}.h', 'w')
    result = ["enum SYSCALLS{\n"]

    for syscall in j["syscalls"]:
        result.append(f'{syscall["name"]} = {syscall["number"]} ,\n')

    result.append("}")
    outf.writelines(result)
    outf.close()
