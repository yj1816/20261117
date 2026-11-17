student = [
    {'id': 'd10', 'dept': 'AITA', 'ch': 95, 'math': 65, 'python': 90},
    {'id': 'd11', 'dept': 'CSIE', 'ch': 85, 'math': 72, 'python': 83},
    {'id': 'd12', 'dept': 'AITA', 'ch': 96, 'math': 83, 'python': 75},
    {'id': 'd13', 'dept': 'CSIE', 'ch': 70, 'math': 91, 'python': 94},
    {'id': 'd14', 'dept': 'AITA', 'ch': 88, 'math': 60, 'python': 79},
]
print(student[1])

print('-' * 20)

for s in student:
  avg = round((s['ch'] + s['math'] + s['python']) / 3, 2)
  s['avg'] = avg
  print(f"學號: {s['id']}, 科系: {s['dept']}, 平均: {s['avg']:.2f}")

print('-' * 20)

aita = 0
csie = 0
aita_avg = 0
csie_avg = 0
aita_max = 0
aita_top = ''
csie_max = 0
csie_top = ''

for s in student:
  if s['dept'] == 'AITA':
    aita += 1
    aita_avg += s['avg']
    if s['avg'] > aita_max:
      aita_max = s['avg']
      aita_top = s['id']
  elif s['dept'] == 'CSIE':
    csie += 1
    csie_avg += s['avg']
    if s['avg'] > csie_max:
      csie_max = s['avg']
      csie_top = s['id']

aita_final = round(aita_avg / aita, 2)
csie_final = round(csie_avg / csie, 2)

print(f'AITA: {aita}人, 全系平均: {aita_final:.2f}, 最高分: {aita_top}')
print(f'CSIE: {csie}人, 全系平均: {csie_final:.2f}, 最高分: {csie_top}')
