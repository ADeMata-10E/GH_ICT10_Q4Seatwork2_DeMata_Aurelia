from pyscript import document

class Classmate:
    def __init__(self, name, section, subject):
        self.name = name
        self.section = section
        self.subject = subject
    
    def introduce(self):
        return f"I am {self.name} from {self.section}. My favorite subject is {self.subject}."

subjects = ["English", "Math", "Science", "Philo", "Music", "Physical Education", "Filipino"]
sections = ["Emerald", "Sapphire", "Ruby", "Topaz"]

classmateNames = [ "Abayon", "Antes", "Apostol", "Banaag", "Barrientos", "Casal", "Coeli", "David", "De Mata", "Dela Cruz F", "Dela Cruz J", "Dellejero", "Fukuda",  "Gozum", 
"Ibay", "Lim", "Lozano", "Mamauag", "Navarro",
"Precones", "Ramos", "Sidhu", "Tiu", "Villamayor", "Zaragoza"]       

classmatePossibleTraits = [
    Classmate("Abayon", "Emerald", "English"),
    Classmate("Antes", "Sapphire", "Math"),
    Classmate("Apostol", "Ruby", "Science"),
    Classmate("Banaag", "Topaz", "Philo"),
    Classmate("Barrientos", "Emerald", "Music"),
    Classmate("Casal", "Sapphire", "Physical Education"),
    Classmate("Coeli", "Ruby", "Filipino"),
    Classmate("David", "Topaz", "English"),
    Classmate("De Mata", "Emerald", "Math"),
    Classmate("Dela Cruz F", "Sapphire", "Science"),
    Classmate("Dela Cruz J", "Ruby", "Philo"),
    Classmate("Dellejero", "Topaz", "Music"),
    Classmate("Fukuda", "Emerald", "Physical Education"),
    Classmate("Gozum", "Sapphire", "Filipino"),
    Classmate("Ibay", "Ruby", "English"),
    Classmate("Lim", "Topaz", "Math"),
    Classmate("Lozano", "Emerald", "Science"),
    Classmate("Mamauag", "Sapphire", "Philo"),
    Classmate("Navarro", "Ruby", "Music"),
    Classmate("Precones", "Topaz", "Physical Education"),
    Classmate("Ramos", "Emerald", "Filipino"),
    Classmate("Sidhu", "Sapphire", "English"),
    Classmate("Tiu", "Ruby", "Math"),
    Classmate("Villamayor", "Topaz", "Science"),
    Classmate("Zaragoza", "Emerald", "Philo")
]

def add_classmate(event):
    name = document.getElementById("name")
    section = document.getElementById("section")
    subject = document.getElementById("subject")

def displaylist(event):
    integrate = document.getElementById("listingspace")

    final_output = ""
    for classmate in classmatePossibleTraits:
        final_output += f"{classmate.introduce()}<br>"
    integrate.innerHTML = final_output

def add_classmate(event):
    student_name = document.getElementById("name")
    student_section = document.getElementById("section")
    favorite_subject = document.getElementById("subject")

    new_classmate = Classmate(student_name.value, student_section.value, favorite_subject.value)
    classmatePossibleTraits.append(new_classmate)

    #to clear afterwards

    student_name.value = ""
    student_section.value = ""
    favorite_subject.value = ""

   

