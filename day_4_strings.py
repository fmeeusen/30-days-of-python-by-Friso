space = ' '
string1 = 'Thirty' + space + 'Days'+ space + 'Of' + space + 'Python'
string2 = 'Coding' + space + 'For' + space + 'All'
company = string2
print(f'company {company}')
print(f'len(company) {len(company)}')
print(f'company.upper() {company.upper()}')
print(f'company.lower() {company.lower()}')
print(f'company.capitalize() {company.capitalize()}')
print(f'company.title() {company.title()}')
print(f'company.swapcase() {company.swapcase()}')
print(f'Cut out the first word: {company[7:]}')
print(f'Coding in Coding For all:  {'Coding' in company}')
print(f'company.find(Coding):  {company.find('Coding')!=-1}')
print(f'company.index(Coding):  {company.index('Coding')!=ValueError}')
print(f"company.replace('Coding', 'Python'), {company.replace('Coding', 'Python')}")
print(f"company.split(' '), {company.split(' ')}")
print(f" 'F, A, A, N, G'.split(','), {'F, A, A, N, G'.split(',')}")
print(f"company[0]: {company[0]}")
print(f"company[-1]: {company[-1]}")
print(f"company[10]: {company[10]}")
print(f"company.index('C'): {company.index('C')}")
print(company.index('F'))
print(company.rfind('l'))
conjuction_string = 'You cannot end a sentence with because because because is a conjunction'
print(conjuction_string.index('because'))
print(conjuction_string.find('because'))
print(conjuction_string.rindex('because'))
print(conjuction_string.replace('because ', ''))
print(conjuction_string.replace('because ', ''))
print(f"Does {conjuction_string} start with 'Coding':{conjuction_string.startswith('Coding')}")
print(f"Does {company} end with 'coding':{conjuction_string.endswith('coding')}")
print(f"Does {company} start with 'Coding':{conjuction_string.startswith('Coding')}")
print("  Coding For All  ".strip('  '))
print(f'30DaysOfPython is an indentifier: {'30DaysOfPython'.isidentifier()}' )
print(f'thirty_days_of_python is an indentifier: {'thirty_days_of_python'.isidentifier()}' )
python_libraries =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(python_libraries))
print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")