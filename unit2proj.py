# Pippin Dowell, the purpose of this code is to calculate standard deviation
#Sample inputs 5.8, 1.2, 10.4, expected output: 0.44230769230769224

print("Standard deviation calculator \nEnter the values and it will calculate the standard deviation")
x = float(input("Enter observed value: "))
u = float(input("Enter the mean of the sample: "))
z = float(input("Enter the Z-Score of the obsererd value: "))
result = str((x-u)/z)
print("The standard deviation is " + result)