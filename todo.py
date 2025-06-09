import requests
import random


res = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = res.json()

# Создаем список цитат с помощью цикла
not_done = []
for todo in todos:
    if not todo["completed"]:
        not_done.append(todo)

print("10 цитат с False (todo):")
if len(not_done) < 10:
    print("Конец")
else:
    for todo in random.sample(not_done, 10):
        print(f'- {todo["title"]}')