def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

if __name__ == "__main__":
    c_temp = 25
    f_temp = celsius_to_fahrenheit(c_temp)
    print(f"{c_temp}C is {f_temp}F")
    
    print(f"{f_temp}F is {fahrenheit_to_celsius(f_temp)}C")
