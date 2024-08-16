#!/bin/python3

n = "name"
h = "house"
p = "patronus"

students = [
    {n: "Hermoine", h: "Gryffindor", p: "Otter"},
    {n: "Harry", h: "Gryffindor", p: "Stag"},
    {n: "Ron", h: "Gryffindor", p: "Jack Russell Terrier"},
    {n: "Draco", h: "Slytherin", p: None},
]

for student in students:
    print(student[n], student[h], student[p], sep=", ")
