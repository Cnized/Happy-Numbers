
# ✅ Happy Number Checker

A simple Python program to check whether a number is a **Happy Number** or not.

---

## 📖 What is a Happy Number?

A **Happy Number** is defined as follows:

1. Start with any positive integer.
2. Replace the number with the sum of the squares of its digits.
3. Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle that does not include 1.
4. Numbers that end in 1 are **Happy Numbers**, while numbers that fall into a repeating cycle that does not include 1 are **Sad Numbers**.

**Example:**

- 19 is a happy number:
  - 1² + 9² = 82  
  - 8² + 2² = 68  
  - 6² + 8² = 100  
  - 1² + 0² + 0² = 1 ✅

---

## ✨ Features

- Checks if a number is **Happy** or **Sad**
- Uses a `set` to track previously seen numbers to detect cycles
- Friendly messages for output
- Lightweight and easy to use

---
## 📂 Project Structure
```bash
Happy-Number/
│
├── README.md              
│
└── src/
    └── main.py            
```
## ⚙️ Requirements

- Python 3.x

No external libraries required.

---

## 🚀 How to Use

1. Clone or download this repository.
2. Open your terminal or command prompt.
3. Navigate to the folder containing the script.
4. Run the script using Python:

```bash
python happy_number.py
```

5. Enter any positive integer when prompted:

```
Enter a number to see if it's Happy or sad: 19
```

6. The script will print:

```
Your number is 'Happy', yay!
```

or

```
Your number is sad :(
```

---

## 💻 Code Overview

```python
def happy_number(number):
    ''' Check if a number is a happy number or not.

    :param number: The number to check.
    :type number: int
    '''
    seen = set()
    while number not in seen:
        seen.add(number) 
        digits = [int(x) for x in str(number)]
        number = sum([x**2 for x in digits])
        if number == 1:
            print("Your number is 'Happy', yay!")
            return
        elif number == 4:
            print("Your number is sad :(")


if __name__ == "__main__":
    number = int(input("Enter a number to see if it's Happy or sad: "))
    happy_number(number)
```

---

## 📜 License

This project is licensed under the **MIT License**.

---
## 👨‍💻Author 
💻 Built with ❤️ by Kian Kheiri N. ([@Cnized](https://github.com/Cnized))