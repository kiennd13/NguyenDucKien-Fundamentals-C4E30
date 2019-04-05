inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
inventory["pocket"] = ['seashell','strange berry','lint']
ds = []
for v in inventory['backpack']:
    ds.append(v)
del ds[1]
inventory['backpack'] = ds
inventory['gold'] += 50
print(inventory)
