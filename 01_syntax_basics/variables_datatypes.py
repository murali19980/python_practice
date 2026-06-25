"""
Practice: Variables & Data Types
"""
def data_type_demo():
    age = 25                      # int
    pi = 3.14                     # float
    name = "Murali"               # str
    is_active = True              # bool
    result = None                 # NoneType

    print(f"age: {age}, type: {type(age)}")
    print(f"pi: {pi}, type: {type(pi)}")
    print(f"name: {name}, type: {type(name)}")
    print(f"is_active: {is_active}, type: {type(is_active)}")
    print(f"result: {result}, type: {type(result)}")

def type_conversion():
    num_str = "123"
    num_int = int(num_str) * 2
    print(f"'{num_str}' converted to int and doubled: {num_int}")

    int_val = 10
    float_val = float(int_val) / 3
    print(f"{int_val} converted to float and divided by 3: {float_val:.2f}")

    float_val2 = 9.99
    int_val2 = int(float_val2)
    print(f"{float_val2} truncated to int: {int_val2}")

if __name__ == "__main__":
    data_type_demo()
    type_conversion()
