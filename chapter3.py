message = 'Hello python'
print(message)
message = 'Hello python crash course'
print(message.title())
print(message.upper())
print(message.lower())

first_name = "Ada"
last_name = "Lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
favourite_language = 'python    '
print(len(favourite_language.rstrip()))

no_starch_url = "https://nostarch.com"
print("no_starch_url " + no_starch_url)
print("no prefix " + no_starch_url.removeprefix("https://"))
print(no_starch_url)

bicycles = ['one', 'two', 'three', 'four', 'five']
print(bicycles)
print(bicycles[-2].title())
bicycles.append('six')
print(bicycles)
bicycles.insert(0, 'inserted')
print(bicycles)
del bicycles[0]
print(bicycles.pop(1))
bicycles.remove('three')
print(bicycles)
bicycles.remove('one')
bicycles.remove('four')
bicycles.remove('five')
bicycles.remove('six')
print(bicycles.sort())
