# Python-Programming Building an Interactive Grading System-
This repository focuses on solving the most common pressing questions with Python programming. 

# Introdution 
Building a grading system is crucial for various educational institutions for easy retrieval and analysis of results. Building an interactive and robust grade system saves time and provides flexibility to adapt to changes. This repository focuses on building such an interactive grade system that can perform diverse activities and be changed when needed. 

# Challenge 
Using Python programming language, I built an interactive grading system that accepts assignments, homework, and three exam inputs to compute any student's course grade. The program begins with an introduction and what it can achieve. The program considers three tests, the mid-term 1 exam, mid-term 2 exam, homework, and final exams. Each of these tests is weighted differently but the final grade should be out of 100. The weights are provided by the user through a prompt. 

## Mid Term 1
The program requests the mid-term 1 scores and also asks if the exam was shifted or not (1 if it was shifted and 0 otherwise). In case of a shift the program further asks the amount shifted and adds the shifted scores to the mid-term 1 scores. All the mid-term scores were capped at 100. Note the shift might be large enough to make the scores above 100. For instance, the student exam scores might be 95, and the shift amount is 10 this makes the exam scores 105 so the student's mid-term exam will be capped at 100 instead. 
The same procedure is applied for mid-term 2. 

## Homework 
The next prompt is about the user's homework information including the weight for the homework. Note there might be more than 1 homework for different students so the program was built to make sure it's flexible to suit each needs. For each homework, the user has to enter the homework score and points possible and also weights at the start of the program prompt. The cumulative sum was used to calculate the final homework score. Another important information is that some part of the homework score comes from the sessions attended which is worth 3 points per session to a maximum of 34 points. 

## Final Exam
The final prompt is about the final exam scores including the weight for the final exam. 

# Final Grade 
The final grade is calculated as follows;
$' final grade =  Weighted  mid-term1 + Weighted  mid-term2 + Weighted  homework score + Weighted  final exam score '$

For example, a student scored 78 for mid-term 1, 84 for mid-term 2, 95 for the final exam which had a shift of 10 points, and did three homework which he scored 14/15, 17/20, 19/25, and attended 3 sessions. The weight for mid-term 1, mid-term 2, homework, and final exam is 10, 10, 50, and 30 respectively. So the grade can be computed as;


$' Grade = (78 / 100) * 10 + (84 / 100) * 10 + (100 / 100)*30 + (14 + 17 + 19 + (10*3) / 15+20+25+34)*50 '$

$' Grade = 7.8+8.4+30.0+42.6 = 88.8 '$

The following criteria must then be fulfilled to determine the final grade category.
 90% and above ->> A, 89.99%-80% ->> B, 79.99%-70% ->> C, 69.99%-60% ->> D, Under 60% ->> F

 































