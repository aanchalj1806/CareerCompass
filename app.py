from career_data import careers
# name = input("enter your name ").title()
# education = input("enter your education ")
# interests = input("enter your interests: ").lower().split(",")
# print(name)
# print(education)
# """if interest == 'coding':
#     career = "sofware devlopment"
# elif interest == 'design':
#     career = 'ui/ux designer'
# elif interest == 'business':
#     career = 'business analyst' 
# else:
#     career = 'not suitable career is found'
# print("recommended career: " , career)"""
# """-------------Dictionary------------"""

# """career = careers.get(interest , " no career is suitable")
# print("recommended career: " , career)"""

# """________________for """
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