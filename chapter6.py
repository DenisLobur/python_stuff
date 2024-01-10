alien0 = {'color': 'green', 'points': 5}
print(alien0['color'])
print(alien0['points'])

print(alien0)

alien0['another'] = 0
print(alien0)
print(f"alien has {alien0['points']} points")
del alien0['color']
print(alien0.get('color'))

for key, value in alien0.items():
    print(f"{key}: {value}")

