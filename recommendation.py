from career_data import careers
def recommend_careers(interests):
    results = []
    for interest in interests:
        interest = interest.strip()
        career = careers.get(interest, "no career found")
        if career != "no career found":
            results.append(career)
    return results
    
        

     