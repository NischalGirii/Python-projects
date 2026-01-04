class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def __str__(self):
        return f"Student: {self.name}, Average: {self.average():.2f}"

    def __len__(self):
        return len(self.marks)

    def __eq__(self, other):
        return self.name == other.name
