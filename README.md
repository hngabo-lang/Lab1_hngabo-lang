# Lab1_hngabo-lang

# Submission Files


 1.grade evaluator.py: Python script that validates grades, calculates GPA, and determines pass or fail status
 2.organizer.sh: Bash script that archives grades.csv and resets the workspace

# Requirements

- Python 3
- Bash shell
- A grades.csv file in the same folder as the scripts

# grades.csv Format

The CSV file must be in the same folder as the scripts and follow this format:


assignment,group,score,weight
Quiz,Formative,85,20
Group Exercise,Formative,40,20
Functions and Debugging Lab,Formative,45,20
Midterm Project - Simple Calculator,Summative,70,20
Final Project - Text-Based Game,Summative,60,20

 assignment: Name of the assignment
 group: Formative or Summative
 score: Score between 0 and 100
 weight: Percentage weight total of 60 on Formative, and 40 on Summative


# How to Run the Python Script

#bash
python3 grade-evaluator.py


When prompted, enter the filename:

```
Enter the name of the CSV file to process (e.g., grades.csv): grades.csv
```

# What it does

A. Grade Validation: checks every score is between 0 and 100
B. Weight Validation: enforces Total=100, Formative=60, Summative=40
C. GPA Calculation: uses the formula `GPA = (Total Grade / 100) * 5.0`
D. Pass or Fail: student must score at or above 50% in both Formative and Summative categories to pass
E. Resubmission: identifies the failed formative assignment(s) with the highest weight. If multiple share the same highest weight, all are displayed

# Sample Output

```
   Processing Grades

  a.Grade Validation: All scores are within range (0-100).
  b.Weight Validation: Total=100, Formative=60, Summative=40.


              STUDENT GRADE TRANSCRIPT

  Assignment                          Group       Score Weight

  Quiz                                Formative     85  20%
  Group Exercise                      Formative     40  20%
  Functions and Debugging Lab         Formative     45  20%
  Midterm Project - Simple Calculator Summative     70  20%
  Final Project - Text-Based Game     Summative     60  20%

  Formative Score:                                 56.0%
  Summative Score:                                 65.0%
  Overall Weighted Total:                          60.0 / 100
  GPA:                                             3.0 / 5.0


  FINAL STATUS: PASSED

  ELIGIBLE FOR RESUBMISSION (highest-weight failed formative):
    Group Exercise  (score: 40.0, weight: 20.0%)
    Functions and Debugging Lab  (score: 45.0, weight: 20.0%)

## How to Run the Shell Script

```bash
chmod +x organizer.sh
./organizer.sh
```

# What it does

A. Creates an `archive/` directory if it does not exist
B. Generates a timestamp in the format `YYYYMMDD-HHMMSS`
C. Renames `grades.csv` to `grades_YYYYMMDD-HHMMSS.csv` and moves it into `archive/`
D. Creates a fresh empty `grades.csv` ready for the next batch of grades
E. Appends a log entry to `organizer.log` the log accumulates entries from every run

# Sample organizer.log entry

```
timestamp  : 20251105-170000
Original   : grades.csv
Archived to: archive/grades_20251105-170000.csv
```

# Folder Structure After Running Both Scripts

```
lab1_yourname/
 grade-evaluator.py
 organizer.sh
 README.md
 grades.csv         #fresh empty file (reset by organizer.sh)
 organizer.log      #log of every archival run
  archive
 grades_20251105-170000.csv
```


