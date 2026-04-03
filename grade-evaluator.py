# Reads student grade data found in grades.csv, validates the data,calculates the final their GPA, decides pass or fail status, and suggest assignments allowd for resubmission.


import csv
import sys
import os

# FIRST PART loads the
def load_csv_data():
   # Ask the user to enter the file name to open
    fl_name = input("Enter the name of the CSV file to process (e.g., grades.csv): ")

  # Stop the program as long as the file don't exist
    if not os.path.exists(fl_name):
        print("File not found.")
        sys.exit(1)

   # Create empty list to store each row as dictionary
    assignmts = []

    try:
        with open(fl_name, mode='r') as file:
            lines = file.readlines()     
   # Loop through every row and save it
            for line in lines[1:]:
                parts = line.strip().split()
                weight = parts[-1]
                score = parts[-2]
                group = parts[-3]
                assignment = ' '.join(parts[:-3])
                assignmts.append({
                    'assignment': assignment,
                    'group': group,
                    'score': float(score),
                    'weight': float(weight)
                })
        return assignmts
    except Exception as e:
        print("file can not be read.", e)
        sys.exit(1)

  # SECOND PART: validate and evaluate the grades

def evaluate_grades(data):
    print("\nProcessing Grades")

    if len(data) == 0:
        print("file empty.")
        sys.exit(1)

    # check scores
    for item in data:
        if item['score'] < 0 or item['score'] > 100:
            print("Score must be in range of 0 to 100")
            return

    # check weights
    ttl_weight = 0
    frmt_weight = 0
    sumt_weight = 0

    for item in data:
        ttl_weight += item['weight']

        if item['group'] == "Formative":
            frmt_weight += item['weight']
        elif item['group'] == "Summative":
            sumt_weight += item['weight']

    if round(ttl_weight, 2) != 100:
        print("Total weight must be 100")
        return

    if round(frmt_weight) != 60:
        print("Formative weight must be 60")
        return

    if round(sumt_weight) != 40:
        print("Summative weight must be 40")
        return

    # calculate scores
    total = 0
    formt_score = 0
    sumt_score = 0

    for item in data:
        result = (item['score'] * item['weight']) / 100
        total += result

        if item['group'].strip().lower() == "formative":
            formt_score += result
        elif item['group'].strip().lower() == "summative":
            sumt_score += result

   # GPA formula
    gpa = (total / 100) * 5

    # pass or fail
    formt_pct = (formt_score / frmt_weight) * 100
    sumt_pct = (sumt_score / sumt_weight) * 100

    if formt_pct >= 50 and sumt_pct >= 50:
        status = "PASS"
    else:
        status = "FAIL"

    # resubmission
    fld = []
    for item in data:
        if item['group'] == "Formative" and item['score'] < 50:
            fld.append(item)
   # Finds the highest weigth in fails
    resubmit = []

    if len(fld) > 0:
        max_w = 0
        for item in fld:
            if item['weight'] > max_w:
                max_w = item['weight']

        for item in fld:
            if item['weight'] == max_w:
                resubmit.append(item)

    # print results
    print("Total:", round(total, 2))
    print("Formative Score:", round(formt_score, 2))
    print("Summative Score:", round(sumt_score, 2))
    print("GPA:", round(gpa, 2))
    print("Status:", status)

    if status == "FAIL" and len(resubmit) > 0:
        print("Resubmit:")
        for item in resubmit:
            print(item['assignment'])

# The start of system
if __name__ == "__main__":
 # Loads the csv
    course_data = load_csv_data()
 # Validate and evaluate the grades
    evaluate_grades(course_data)


