n = input().strip()
for i in '02356789':
  if i in n:
    print('NO')
    break
else:
  if '444' in n:
    print('NO')
  elif n[0] == '4':
    print('NO')
  else:
    print('YES')
