def student_report(name, age, /, *, grade, school):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Grade: {grade}")
    print(f"School: {school}")

def project_details(title, *technologies, **info):
    print(f"Project Title: {title}")
    print(f"Technologies: {technologies}")
    print(f"Info: {info}")

student_report("Faiyaz", 23, grade="A+", school="BRAC University")

project_details(
    "AI Assistant",
    "Python", "TensorFlow", "React",      
    duration="6 months", team_size=5       
)