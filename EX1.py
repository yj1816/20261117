menu = {
    '珍奶': {'price': 60, 'store': 5},
    '紅茶': {'price': 30, 'store': 3},
    '冬瓜茶': {'price': 25, 'store': 6},
}

order = [
    ('小美', '珍奶', 2),
    ('阿明', '紅茶', 2),
    ('小華', '珍奶', 3),
    ('小美', '紅茶', 2),
    ('阿明', '冬瓜茶', 4),
    ('小華', '紅茶', 1),
    ('小美', '珍奶', 1),
]

money = 0
person_money = {'小美': 0, '阿明': 0, '小華': 0}
reject = []

for person, drink, count in order:
  if menu[drink]['store'] >= count:
    menu[drink]['store'] -= count
    cost = menu[drink]['price'] * count
    money += cost
    person_money[person] += cost
  else:
    reject.append(f'{person}-{drink}')

left_store = {}
for drink in menu:
  left_store[drink] = menu[drink]['store']

king = ''
max_money = -1
for person, total in person_money.items():
  if total > max_money:
    max_money = total
    king = person

print('冰箱剩餘庫存：', left_store)
print('今晚賺了多少錢：', money)
print('三位常客各花了多少：', person_money)
print('被婉拒的訂單：', reject)
print('今晚消費王：', king)
