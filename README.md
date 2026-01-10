**Snake, Gun, Water – Game** 

**Overview**
This is a simple command-line game written in Python where the user plays Snake, Gun, Water against the computer.
The computer randomly selects a choice, and the result is decided using conditional logic.

This game is similar to Rock,Paper,Scissors but with
1. Snake - 1
2. water - -1
3. Gun - 0

**Game Rules**

Snake drinks water - Snake wins
Gun kills snake - Gun wins
Water damages gun - Water wins
Same choices -  Draw

**How Program Works**

The computer randomly 1- snake, 0- Gun, -1- water, the user have to choose as string. A dictionary converts the user input into numeric values and another dictionary is used to convert numbers back into readable choices for display.
The program compares the computer’s choice and the user’s choice using if-elif-else conditions.
The result is printed as: You Win, You Lose, It's a Draw.
And also if anything wrong in if-else ladder its prints "something went wrong "

**How To Run the programe**

Make sure python is installed in your pc and run the programe, choose your choice. User input must be exactly snake or water or gun then computer randomly selects.












