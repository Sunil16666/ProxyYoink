import json

a = [[('x1', 'y1', ['z1']), ('x2', 'y2', ['z2'])], [('x3', 'y3', ['z3']), ('x4', 'y4', ['z4'])]]
b = [
    f"{protocol}://{ip}:{port}"
    for sublist in a
    for ip, port, protocols in sublist
    for protocol in protocols
]

with open('raw_proxies.txt', 'w') as f:
    for proxy in b:
        f.write(proxy + '\n')
