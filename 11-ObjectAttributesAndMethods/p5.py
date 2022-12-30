class person:
    last_id = 225565
    univeristy + "UEK Krakow"
    def __init__(self, name, surname, id, field_of_study, university):
        self.name = name
        self.surname = surname
        self.id = person.last_id
        person.last_id += 1
        self.field_of_study = field_of_study
    def __str__(self):
        return f"Performer: {self.name}\nstudent: {self.id}\nfield of study: {self.field_of_study}\nuniversity: {self.university}"

student1 = person("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
student2 = person("Disclosure", "White Noise", "Settle", 2013)
student3 = person("Mike Gordon", "At Doom's Gate", "Doom OST", 2016)
print(student1,"\n\n",student2,"\n\n",student3)