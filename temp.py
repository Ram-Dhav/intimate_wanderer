name = input("Hello! What is your name? ")
temp = float(input(f"Hello {name}, enter temperature in Celsius: "))
if temp < 0:
 print("Freezing weather")
elif temp < 10:
 print("Very Cold weather")
elif temp < 20:
 print("Cold weather")
elif temp < 30:
 print("Normal weather")
elif temp < 40:
 print("Hot weather")
else:
 print("Very Hot weather")

ask = input("Which type of weather do you want to know? (Freezing, Very Cold, Cold, Normal, Hot, Very Hot): ")
if ask.lower() == "freezing":
    print("Freezing weather is when the temperature is below 0°C.")
elif ask.lower() == "very cold":
    print("Very Cold weather is when the temperature is between 0°C and 10°C.")
elif ask.lower() == "cold":
    print("Cold weather is when the temperature is between 10°C and 20°C.")
elif ask.lower() == "normal":
    print("Normal weather is when the temperature is between 20°C and 30°C.")
elif ask.lower() == "hot":  
    print("Hot weather is when the temperature is between 30°C and 40°C.")
elif ask.lower() == "very hot":
    print("Very Hot weather is when the temperature is above 40°C.")

