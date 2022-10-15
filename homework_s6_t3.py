'''
3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
in
"Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

out

{'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}
'''



def create_dictionary(list_keys, list_evaluation):
    dic = {}
    for i in range(len(list_evaluation)):
        k = list_keys[i]
        if k not in dic:
            dic[k] = list_evaluation[i]
        else: dic[k] += f', {list_evaluation[i]}'
    return dic

names_str = (input("Введите имена через пробел: ")).split()
names_list = ' '.join(sorted(names_str))
names_keys = ([w[0] for w in names_list.split()])
print(f'{names_list}\n{names_keys}')
print(create_dictionary(names_keys, names_list.split()))
