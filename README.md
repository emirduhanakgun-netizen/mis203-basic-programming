# mis203-basic-programming
* Name: Emir Duhan Akgun
* Student Number: 2404109052
* Department: Management Information System
* Course Name: MIS-203 Basic Programming

---

## Week01 - AI Usage Note
* AI Tool Used: Google Gemini
* Prompt Used: "Write a simple beginner Python code that asks for name, department, age, and career goal using input, and prints them as a student profile."
* What did you change? The AI gave me plain lines of code. I put them inside a main() function to make the code cleaner and organized.

---

## Week 02 - AI Usage Note
* AI Tool Used: Google Gemini
* Prompt Used: "Write a Python program named grade_calculator.py that runs an infinite while True loop. Ask for student name (or q to quit with break) and score. Validate score between 0-100 with continue, assign letter grades (A-F), and calculate average score rounded to 2 decimal places after the loop ends."
* What did you change?: I changed the score input to simple integer and fixed the indentation so the average calculation stays outside the loop.
* What does break do in your program?: In my program, break immediately stops the infinite while True loop when the user enters 'q' for the student name, allowing the program to proceed to the summary and average calculation outside the loop.

---

## Week 03 - AI Usage Note
* AI Tool Used: Google Gemini
* Prompt Used: "Write a Python cinema ticket program with while loop, input validation for age and day, discount rules, and summary statistics."
* What did you change? I used ".lower()" to accept inputs like "WEEKEND" or "Weekday" without errors. I also checked to give the best discount first.
* Tests:
  - Test 1 (Age 0 - Boundary): Name: Umut, Age: 0, Day: weekday, Student: no -> Output: Umut: 0.00 TRY (Free)
  - Test 2 (Age 25 - Boundary): Name: Zeynep, Age: 25, Day: weekend, Student: yes -> Output: Zeynep: 175.00 TRY (Student)
  - Test 3 (Age 12 - Boundary): Name: Beyza, Age: 12, Day: weekday, Student: yes -> Output: Beyza: 120.00 TRY (Child)
* Why does the order of the rules matter? 
- Because Python checks `if/elif` lines from top to bottom and stops at the first true condition. If the student rule was above the child rule, a 10-year-old student would get 30% discount instead of the 40% child discount.

---

## Week 04 - AI Usage Note
* **Program Overview:** This program is a Morse code simulation that feels like a typewriter. It writes dots and dashes step by step on the screen with real beep sounds. I also added morse_shema.txt to explain the program flow.
* AI Tool Used: Google Gemini
* Prompt / Interaction: Brainstorming & Bug Fixing (I didn't ask for the full code directly. Instead, I discussed libraries, asked how to solve specific bugs, and worked on timing issues step by step).
* What did you discuss and fix?:
  - Sound Library & Errors: I asked about Python's built-in sound options and learned how to use `winsound.Beep()`.
  - Turkish Characters: When I entered letters like Ç, Ğ, İ, Ö, Ş, Ü, the program was crashing because they were not in the dictionary. We discussed how to handle this, and I decided to add Turkish characters and punctuation directly into the dictionary.
  - Sound Delay & Hardware Issues: My laptop speakers were cutting off the short dot sounds (beeps). We experimented with the durations, so I increased the dot time to 350 ms and dash time to 850 ms, and added small pauses so the speaker doesn't clip the audio.
  - Double Printing Bug: I noticed the Morse characters were printing twice on the terminal before the sound played. I found and removed the extra print line so the text and sound now play at the exact same time.
* Why do we need different sleep intervals?: Morse code has a rhythm: symbols inside a letter need a very short pause (0.19s), changing to a new letter needs a medium pause (0.21s), and words need a longer pause (0.3s). Without these gaps, all the beeps mix together and it just sounds like non-stop noise. 