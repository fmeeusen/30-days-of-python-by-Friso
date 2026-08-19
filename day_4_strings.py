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