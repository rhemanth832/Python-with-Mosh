try:
    age = int(input('Enter your age: '))
    income=20000
    risk = income/age
    print(age)

except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError:
    print('Invalid Value'
          