from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/recommend", methods=["POST"])
def recommend():
    name = request.form["name"]
    education = request.form["education"]
    interests = request.form["interests"].lower().split(",")
    results = recommend_careers(interests)


    return render_template("result.html", results=results)
from recommendation import recommend_careers
from career_data import careers
def get_student_data():
    name = input("Enter your name: ").title()
    education = input("Enter your education: ")
    interests = input("Enter your interests: ").lower().split(",")

    return name, education, interests
# name, education, interests = get_student_data()

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
# display_results(results)            
if __name__ == "__main__":
    app.run(debug=True)