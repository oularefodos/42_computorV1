# Computor v1

A polynomial equation solver that handles equations up to degree 2.

## Description

This program solves polynomial equations of the form:
```
a * X^0 + b * X^1 + c * X^2 = d * X^0 + e * X^1 + f * X^2
```

It supports:
- Linear equations (degree 1)
- Quadratic equations (degree 2)
- Complex solutions when discriminant is negative
- Special cases (no solution, infinite solutions)

## Requirements

- Python 3.x

## Usage

```bash
python3 computor.py "equation"
```

Or make it executable:
```bash
chmod +x computor.py
./computor.py "equation"
```

## Examples

### Quadratic equation with positive discriminant:
```bash
$ python3 computor.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
Reduced form: 4.0 * X^0 + 4.0 * X^1 - 9.3 * X^2 = 0
Polynomial degree: 2
Discriminant is strictly positive, the two solutions are:
-0.47513146390886934
0.9052389907905898
```

### Linear equation:
```bash
$ python3 computor.py "5 * X^0 + 4 * X^1 = 4 * X^0"
Reduced form: 1.0 * X^0 + 4.0 * X^1 = 0
Polynomial degree: 1
The solution is:
-0.25
```

### Degree > 2:
```bash
$ python3 computor.py "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
Reduced form: 5.0 * X^0 - 6.0 * X^1 + 0.0 * X^2 - 5.6 * X^3 = 0
Polynomial degree: 3
The polynomial degree is strictly greater than 2, I can't solve.
```

### Infinite solutions:
```bash
$ python3 computor.py "6 * X^0 = 6 * X^0"
Reduced form: 0.0 * X^0 = 0
Polynomial degree: 0
Any real number is a solution.
```

### No solution:
```bash
$ python3 computor.py "10 * X^0 = 15 * X^0"
Reduced form: -5.0 * X^0 = 0
Polynomial degree: 0
No solution.
```

### Complex solutions:
```bash
$ python3 computor.py "1 * X^0 + 2 * X^1 + 5 * X^2 = 0"
Reduced form: 1.0 * X^0 + 2.0 * X^1 + 5.0 * X^2 = 0
Polynomial degree: 2
Discriminant is strictly negative, the two complex solutions are:
-1/5 + 2i/5
-1/5 - 2i/5
```

## Implementation Details

### No External Math Libraries
The implementation does not use any built-in mathematical functions except basic arithmetic operations (+, -, *, /). The square root function is implemented using Newton's method.

### Features
- **Parsing**: Extracts coefficients from polynomial expressions
- **Reduction**: Combines like terms and moves all terms to the left side
- **Degree calculation**: Finds the highest power with non-zero coefficient
- **Square root**: Custom implementation using Newton's method
- **Complex numbers**: Handles negative discriminants with complex solutions
- **Fraction display**: Simplifies complex solutions to fraction format when possible

## Project Structure

```
.
├── computor.py       # Main program
├── README.md         # This file
└── en.subject.pdf     # Project subject
```

## Author

Fode Oulare