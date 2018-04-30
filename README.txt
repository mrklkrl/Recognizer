FACIAL RECOGNITION README 5/3/2017
author: Michael Cole

the project consists of three modules:

1)datasetCreator.py
2)trainer.py
3)recognizer.py

to use these programs, you must have python 2.7 and the latest version of openCV as well as PIL installed.

the dataSet directory currently includes a set of sample images used in making the project. If you wish to create your own data, you must first empty this directory.

STEP 1: CREATE THE DATASET:

in idle, run datasetCreator.py. You will be prompted for a user ID. for each unique user, enter a unique integer for the ID.

after the user ID is entered, press return. the program will open the computer's default webcam and take 301 photos of the detected face. The face being photographed will be framed with a blue rectangle. remain as still as possible during this process. the more users, the better. The more times you run this program per user, the better.

STEP 2: TRAIN THE FACE RECOGNIZER

run trainer.py . If you are on an apple computer, you must open the dataSet directory in vim and delete the first and last entries as they are junk data used by OS X that will interfere with the program. When the program is complete, exit.

STEP 3: CHANGE THE DEFAULT NAMES ASSOCIATED WITH ID

names associated with IDs are hardcoded. open recognizer.py and find the IF block where if ID = 1 and change MIKE to the name you want to use for user 1, etc.

STEP 4: RUN THE PROGRAM

run recognizer.py . Your face should be framed and your name written in the blue square! 