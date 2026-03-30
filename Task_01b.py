# Task 01b - Classify Temperature
# Write a function called classify_temperature(temp)
# that returns:
# "Cold" if temp < 15
# "Mild" if temp is 15 to 24
# "Hot" if temp >= 25
#
# Example:
# classify_temperature(12) -> "Cold"

def classify_temperature(temp):
    # Write your code here
    if temp < 15:
        classify = 'Cold'
    elif temp >= 15 and temp < 25:
        classify = 'Mild'
    elif temp >= 25:
        classify = 'Hot'
    else:
        pass
    return classify


def main():
    temp = int(input("Enter temperature: "))
    print(classify_temperature(temp))


if __name__ == "__main__":
    main()
