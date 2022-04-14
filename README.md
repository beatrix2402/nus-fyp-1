# A low-cost device to detect angle closure glaucoma
This repository was created as part of my final year project at the National University of Singapore under the Department of Biomedical Engineering.

In this project, the development of a device using low-cost materials was explored to facilitate the Standard Flashlight Test (SFT), a simple test done that checks for primary angle closure glaucoma (PACG) in patients. This device was created with the intention of independent use by users regardless of technological skills as majority of the target audience are elderly.

A lightweight 3D-printed device was built to solve the problem of infrequent testing for angle closure, which often lead to the unsuspected development of the disease and irreversible blindness. The device runs a Python code on a microprocessor to capture images of a patient’s eye with a camera and a light source. Thereafter, a deep learning algorithm built with PyTorch segments the iris and determines the grading of primary angle closure suspect. The result is displayed to the patient through the device.

## Contents
In this repository, you will find the device code (startup_code_fyp.py) and segmentation code (segmentation_code). Both are written in Python.

The data in the segmentation_code folder is not provided. Please request it if necessary from marisa.lim@u.nus.edu.
