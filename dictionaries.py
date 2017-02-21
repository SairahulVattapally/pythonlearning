states= {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities= {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' :'Jacksonsville'

}

cities['NY']='New York'
cities['OR']='Portland'

print '-'*20
print "NY state has: ",cities['NY']
print "OR state has: ",cities['OR']

print '-'*20
print "Michigan state abbreviation is: ", states['Michigan']
print "California state abbreviation is: ", states['California']

print "-"*20
print "Michigan has:", cities[states['Michigan']]
print "California has: ", cities[states['California']]

print "-"*20
for state, abbrev in states.items():
    print "%s state is abbreviated as %s" %(state,abbrev)

print "-"*20
for abbrev,city in cities.items():
    print "%s state has %s"%(abbrev,city)

print "-"*20
for state,abbrev in states.items():
    print "%s state is abbreviated as %s, has a city %s"%(state,abbrev,cities[abbrev])
