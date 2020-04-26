# Cryptography Project

The problem statement and its corresponding **.tex** file can be accessed from the **Problem Statement** directory.
The starter code (for the students) and complete codes (for the instructors) in C++, Java, and Python is available in the folders named accordingly. We recommed providing the Google drive or equivalent links to starter codes for each language in a zip file which the students can download. 

The code for creating test cases and grading submissions is available in the Tester directory. The file named **generateTestCases.py** can be used to generate the test cases. This script takes as input the usernames of students in a file named **names.txt** and generates the testcases for each student and corresponding Private keys for the Public keys generated in Test 1. The test cases for the students are saved in the directory named **testcases** and should be provided to the students. The Private keys for Test 1's evaluation are saved in the **res** directory and should be used by the instructors when grading the submissions.

The submissions can be graded by passing the following as input for each student:

**[username]**

**[Output of Test case 1]**

**[Output of Test case 2]**

These can be fed into the **evaluateResults.py** script which will evaluate whether a student's submission is correct or not.
