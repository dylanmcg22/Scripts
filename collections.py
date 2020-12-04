dylan = {}
dylan['first'] = 'Dylan'
dylan['last'] = 'McGrath'

john = {}
john['first'] = 'John'
john['last'] = 'Terry'

people = []
people.append(dylan)
people.append(john)
people.append({
    'first': 'Bill', 'last': 'Gates'
})

print(people)