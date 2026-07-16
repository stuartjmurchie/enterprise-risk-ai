def assess_risk(action):

    if "password" in action.lower():
        return {
            "risk": "HIGH",
            "impact": "HIGH",
            "likelihood": "HIGH",
            "reason": "Passwords are sensitive credentials."
        }

    elif "customer data" in action.lower():
        return {
            "risk": "HIGH",
            "impact": "HIGH",
            "likelihood": "MEDIUM",
            "reason": "Customer information must be protected."
        }

    return {
        "risk": "LOW",
        "impact": "LOW",
        "likelihood": "LOW",
        "reason": "No known risk indicators found."
    }


action = input("Describe an action: ")

result = assess_risk(action)

print("\nRisk Level:", result["risk"])
print("Impact:", result["impact"])
print("Likelihood:", result["likelihood"])
print("Reason:", result["reason"])