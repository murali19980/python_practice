"""
Practice: Properties & Setters
"""
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

if __name__ == "__main__":
    t = Temperature(25)
    print(f"Celsius: {t.celsius}, Fahrenheit: {t.fahrenheit}")
    t.fahrenheit = 98.6
    print(f"Set Fahrenheit 98.6 -> Celsius: {t.celsius}")
