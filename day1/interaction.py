name = raw_input("name: ")
age = int(raw_input('age: '))
job = raw_input("job: ")
salary = raw_input("salary:")

info = '''
-----------info of %s---------
name:%s
age:%d
job:%s
salary:%s
''' % (name,name,age,job,salary)

info2 = '''
-----------info of {_name}---------
name:{_name}
age:{_age}
job:{_job}
salary:{_salary}
''' .format (_name=name,
             _age=age,
             _job=job,
             _salary=salary)

info3 = '''
-----------info of {0}---------
name:{0}
age:{1}
job:{2}
salary:{3}
''' .format (name,age,job,salary)

print info3