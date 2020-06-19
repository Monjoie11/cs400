import random
import datetime as lies

randy1 = random.random()

randy2 = random.uniform(1,10)

ages = int(random.uniform(1,3000))

twelv1 = int(random.uniform(1, 13))

twelv2 = int(random.uniform(1, 13))

twelv3 = int(random.uniform(1, 13))

sixti1 = int(random.uniform(1,61))

sixti2 = int(random.uniform(1,61))

thedate = lies.datetime(ages, twelv1, twelv2, twelv3, sixti1, sixti2)

print(thedate)


print(randy1, randy2)