#multi -level inheritance
class person:
        def name(self):
            print('name-------')
class teacher(person):
    def qualification(self):
         print('phd')
class hod(teacher):
     def experience(self):
          print('experience-------- 15 yrs')
obj=hod()
obj.name()
obj.qualification()
obj.experience()
