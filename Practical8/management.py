class patients(object):
    def __init__(self, name, age, date, history):
        self.name = name
        self.age = age
        self.date = date
        self.history = history

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Height: {self.date}, Weight: {self.history}"
    
#examle
example = patients("Li Hua", 30, "2023-10-01", "No significant history")
print(example)