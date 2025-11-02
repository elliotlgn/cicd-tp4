"""Calculatrice simple avec fonctionnalités avancées"""

class Calculator:
    def add(self, a: float, b: float) -> float:
        """Addition de deux nombres"""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Soustraction de deux nombres"""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiplication de deux nombres"""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Division de deux nombres"""
        if b == 0:
            raise ValueError("Division par zéro")
        return a / b

    def power(self, base: float, exponent: float) -> float:
        """Calcul de la puissance"""
        return base ** exponent

    def sqrt(self, value: float) -> float:
        """Racine carrée"""
        if value < 0:
            raise ValueError("Impossible de calculer la racine carrée d'un nombre négatif")
        return value ** 0.5

    def factorial(self, n: int) -> int:
        """Factorielle d'un nombre"""
        if n < 0:
            raise ValueError("La factorielle d'un nombre négatif n'existe pas")
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result