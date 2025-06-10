import requests 
import random #импортирую модуль, чтобы случайным образом выбирать элементы.


res = requests.get("https://jsonplaceholder.typicode.com/todos") #получаем данные с сайта
todos = res.json() #переводит полученые данные в список словарей (ключ-значение)

# Создаю список цитат, которые не выполнены с помощью цикла
not_done = []
for todo in todos:
    if not todo["completed"]:
        not_done.append(todo) #если цитата "completed" = "false" добавляем ее в новый список not_done

print("10 цитат с False (todo):") #выводит заголовок
if len(not_done) < 10:  #проверяет, есть ли 10 цитат в списке not_done с "false"
    print("Конец")    #если цитат меньше 10 выводить "конец"
else:
    for todo in random.sample(not_done, 10):   #иначе выбираем 10 случайных цитат из списка
        print(f'- {todo["title"]}')  #выводит 10 случайных цитат и их названия(текст) "title"                
