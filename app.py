from career_data import careers
def get_student_data():
    name = input("Enter your name: ").title()
    education = input("Enter your education: ")
    interests = input("Enter your interests: ").lower().split(",")

    return name, education, interests
name, education, interests = get_student_data()
def recommend_careers(interests):
    results = []

    for interest in interests:
        interest = interest.strip()

        career = careers.get(interest, "no career found")

        if career != "no career found":
            results.append(career)

    return results


results = recommend_careers(interests)

print("\nRecommended Careers:")

def display_results(results):
    for career in results:
        print("\nCareer:", career["name"])

        print("Skills:")
        for skill in career["skills"]:
            print("-", skill)

        print("Roadmap:")
        for step in career["roadmap"]:
            print("-", step)
display_results(results)            