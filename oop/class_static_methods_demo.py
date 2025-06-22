# class_static_methods_demo.py

class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Performs addition without using class or instance attributes."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Performs multiplication and prints a class-level attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
