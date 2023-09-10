student  = {


    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

students = [
    {
        "name": "Hermione",
        "house": "Gryffindor",
        "patronous": "Otter"
    },
        {
        "name": "Harry",
        "house": "Gryffindor",
        "patronous": "Stag"
    },
    {
        "name": "Ron",
        "house": "Gryffindor",
        "patronous": "Jack Russell terrier"
    },
    {
        "name": "Hermione",
        "house": "Gryffindor",
        "patronous": "Otter"
    },
    {
        "name": "Draco",
        "house": "Slytherin",
        "patronous": None
    }
]

for student in students:
    print(student["name"], student["house"], sep=", ")