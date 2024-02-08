# YOLO Train Test Split
This script splits the YOLO format dataset as train, validation and test!

## How to use?
Before running the script you need to edit a few variables.

 1. Point where your YOLO dataset images is by changing  `input_images_folder`  at line 44.
 2. Point where your YOLO dataset labels is by changing  `input_labels_folder`  at line 45.
 3. Edit the  `output_folder`  at line 46 to set the output folder.
 
 Finally run the script. How long it takes to run depends on your dataset and your environment.

    python train_test_split.py
