#!/usr/bin/env python3
import sys
import re


class PolynomialSolver:
    def __init__(self, equation_str):
        self.equation_str = equation_str
        self.coefficients = {}
        
    def parse_equation(self):
        """Parse the polynomial equation and extract coefficients"""
        if '=' not in self.equation_str:
            raise ValueError("Invalid equation format: missing '='")
        
        left_side, right_side = self.equation_str.split('=')
        
        left_coeffs = self._parse_side(left_side)
        right_coeffs = self._parse_side(right_side)
        
        all_powers = set(left_coeffs.keys()) | set(right_coeffs.keys())
        
        for power in all_powers:
            left_val = left_coeffs.get(power, 0)
            right_val = right_coeffs.get(power, 0)
            self.coefficients[power] = left_val - right_val
        
    def _parse_side(self, side_str):
        """Parse one side of the equation and return coefficients dict"""
        coeffs = {}
        
        pattern = r'([+-]?\s*\d+\.?\d*)\s*\*\s*X\s*\^\s*(\d+)'
        
        matches = re.findall(pattern, side_str)

        
        for coeff_str, power_str in matches:
            coeff_str = coeff_str.replace(' ', '')
            coeff = float(coeff_str)
            power = int(power_str)
            
            if power in coeffs:
                coeffs[power] += coeff
            else:
                coeffs[power] = coeff
        
        return coeffs
    
    def get_reduced_form(self):
        """Return the reduced form string"""
        if not self.coefficients:
            return "0 * X^0 = 0"
        
        sorted_powers = sorted(self.coefficients.keys())
        
        terms = []
        for power in sorted_powers:
            coeff = self.coefficients[power]
            
            if len(terms) == 0:
                terms.append(f"{coeff} * X^{power}")
            else:
                if coeff >= 0:
                    terms.append(f"+ {coeff} * X^{power}")
                else:
                    terms.append(f"- {abs(coeff)} * X^{power}")
        
        return " ".join(terms) + " = 0"
    
    def get_degree(self):
        """Return the polynomial degree"""
        if not self.coefficients:
            return 0
        
        max_power = 0
        for power, coeff in self.coefficients.items():
            if coeff != 0:
                max_power = max(max_power, power)
        
        return max_power
    
    def solve(self):
        """Solve the polynomial equation"""
        degree = self.get_degree()
        
        print(f"Reduced form: {self.get_reduced_form()}")
        print(f"Polynomial degree: {degree}")
        
        if degree > 2:
            print("The polynomial degree is strictly greater than 2, I can't solve.")
            return
        
        a = self.coefficients.get(2, 0)
        b = self.coefficients.get(1, 0)
        c = self.coefficients.get(0, 0)
        
        if degree == 0:
            if c == 0:
                print("Any real number is a solution.")
            else:
                print("No solution.")
        
        elif degree == 1:
            if b == 0:
                if c == 0:
                    print("Any real number is a solution.")
                else:
                    print("No solution.")
            else:
                solution = -c / b
                print("The solution is:")
                print(solution)
        
        elif degree == 2:
            discriminant = b * b - 4 * a * c
            
            if discriminant > 0:
                print("Discriminant is strictly positive, the two solutions are:")
                sqrt_discriminant = self._sqrt(discriminant)
                x1 = (-b + sqrt_discriminant) / (2 * a)
                x2 = (-b - sqrt_discriminant) / (2 * a)
                print(x1)
                print(x2)
            
            elif discriminant == 0:
                print("Discriminant is zero, the solution is:")
                x = -b / (2 * a)
                print(x)
            
            else:  # discriminant < 0
                print("Discriminant is strictly negative, the two complex solutions are:")
                real_part = -b / (2 * a)
                img_part = self._sqrt(abs(discriminant)) / (2 * a)
                
                if real_part == 0:
                    print(f"{img_part}i")
                    print(f"-{img_part}i")
                else:
                    # Try to express as fractions
                    if self._is_simple_fraction(real_part) and self._is_simple_fraction(img_part):
                        real_num, real_den = self._to_fraction(real_part)
                        img_num, img_den = self._to_fraction(img_part)
                        
                        if real_den == img_den:
                            print(f"{real_num}/{real_den} + {img_num}i/{img_den}")
                            print(f"{real_num}/{real_den} - {img_num}i/{img_den}")
                        else:
                            print(f"{real_part} + {img_part}i")
                            print(f"{real_part} - {img_part}i")
                    else:
                        print(f"{real_part} + {img_part}i")
                        print(f"{real_part} - {img_part}i")
    
    def _sqrt(self, x):
        """Calculate square root using Newton's method"""
        if x == 0:
            return 0
        
        guess = x / 2.0
        epsilon = 1e-10
        
        while True:
            next_guess = (guess + x / guess) / 2.0
            if abs(next_guess - guess) < epsilon:
                return next_guess
            guess = next_guess
    
    def _is_simple_fraction(self, value):
        """Check if value can be expressed as a simple fraction"""
        for denom in range(1, 20):
            numerator = value * denom
            if abs(numerator - round(numerator)) < 1e-9:
                return True
        return False
    
    def _to_fraction(self, value):
        """Convert decimal to simple fraction (numerator, denominator)"""
        for denom in range(1, 20):
            numerator = value * denom
            if abs(numerator - round(numerator)) < 1e-9:
                return int(round(numerator)), denom
        return value, 1


def main():
    if len(sys.argv) != 2:
        print("Usage: ./computor.py \"equation\"")
        sys.exit(1)
    
    equation = sys.argv[1]
    
    try:
        solver = PolynomialSolver(equation)
        solver.parse_equation()
        solver.solve()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()