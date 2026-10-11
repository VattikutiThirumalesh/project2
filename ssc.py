def main():
	"""Display an SSC 10th-grade marks list and summary."""
	student_name = input("Enter student name: ").strip()
	roll_number = input("Enter roll number: ").strip()

	subjects = ["First Language", "Second Language", "Mathematics",
				"Science", "Social Studies","Telugu"]
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

	total = sum(marks.values())
	percentage = total / len(subjects)
	result = "PASS" if all(mark >= 35 for mark in marks.values()) else "FAIL"

	print("\n" + "=" * 38)
	print("              SSC MARKS LIST")
	print("=" * 38)
	print(f"Name      : {student_name}")
	print(f"Roll No.  : {roll_number}")
	print("-" * 38)
	for subject, mark in marks.items():
		print(f"{subject:<20} {mark:>6.2f}")
	print("-" * 38)
	print(f"Total     : {total:.2f}/{len(subjects) * 100}")
	print(f"Percentage: {percentage:.2f}%")
	print(f"Result    : {result}")


if __name__ == "__main__":
	main()
