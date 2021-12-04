midterms = [80,91,78]
finals = [98,89,53]
students = ["dan","ang","kate"]

grades = list(zip(students,map(lambda x: max(x),zip(midterms,finals))))
print(grades)