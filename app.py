import requests

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.weatherapi.com/v1/current.json"
        self.favorite_cities = set()

    def get_weather(self, city):
        params = {"key": self.api_key, "q": city}
        response = requests.get(self.base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Error: Unable to get weather data for {city}")
            return None

    def add_favorite(self, city):
        self.favorite_cities.add(city)
        print(f"{city} added to favorites.")

    def remove_favorite(self, city):
        if city in self.favorite_cities:
            self.favorite_cities.remove(city)
            print(f"{city} removed from favorites.")
        else:
            print(f"{city} is not in your favorites.")

    def list_favorites(self):
        print("Favorite Cities:")
        for city in self.favorite_cities:
            print(f"- {city}")

def main():
    api_key = " d7af969a9b064f72bce195030240701"  # Replace with your actual API key
    weather_app = WeatherApp(api_key)

    while True:
        print("\nOptions:")
        print("1. Check Weather by City")
        print("2. Add Favorite City")
        print("3. Remove Favorite City")
        print("4. List Favorite Cities")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            city = input("Enter city name: ")
            weather_data = weather_app.get_weather(city)
            if weather_data:
                print(f"Weather in {city}:\n{weather_data['current']}")
        elif choice == "2":
            city = input("Enter city name to add to favorites: ")
            weather_app.add_favorite(city)
        elif choice == "3":
            city = input("Enter city name to remove from favorites: ")
            weather_app.remove_favorite(city)
        elif choice == "4":
            weather_app.list_favorites()
        elif choice == "5":
            print("Exiting Weather App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
