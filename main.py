age = int(input())
month = 0
year = 0

while(age != 0):
  while age >= 365:
    age -= 365
    year += 1
  while age >= 30:
    age -= 30
    month +=1
    
  days = age
  age = 0
print(f"""{year} ano(s)
{month} mes(es)
{days} dia(s)""")