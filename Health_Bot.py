 def analyze_bp(systolic, diastolic):
    if systolic < 90 or diastolic < 60:
        return "Low Blood Pressure (Hypotension). Consider consulting a doctor if you feel dizzy."
    elif 90 <= systolic <= 120 and 60 <= diastolic <= 80:
        return "Normal Blood Pressure. Keep up the healthy lifestyle!"
    elif 121 <= systolic <= 139 or 81 <= diastolic <= 89:
        return "Elevated Blood Pressure. Monitor your BP and consider lifestyle changes."
    else:
        return "High Blood Pressure (Hypertension). Please consult a doctor."


def analyze_fever(temp):
    if temp < 95:
        return "Low body temperature. Consider seeking medical advice if you feel unwell."
    elif 95 <= temp <= 99.5:
        return "Normal body temperature."
    elif 99.6 <= temp <= 100.9:
        return "Mild fever. Stay hydrated and rest."
    else:
        return "High fever. Consult a doctor if symptoms persist."


def analyze_blood_sugar(level, fasting=True):
    if fasting:
        if level < 70:
            return "Low blood sugar (Hypoglycemia). Eat something sugary and monitor your levels."
        elif 70 <= level <= 99:
            return "Normal fasting blood sugar level."
        elif 100 <= level <= 125:
            return "Prediabetes. Consider lifestyle changes and monitoring."
        else:
            return "High blood sugar (Diabetes). Consult a doctor."
    else:
        if level < 140:
            return "Normal post-meal blood sugar level."
        elif 140 <= level <= 199:
            return "Prediabetes. Monitor your diet and exercise."
        else:
            return "High blood sugar (Diabetes). Seek medical advice."


def chatbot():
    print("Welcome to the Health Analysis Chatbot!")

    while True:
        print("\nChoose a health parameter to analyze:")
        print("1. Blood Pressure")
        print("2. Body Temperature")
        print("3. Blood Sugar")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            systolic = int(input("Enter your systolic BP (upper number): "))
            diastolic = int(input("Enter your diastolic BP (lower number): "))
            print(analyze_bp(systolic, diastolic))

        elif choice == '2':
            temp = float(input("Enter your body temperature (°F): "))
            print(analyze_fever(temp))

        elif choice == '3':
            fasting = input("Is this a fasting blood sugar test? (yes/no): ").strip().lower() == 'yes'
            blood_sugar = int(input("Enter your blood sugar level (mg/dL): "))
            print(analyze_blood_sugar(blood_sugar, fasting))

        elif choice == '4':
            print("Thank you for using the chatbot! Stay healthy!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    chatbot()
