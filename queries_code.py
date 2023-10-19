
# Name, email, college and phone number
#done...


#Name : Gagandeep Singh
#Email : singhgagandeep8056@gmail.com
#College : Guru Nanak Dev Univerity (Amritsar)
#Phone no. : 7888742774


# Also mention the sum(land) for Anjali Devi and Suraj Kumar in comment in the code. Output should be correct and match with your code output.
#done...
#sum(land) for anjali : ans : 12
#sum(suraj kumar) : ans : 62






class LandRecord:
    def __init__(self, name, father, land):
        self.name = name
        self.father = father
        self.land = land

class LandRegistry:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def select_records(self, query):
        results = []
        if query.startswith("Select * from LR where name ="):
            name = query.split("'")[1]
            results = [record for record in self.records if record.name == name]
        elif query.startswith("Select Sum(Land) from LR where name ="):
            name = query.split("'")[1]
            land_sum = sum(record.land for record in self.records if record.name == name)
            results.append((land_sum,))
        elif query.startswith("Select * from LR where FamilyTree ="):
            name = query.split("'")[1]
            results = [record for record in self.records if self.is_family_tree(record, name)]
        elif query.startswith("Select Sum(Land) from LR where FamilyTree ="):
            name = query.split("'")[1]
            land_sum = sum(record.land for record in self.records if self.is_family_tree(record, name))
            results.append((land_sum,))
        return results

    def is_family_tree(self, record, target_name):
        if record.name == target_name:
            return True
        elif record.father and self.is_family_tree(record.father, target_name):
            return True
        return False

# Parsing the statements
statements = [
    "Mr. Arun Kumar S/o Mr. Suraj Kumar has purchased 10 acres of land.",
    "Mr. Amit Kumar S/o Mr. Arun kumar has purchased 15 acres of land.",
    "Mr. Ram Kumar S/o Mr. Arun kumar and Mr. Amit Kumar S/o Mr. Arun kumar have purchased 20 acres of land.",
    "Mrs. Anjali Devi W/o Mr. Amit Kumar has purchased 12 acres of land.",
    "Mr. Manish Kumar S/o Mrs. Anjali Devi has purchased 17 acres of land.",
    "Mr. Amit Kumar S/o Mr. Arun kumar has sold 10 acres of land.",
    "Mr. Manish Kumar S/o Mr. Amit Kumar and Ms. Priya D/o Mrs. Anjali Devi have purchased 20 acres of land.",
    "Mr. Ram Kumar S/o Mr. Arun kumar and Mr. Amit Kumar S/o Mr. Arun kumar have sold 10 acres of land."
]

registry = LandRegistry()

for statement in statements:
    parts = statement.split()
    name = parts[1]
    father_name = parts[3] if "S/o" in statement else None
    land = int(parts[-4])
    father_record = next((record for record in registry.records if record.name == father_name), None)
    record = LandRecord(name, father_record, land)
    registry.add_record(record)

# Executing queries
query1 = "Select * from LR where name = 'Arun Kumar'"
query2 = "Select Sum(Land) from LR where name = 'Anjali Devi'"
query3 = "Select * from LR where FamilyTree = 'Amit Kumar'"
query4 = "Select Sum(Land) from LR where FamilyTree = 'Suraj Kumar'"

results1 = registry.select_records(query1)
results2 = registry.select_records(query2)
results3 = registry.select_records(query3)
results4 = registry.select_records(query4)

# Printing results
print("Query 1 Results:")
for result in results1:
    print(f"Name: {result.name}, Land: {result.land}")

print("\nQuery 2 Results:")
print(f"Total Land for Anjali Devi: {results2[0][0]} acres")

print("\nQuery 3 Results:")
for result in results3:
    print(f"Name: {result.name}, Land: {result.land}")

print("\nQuery 4 Results:")
print(f"Total Land for Suraj Kumar's Family: {results4[0][0]} acres")

