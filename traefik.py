import requests
import re
import argparse

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('api', nargs='+')
args = parser.parse_args()

match1 = re.compile(r"Host\(((?:`[^`]*`,?)*)\)")

def parse_rule(rule):
    domains = []
    parts = re.split('(\|\||&&)', rule)
    for part in parts:
        res = parse_rule_part(part.strip())
        if res != None:
            domains.extend(res)
    return domains

def parse_rule_part(part):
    host = re.match(match1, part)
    if host:
        return parse_host(host.group(1))

def parse_host(host):
    host = host.split(',')
    return [domain[1:-1] for domain in host]

for api in args.api:
    r = requests.get('%s/http/routers' % api)
    for l in r.json():
        print(parse_rule(l['rule']))
