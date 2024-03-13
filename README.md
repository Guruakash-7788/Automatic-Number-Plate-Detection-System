# ANPR and Parking Management System

This repository contains code and resources for an Automatic Number Plate Recognition (ANPR) system and a Parking Management System.

## Team Members
- [Naveen KM](https://github.com/Naveen2701)
- [Gokul S](https://github.com/gokuls007)
- [Guruakash P](https://github.com/guruakash-7788)
- [Merin T](https://github.com/20BTRCL063)

## Project Overview

### ANPR System
The ANPR system allows for the detection and recognition of license plates using computer vision techniques, including the Haar Cascade classifier for plate detection. It includes the following components:

- `number_plate.py`: This file contains the Python script for detecting license plates in real-time using a webcam feed, utilizing the Haar Cascade classifier for plate detection.
- `ocr.py`: This file contains the Python script for optical character recognition (OCR) of the detected license plates.


### Parking Management System
The Parking Management System is a WordPress website developed by Gokul S. It includes functionalities such as:

- Managing vehicles entering and exiting the parking lot.
- Printing receipts for vehicles.
- Tracking vehicle activity within the parking lot.

### Parking Space Monitoring
The Parking Space Monitoring system utilizes computer vision to monitor parking spaces in a parking lot. It includes the following components:

- `main.py`: This file contains the Python script for monitoring parking spaces using computer vision techniques.
- `ParkingSpacePicker.py`: This file contains the Python script for selecting parking spaces and mark it empty or occupied on an image.

## Setup Instructions

### ANPR System
1. Install the required Python libraries: `easyocr`, `opencv-python`, and `mysql-connector-python`.
2. Run `number_plate.py` to detect license plates in real-time.
3. Run `ocr.py` to perform optical character recognition on the detected license plates.

### Parking Management System
1. Deploy the WordPress website contained in the `Parking_Wordpress_Website` folder on a web server.
2. Customize the website according to your requirements.
3. Ensure proper integration with the database for managing vehicle data.

### Parking Space Monitoring
1. Install the required Python libraries: `opencv-python`, `numpy`, and `cvzone`.
2. Run `main.py` to monitor parking spaces using computer vision.
3. Use `ParkingSpacePicker.py` to select parking spaces on an image.

## Requirements
The following libraries are required to run the code in this repository:
- easyocr, opencv-python, mysql-connector-python,numpy, cvzone
use this command to install all required Libraries `pip install -r requirements.txt`
- Ensure you have a MySQL database set up for the ANPR system and update the connection details accordingly in the `number_plate.py` script.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- The ANPR system is inspired by the works of various researchers in the field of computer vision.
- The Parking Management System is based on WordPress, an open-source content management system.
