# 🧠 Real Image vs AI Generated Image Detection

This project demonstrates a simple approach to determine whether an image is likely a **real photograph** or a **possibly AI-generated image**.

The program analyzes several image characteristics such as edge density, noise variance, and histogram distribution to estimate the authenticity of the image.

---

## 🛠 Technologies Used

* Python
* OpenCV
* NumPy

---

## 📌 How It Works

The image is analyzed using several computer vision techniques:

* Convert the image to grayscale
* Detect edges in the image
* Estimate noise using Laplacian variance
* Analyze histogram distribution
* Apply a rule-based decision to classify the image

The program will display a result such as:

* Likely Real Image
* Possibly AI Generated Image

---

## 📂 Input Image

* This program checks **one image at a time**.
* The default image name used in the program is **test.jpg**.
* Place the image file in the **same folder as the Python script**.

Example folder structure:

project-folder
detect_image.py
test.jpg

If you want to test another image:

* Replace **test.jpg** with another image
* OR change the image filename inside the code

---

## ▶️ How to Run

* Install Python on your system
* Install the required libraries (OpenCV and NumPy)
* Place the image file in the project folder
* Run the Python script

The program will analyze the image and display the result.

---

## ⚠️ Note

* This is a **basic experimental method** for learning purposes.
* Advanced AI image detection systems usually use **deep learning models and large datasets**.

---

## 👨‍💻 Author

Prabhakaran


---

⭐ If you found this project helpful, consider giving it a star.
