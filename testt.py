class event_booking():
    def __init__(self):
        self.institution_count = {}
        self.student_info = []
        self.institution_day = {}
        self.day_institution = {'day1':[],
                                'day2':[],
                                'day3':[]}
       
    def students_attending_institution(self,institution,no_of_students):
        self.institution_count[institution] = {'students':no_of_students}
 
        self.institution_day[institution] = {'day1':0,
                                             'day2':0,
                                             'day3':0}
       
    def student_registration(self,register_no,name,institution):
        self.student_info.append([register_no,name,institution])
       
    def slot_booking(self,register_no,name,institution,day):
 
 
        if day == 'day1':
            if self.institution_day[institution]['day1'] < (self.institution_count[institution]['students'])/2:
                self.institution_day[institution]['day1']+=1
                self.day_institution['day1'].append(register_no)
            else:
                print('day 1 slots are filled please choose next day')
 
        if day == 'day2':
            if self.institution_day[institution]['day2'] < (self.institution_count[institution]['students'])/2:
                self.institution_day[institution]['day2']+=1
                self.day_institution['day2'].append(register_no)
            else:
                print('day 2 slots are filled please choose next day')
 
        if day == 'day3':
            if self.institution_day[institution]['day3'] < (self.institution_count[institution]['students'])/2:
                self.institution_day[institution]['day3']+=1
                self.day_institution['day3'].append(register_no)
 
 
    def count_of_students(self):
       for institution, details in self.institution_count.items():
        print(f"Number of students from {institution} is: {details['students']}")
 
 
    def day_display(self, day):
        if day in self.day_institution:
            print(f"Students registered for {day}: {self.day_institution[day]}")