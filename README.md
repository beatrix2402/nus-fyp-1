# A low-cost device to detect angle closure glaucoma
This repository was created as part of my final year project at the National University of Singapore under the Department of Biomedical Engineering.

In this project, the development of a device using low-cost materials was explored to facilitate the [Standard Flashlight Test (SFT)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5130941/), a simple test done that checks for primary angle closure glaucoma (PACG) in patients. This device was created with the intention of independent use by users regardless of technological skills as majority of the target audience are elderly.

A lightweight 3D-printed device (`CAD_files`) was built to solve the problem of infrequent testing for angle closure, which often lead to the unsuspected development of the disease and irreversible blindness. The device runs a Python code on a Raspberry Pi Zero (`startup_code_fyp.py`) to capture images of a patient’s eye with a camera and a light source. Thereafter, a deep learning algorithm built with PyTorch (`segmentation_code.ipynb`) segments the iris and determines the grading of primary angle closure suspect. The result is displayed to the patient through the device.

## About the Repository
In this repository, you will find the device code (`startup_code_fyp.py`), segmentation code (`segmentation_code`) and the CAD files used to print the device (`CAD_files`). Both are written in Python.

**The data for the segmentation code is not provided.** Please request it if necessary from marisa.lim@u.nus.edu.

## Segmentation Code
In the `segmentation_code` folder, you will find the models and Python notebook used. The `.html` and `.pdf` versions of the Python notebook are also included.

The necessary outputs are kept within for a better understanding of the notebook.

## Start-up Code
This Python code is run on a Raspberry Pi Zero in the device to automate the Standard Flashlight Test. The Raspberry Pi GPIO library was used.

## CAD Files
There are three components to the 3D-printed device: box top, box bottom, and LED holder. These are found in the `CAD_files` folder, which contains both the `.stl` and original SolidWorks files. An assembly file is also included within to visualise the three components together, with an additional eye cup to simulate the silicon eye cup that is attached later on.
