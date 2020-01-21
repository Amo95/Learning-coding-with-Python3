# create a mapping of region to abbreviation
regions = {
  'Greater Accra': 'G/A',
  'Ashanti': 'A/R',
  'Eastern': 'E/R',
  'Volta': 'V/R',
  'Brong Ahafo': 'B/A'
}

# create a basic set of regions and some cities in them
cities = {
  'G/A': 'Accra',
  'E/R': 'Koforidua',
  'V/R': 'Ho'
}

# add some more cities
cities['B/A'] = 'Sunyani'
cities['A/R'] = 'Kumasi'

# print out some  cities
print('-' * 10)
print("E/R has:", cities['E/R'])
print("G/A has:", cities['G/A'])

# print some regions
print('-' * 10)
print("Greater Accra's abbreviation is:", regions['Greater Accra'])
print("Brong Ahafo's abbreviation is:", regions['Brong Ahafo'])

# do it by using the region then cities dict
print('-' * 10)
print("Eastern has:", cities[regions['Eastern']])
print("Ashanti has:", cities[regions['Ashanti']])

# print every state abbreviation
print('-' * 10)
for region,abbrev in list(regions.items()):
  print(f"{region} is abbreviated as {abbrev}")

# print every city in region
print('-' * 10)
for region, city in list(cities.items()):
  print(f"{region} has the city {city}")

# now do both at the same time
print('-' * 10)
for region, abbrev in list(regions.items()):
  print(f"{region} region is abbreviated {abbrev}")
  print(f"and has city {cities[abbrev]}")

# safely get a abbreviaton by region that might not be there
def test():
  print('-' * 10)
  region = regions.get('Western')

  if not region:
    print("Sorry, no Western")

  # get a city with a default value
  city = cities.get('W/R', "Does Not Exist")
  print(f"The city for the region 'Western'is: {city}")

test()

regions['Western'] = 'W/R'
cities['W/R'] = 'Sekondi-Takoradi'

test()
