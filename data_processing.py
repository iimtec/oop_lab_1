import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
print("All cities in Germany:")
g_city = []
for city in cities:
    if city['country'] == 'Germany':
        g_city.append(city)
print(g_city)
print()

# Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with temperature above 12°C:")
s_city = []
for city in cities:
    if city['country'] == 'Spain' and float(city['temperature']) > 12:
        s_city.append(city)
print(s_city)
print()

# Count the number of unique countries
print("Number of unique countries")
countries = []
for city in cities:
    if city['country'] not in countries:
        countries.append(city['country'])
    elif city['country'] in countries:
        pass
print(len(countries))
print()

# Print the average temperature for all the cities in Germany
print("The average temperature of cities in Germany")
temp = []
for city in cities:
    if city['country'] == 'Germany':
        temp.append(float(city['temperature']))
print(f"{sum(temp)/len(temp):.2f}")
print()

# Print the max temperature for all the cities in Italy
print("Max temperature of the Italy")
temp = []
for city in cities:
    if city['country'] == 'Italy':
        temp.append(float(city['temperature']))
print(max(temp))