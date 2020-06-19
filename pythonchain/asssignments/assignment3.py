theFeds = [
    {'name': 'Trump', 'age': 78, 'hobbies': ['racism', 'treason', 'self adoration']},
    {'name': 'McConnell', 'age': 987, 'hobbies': ['hail satan', 'hail beelzebub', 'macramae']},
    {'name': 'Kushner', 'age': 44, 'hobbies': ['larceny', 'theft', 'patriphilia']},
    {'name': 'Putin', 'age': 55, 'hobbies': ['running stuff', 'owning the US', 'watching pee vids']}
    ]


allstars = [person['name'] for person in theFeds]

print(allstars)

damnOld = all([person['age'] > 20 for person in theFeds])

print(damnOld)

moreFeds = theFeds[:]

d = {'why' : 7}



evenMoreFeds = [humanwaste.copy() for humanwaste in moreFeds]

for zombie in evenMoreFeds:
   zombie['name'] = 'thrall' 

print(moreFeds)

print(evenMoreFeds)

print(theFeds)

for scum in theFeds:
    a, b, c  = scum.items()
    print(a, b, c)



