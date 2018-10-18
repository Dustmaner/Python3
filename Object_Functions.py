from Student import Studentt

student1 = Studentt("Vane", "Lancer", 3.1)
student2 = Studentt("Lancelot", "Dual-Sword", 3.8)

print(student1.on_honor_roll())
print(student2.on_honor_roll())
student2.gpa = 1.5
print(student2.on_honor_roll())
