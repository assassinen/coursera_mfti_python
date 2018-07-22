import os
import tempfile
import argparse
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
# storage_path = 'storage.data'

def get_date():
    try:
        data = json.load(open(storage_path))
    except:
        data = {}
    return data


def get_key(args=None):
    data = get_date()
    if args.key in data:
        print(', '.join(data[args.key]))
    else:
        print(None)


def set_key(args):
    data = get_date()
    if args.key in data:
        data[args.key].append(args.val)
    else:
        data[args.key] = [args.val]

    with open(storage_path, 'w') as f:
        out = json.dumps(data, indent=4)
        f.write(out)


parser = argparse.ArgumentParser()
parser.add_argument("--key", help="key_name")
parser.add_argument("--val", help="value")
args = parser.parse_args()


if args.val and args.key:
    set_key(args)
elif args.key:
    get_key(args)
else:
    print("Не верный ввод.")