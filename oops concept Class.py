class student:

    def getData(self,fname,lname,sname,ename):
        self.f=fname
        self.l=lname
        self.s=sname
        self.e=ename
    def putData(self):
        print("First Name : ",self.f)
        print("Last Name : ",self.l)
        print("Subject Name : ",self.s)
        print("Email : ",self.e)

s1=student()
s1.getData("vipul","memakiya","Account","vmmemakiya22@gmail.com")
s1.putData()
