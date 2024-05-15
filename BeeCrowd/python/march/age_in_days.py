age = int(input())

in_years = age//365
in_months = (age%365) // 30
in_days = (age%365) % 30

print("{} ano(s)".format(in_years))
print("{} mes(es)".format(in_months))
print("{} dia(s)".format(in_days))