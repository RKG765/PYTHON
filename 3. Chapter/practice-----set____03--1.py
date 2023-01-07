# a = (''' Dear Raj Kumar,\n \tYou are selected for Covid-21 Test.\n\t\t Date : 23/04/2021''')
a = ''' Dear <|Name|>
We are happy to tell you that,
You are selected!
Lots of regards from our company,
ABC company,
And have a great journey ahead with our company.
       <|date|>'''
Name = input("Enter your Name:\n" )
date = input("enter date:\n")
a = a.replace("<|Name|>", Name)
a = a.replace("<|date|>", date)
print(a)