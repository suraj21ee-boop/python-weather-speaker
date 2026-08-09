import requests
import pyttsx3
engine = pyttsx3.init()
print("            IMPORTANT  !!!      \n               please switched on your internet connection ....")
def speak(text):
    print(text)  
    engine.say(text)
    engine.runAndWait()
n = input("Do you really want to know about weather?...\nSay yes or no: ").lower().strip()

while True:
    if n == "yes":
        city_name = input("\nEnter the name of the city or state: ").strip()
        url_link = f'https://api.weatherapi.com/v1/current.json?key=7a810a61ae374244b69124635260408&q={city_name}'
        
        try:
            response = requests.get(url_link)
            data = response.json()
            
            if "error" in data:
                speak(f"Location not found: {data['error']['message']}. Please check your spelling!")
                continue  
                
            name = data["location"]["name"]
            region = data["location"]["region"]
            temp = data["current"]["temp"]
            condition = data["current"]["condition"]["text"]
            weather_report = f"The current temperature in {name}, {region} is {temp} degrees Celsius with {condition}."
            speak(weather_report)
            
        except Exception as e:
            speak("Network error. Could not connect to the weather service.")
            continue
        j = input("\nDo you want more cities? (yes/no): ").lower().strip()
        if j == "no":
            break
            
    elif n == "no":
        speak("Thank you for your time!")
        break
    else:
        n = input("Invalid input!\n Enter either yes or no: ").lower().strip()

print("\nThis is the end of the dicussion.")
