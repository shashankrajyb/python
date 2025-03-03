def functions(x,*y,z=100):
    print(x)
    print(y)
    print(z)
functions(10 ,20,30,40,60)
functions(10,20,30,40)
functions(10,20,30,z=100)

def patient(*diseases,emailid='nomailid',**kwargs,):
        print('Diseases:',diseases)
        print('Email_id=',emailid)
        for i, j in kwargs.items():
            print(i, '=', j)


patient('fever','headache','bodypains',emailid='ten@gmail.com',patient_name='Raj',blood_group='o+')

def hosp(name,blood_group,*diseases,email='not provied'):
    print(name)
    print(blood_group)
    for i in diseases:
        print(i,end='')
        print(email)
hosp('Raj','o+','fever',email='raj@gmail.com')

def institue(Student_name,*address,**Email_id):
    print(Student_name)
    print(Email_id)
    print(address)
institue('Raj','Yelhanka','raj@gmail.com','tenen@gmail.com')
