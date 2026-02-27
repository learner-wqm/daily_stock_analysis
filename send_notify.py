import os
import requests
import glob

token = os.environ.get('PUSHPLUS_TOKEN')
if not token:
    print('PushPlus token not found')
    exit(0)

files = glob.glob('reports/*')
if not files:
    print('No report files found')
    exit(0)

latest = max(files, key=os.path.getctime)
print(f'Found report: {latest}')

with open(latest, 'r', encoding='utf-8') as f:
    content = f.read()[:8000]

resp = requests.post('http://www.pushplus.plus/send', json={
    'token': token,
    'title': '📈 每日股票分析报告',
    'content': content,
    'template': 'txt'
}, timeout=30)

print(f'PushPlus response: {resp.json()}')