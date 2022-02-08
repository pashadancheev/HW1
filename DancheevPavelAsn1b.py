# Pavel Dancheev Assignment 1B) Investments: Return and Risk - problem 6

# part a)

start = int(input("Enter start value:"))
high = int(input("Enter high value:"))
low  = int(input("Enter low value:"))


expected_end_value = (high + low)/2
expected_return = ((expected_end_value - start)/start)*100
risk = (high - low)/2
print("Expected end value =", expected_end_value)
print("Expected return value = ",expected_return)
print("Risk = ",risk)

# part b)

#Cash fund: 
#Expected end value = 1005
#Expected return value = 0.5
#Risk = 5.0

#Bond fund:
#Expected end value = 1010
#Expected return value = 1.0
#Risk = 40.0

#Stock fund:
#Expected end value = 1025
#Expected return value = 2.5
#Risk = 75.0


