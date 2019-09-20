import pandas as pd
#problem 2a:
df = pd.read_csv('df.csv')#inport all the data
female = df.female#seperate different data
male = df.male  
femalesurvival=df.femalesurvival
malesurvival=df.malesurvival


length=len(df)-1

femalesurvival.iloc[0]=1
malesurvival.iloc[0]=1

for i in range(length):
       femalesurvival.iloc[i+1]=femalesurvival.iloc[i]*(1-female.iloc[i])
       malesurvival.iloc[i+1]=malesurvival.iloc[i]*(1-male.iloc[i])

print (df.head(5))


#problem 2b:
age=30
term=10
payout=10000


premium=0
for i in range(term):
    premium=premium+payout/(pow(1.02,2*i+1))*(malesurvival.iloc[age+i]-malesurvival.iloc[age+i+1])/malesurvival.iloc[age]

print('A',age, 'year-old man should pay a lumpsum of',premium, 'dollars for a', term,'year insurance with a payout of',payout,'dollars.')

print('')
      
premium=0
for i in range(term):
    premium=premium+payout/(pow(1.02,2*i+1))*(femalesurvival.iloc[age+i]-femalesurvival.iloc[age+i+1])/femalesurvival.iloc[age]

print('A',age, 'year-old woman should pay a lumpsum of',premium, 'dollars for a', term,'year insurance with a payout of',payout,'dollars.')

