name = input("enter the name: ")
rollnumber = input("enter your rollnumber: ")

subjects = [
	"First Language",
	"Second Language",
	"Mathematics",
	"Science",
	"Social Studies",
	"Telugu",
]


def get_grade(mark):
	if mark >= 90:
		return "A1"
	if mark >= 80:
		return "A2"
	if mark >= 70:
		return "B1"
	if mark >= 60:
		return "B2"
	if mark >= 50:
		return "C1"
	if mark >= 40:
		return "C2"
	if mark >= 30:
		return "D"
	return "F"


marks = {}
for subject in subjects:
	while True:
		try:
			mark = float(input(f"Enter marks for {subject} (0-100): "))
			if 0 <= mark <= 100:
				marks[subject] = mark
				break
			print("Marks must be between 0 and 100.")
		except ValueError:
			print("Please enter a valid number.")

print(f"Enter your Name:{name}")
print(f"Eter your Roll number :{rollnumber}")
print("\nSSC 10th Marks and Grades")
print("-" * 35)
total = 0
for subject, mark in marks.items():
	print(f"{subject}: {mark:g} - Grade {get_grade(mark)}")
	total += mark

print("-" * 35)
print(f"Total: {total:g}/600")
print(f"Percentage: {total / 6:.2f}%")
