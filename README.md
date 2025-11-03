# Task 1: Name Matching System

This project finds the most similar names from a dataset using RapidFuzz.

## Setup

pip install -r requirements\_task1.txt

## Run

python task1/name\_matcher.py

2.Create and activate a virtual environment:

python -m venv .venv
.venv\\Scripts\\activate



3.Install dependencies:

pip install -r requirements\_task1.txt



4.Run the name-matcher script:

python name\_matcher.py



5.Interact with the program:

When prompted, type a name and press Enter (e.g., Gita).

To exit, type exit and press Enter.





\#Sample interactive session (**expected output**)


✅ Loaded 36 names from dataset.

Enter a name (or type 'exit' to quit): Gita

🔹 Best Match: Gita (Score: 100.00)

🔸 Top 10 Similar Names:
Gita                       Score: 100.00
Gitanjali                  Score: 90.00
Gitanjli                   Score: 90.00
...



Type exit (or press Ctrl+C) to quit the program.

