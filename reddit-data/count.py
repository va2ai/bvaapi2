import json, os
total = 0
d = 'C:/Users/ccdmn/code/bvaapi/reddit-data'
for f in sorted(os.listdir(d)):
    if f.endswith('.json'):
        with open(os.path.join(d, f), encoding='utf-8') as fp:
            data = json.load(fp)
        print(f'{f}: {len(data)} posts')
        total += len(data)
print(f'TOTAL: {total} posts')
