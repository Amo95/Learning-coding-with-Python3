# create a mapping of regions to abbreviation
regions = {
  'Greater Accra': 'G/A',
  'Volta': 'V/R',
  'Central': 'C/R'
}

# create a basic set of regions and some capitals in them
capitals = {
  'G/A': 'Accra',
  'C/R': 'Cape Coast',
  'V/R': 'Ho',
  'W/R': 'Sekondi-Takoradi',
  'N/R': 'Tamale'
}

# add some more regions
regions['Western'] = 'W/R'
regions['Northern'] = 'N/R'

# print out some capitals
print('-' * 10)
print("V/R region has:", capitals['V/R'])
print("N/R region has:", capitals['N/R'])

# print some regions
print('-' * 10)
print("Northern's abbreviation is:", regions['Northern'])
print("Volta's abbreviation is:", regions['Volta'])

# do it by using the regions then cities dict
print('-' * 10)
print("Volta has:", capitals[regions['Volta']])
print("Central has:", capitals[regions['Western']])

# print every regions abbreviation
print('-' * 10)
for region, abbrev in list(regions.items()):
        print(f"{region} is abbreviated {abbrev}")

# print every capitals in regions
print('-' * 10)
for abbrev, capital in list(capitals.items()):
        print(f"{capital} is the capital town for {abbrev}")

# now do both at the same time
print('-' * 10)
for region, abbrev in list(regions.items()):
        print(f"{region} region is abbreviated {abbrev}")

# safely get a abbreviation by regions that might not be there
print('-' * 10)
region = regions.get('Upper West')

if not region:
        print("Sorry, no Texas")

# get a capitals with a default value
capital = capitals.get('U/W', "Does Not Exist")
print(f"The city for the state 'U/W' is:", capital)
