
#---
# gameplay.py
#---

import random , os
from city import City, SmallCity, BigCity

#---
# gameplay class
#---
class Gameplay:
    def __init__(self):
        self.cities = []
        self.current_city = None 
        self.round = 0

#---
# Start game
#---
    def start_game(self):
        self.clear_screen()
        print("Welcome to the game!")
        # check user input

        small_city_list = []
        big_city_list = []

        while not small_city_list:
            small_city_list = input("Enter the names of the Small cities (comma separated): ").split(",")
            small_city_list = [city.strip() for city in small_city_list if city.strip()]
            if not small_city_list:
                self.clear_screen()
                print("Please enter at least one small city.")

        while not big_city_list:
            big_city_list = input("Enter the names of the Big cities (comma separated): ").split(",")
            big_city_list = [city.strip() for city in big_city_list if city.strip()]
            if not big_city_list:
                self.clear_screen()
                print("Please enter at least one big city.")
            

    

        baseunits = [11000, 10, 10, 10, 10] # Adjusted to match expected arguments
        
        for small_city in small_city_list:
            city_manager = SmallCity(small_city, "smallcity", *baseunits)
            self.cities.append(city_manager)
        for big_city in big_city_list:
            city_manager = BigCity(big_city, "bigcity", *baseunits)
            self.cities.append(city_manager)
            

        self.run_game()

#---
# End game
#---
    def end_game(self):
        print("Thank you for playing!")
        exit()

#---
# Run the game
#---
    def run_game(self):
        events = [
            ("Earthquake", 14.2857142857),
            ("professional_join", 14.2857142857),
            ("Farmer_join", 14.2857142857),
            ("worker_join", 14.2857142857),
            ("Bussiness_join", 14.2857142857),
            ("Trade_port_open", 14.2857142857),
            ("Attack", 14.2857142857),
        ]
        loop = True

        while loop == True:
            self.round += 1
            self.clear_screen()
            print(f"Round {self.round}")
            input("plase press any key to continue")


            # Random event
            self.event(events)

            
            askshowlist = input("did you want to show list? (y/n)")
            if askshowlist == "y":

                for city in self.cities:
                    print(city)
            else:
                pass



            # Check if the game is over
            askendgame = input("did you want to end game? (y/n)")
            if askendgame == "y":
                loop = False
            else:
                pass

        self.end_game()
#---
# Event
#---                
    def event(self, events):
        temp_cities = self.cities.copy()
        temp_cities = self.pair_trade_city(temp_cities)

        for city in temp_cities:
            random_event = random.randint(1, 100)
            cumulative_probability = 0
            
            for event, probability in events:
                cumulative_probability += probability
                
                if random_event <= cumulative_probability:
                    # Handle Attack event separately since it needs a parameter
                    if event == "Attack":
                        if city.CityType == "smallcity":
                            print(f"skip the event {event} in {city.name} because it is small city")
                            break
                        elif city.CityType == "bigcity":
                            if temp_cities:
                                attack_city = random.choice(temp_cities)
                                if attack_city != city:  # Prevent self-attack
                                    print(f"{city.name} Attacked {attack_city.name}!")
                                    city.Attack(attack_city)
                            break
                    else:
                        # Handle other events normally
                        print(f"{event} event triggered in {city.name}!")
                        event_method = getattr(city, event, None)
                        if callable(event_method):
                            event_method()
                        else:
                            print(f"No method found for {event} in {city.name}.")
                    break




#---
# Trade with other city
#---
    def pair_trade_city(self, cities):
        Trade_city = []
        for city in cities:
            if city.TradeState == True:
                Trade_city.append(city)
        while len(Trade_city) > 1:
            # random city
            city_1 = random.choice(Trade_city)
            Trade_city.remove(city_1)
            city_2 = random.choice(Trade_city)
            Trade_city.remove(city_2)
            city_1.Trade_with_other_city(city_2)
            print(f"{city_1.name} trade with {city_2.name}")

            city_1.Trade_port_close()
            city_2.Trade_port_close()
            #remove city from Temp_cities to avoid double trade
            cities.remove(city_1)
            cities.remove(city_2)

        return cities
    

#---
# Clear the console screen
#---
    @staticmethod
    def clear_screen():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')