import requests

city = input("Enter the city name(Fairfield): ")
country = input("Enter the country name(United States of America): ")

class LocationInfoApi:
    def __init__(self):
        self.url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities/Q754635"

        self.headers = {
            "X-RapidAPI-Key": "56b9e031e8mshc830e4c0ac0ae47p1620ccjsn91bb4249600e",
            "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
        }

        self.response = requests.get(self.url, headers=self.headers)

    def getCityInfo(self):

        try:
            data = self.response.json()

            if data.get("data"):
                return data["data"]
            else:
                return None

        except requests.RequestException as e:
            print("Error fetching city data", e)
            return None

    def getPopulation(self):
        city_info = self.getCityInfo()
        if city_info:
            return city_info.get("population", "Population data not available")
        else:
            return "City not found"

    def getCoordinates(self):
        city_info = self.getCityInfo()
        if city_info:
            return (
                city_info.get("latitude", "Latitude data not available"),
                city_info.get("longitude", "Longitude data not available")
            )
        else:
            return "City not found", "City not found"

    def getElevation(self):
        city_info = self.getCityInfo()
        if city_info:
            return city_info.get("elevationMeters", "Elevation data not available")
        else:
            return "City not found"

    def getTimezone(self):
        city_info = self.getCityInfo()
        if city_info:
            return city_info.get("timezone", "Timezone data not available")
        else:
            return "City not found"


class LocationDetails:
    def __init__(self):
        self.is_running = True
        self.geodb_api = LocationInfoApi()

    def userInterface(self):
        print("====================================")
        print("Location Details Program")
        print("Options:")
        print("Enter 1 For Population")
        print("Enter 2 For Longitude Coordinates")
        print("Enter 3 For Latitude Coordinates")
        print("Enter 4 For Elevation")
        print("Enter 5 For Timezone")
        print("Enter 9 To Exit")
        print("====================================")

    def run(self):
        print("Welcome to the Location Details Program")
        print("This program provides information about Fairfield.")

        while self.is_running:
            self.userInterface()
            user_input = input("Enter your choice: ")

            if user_input == "1":
                population = self.geodb_api.getPopulation()
                print("Population: ", population)

            elif user_input == "2":
                latitude, longitude = self.geodb_api.getCoordinates()
                print("Longitude: ", longitude, "Latitude: ", latitude)

            elif user_input == "3":
                latitude, _ = self.geodb_api.getCoordinates()
                print("Latitude ", latitude)

            elif user_input == "4":
                elevation = self.geodb_api.getElevation()
                print("Elevation(Meters) ", elevation)

            elif user_input == "5":
                timezone = self.geodb_api.getTimezone()
                print("Timezone: ", timezone)

            elif user_input == "9":
                print("Exiting Location Details Program.")
                self.is_running = False

            else:
                print("Invalid choice. Please enter a valid option.")


api_key = "Gq42uNUzWZuGdsxfQcYCg1PqGsO9CcVYeZojGt3w"
location_details_app = LocationDetails()
location_details_app.run()