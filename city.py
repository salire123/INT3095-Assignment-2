#------------------------------------------------------------------------------------------------------------
#--city.py
#------------------------------------------------------------------------------------------------------------
# version 1.0
# author: Simon
# date: 2024-20-11
# description: this is a class for city
# 
#
#------------------------------------------------------------------------------------------------------------
#--city class
#------------------------------------------------------------------------------------------------------------
class City:
    """
    A class to represent a city.
    Attributes:
        name (str): The name of the city.
        CityType (str): The type of the city. Can be either 'bigcity' or 'smallcity'.
        population_size (int): The size of the city's population.
        culture (int): The culture of the city.
        food (int): The food of the city.
        productivity (int): The productivity of the city.
        wealth (int): The wealth of the city.
        TradeState (bool): The state of the city's trade.
    """
    
    def __init__(self, name, CityType, population_size, culture, food, productivity, wealth):
        if CityType not in ["bigcity", "smallcity"]:
            raise ValueError("CityType must be either 'bigcity' or 'smallcity'")
        self.population_size = int(population_size)
        self.culture = int(culture)
        self.food = int(food)
        self.productivity = int(productivity)
        self.wealth = int(wealth)
        self.name = str(name)
        self.TradeState = False
        self.CityType = CityType

    def __str__(self):
        return (
            "----------------------------------------\n"
            f"{self.name} population have: {self.population_size}\n"
            f"culture: {self.culture}\n"
            f"food: {self.food}\n"
            f"productivity: {self.productivity}\n"
            f"wealth: {self.wealth}\n"
            f"TradeState: {self.TradeState}\n"
            f"CityType: {self.CityType}\n"
            "----------------------------------------"
        )

    def add_remove_population(self, population_change):
        self.population_size = max(self.population_size + population_change, 0)
        return self.population_size
    
    def add_remove_culture(self, culture_change):
        self.culture = max(self.culture + culture_change, 0)
        return self.culture
    
    def add_remove_food(self, food_change):
        self.food = max(self.food + food_change, 0)
        return self.food
    
    def add_remove_productivity(self, productivity_change):
        self.productivity = max(self.productivity + productivity_change, 0)
        return self.productivity
    
    def add_remove_wealth(self, wealth_change):
        self.wealth = max(self.wealth + wealth_change, 0)
        return self.wealth

#------------------------------------------------------------
#city -> smallcity class---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
class SmallCity(City):
    """
    A class representing a small city, inheriting from the City class.
    Attributes:
    -----------
    name : str
        The name of the city.
    CityType : str
        The type of the city.
    population_size : int
        The population size of the city.
    culture : int
        The culture level of the city.
    food : int
        The food resources of the city.
    productivity : int
        The productivity level of the city.
    wealth : int
        The wealth level of the city.
    Methods:
    --------
    professional_join():
        Handles the event of professionals joining the city.
    Farmer_join():
        Handles the event of farmers joining the city.
    worker_join():
        Handles the event of workers joining the city.
    Bussiness_join():
        Handles the event of business people joining the city.
    Earthquake():
        Handles the event of an earthquake affecting the city.
    Trade_port_open():
        Opens the trade port of the city.
    Trade_port_close():
        Closes the trade port of the city.
    Trade_with_other_city(trade_city):
        Handles the event of trading with another city.
    """
    def __init__(self, name, CityType, population_size, culture, food, productivity, wealth):
        super().__init__(name, CityType, population_size, culture, food, productivity, wealth)

    # join event
    def professional_join(self):
        self.add_remove_population(     1009    )
        self.add_remove_culture(        1       )
        self.add_remove_food(           -1      )
        self.add_remove_productivity(   -1      )
        self.add_remove_wealth(         0       )

    def Farmer_join(self):
        self.add_remove_population(     1009    )
        self.add_remove_culture(        0       )
        self.add_remove_food(           1       )
        self.add_remove_productivity(   1       )
        self.add_remove_wealth(         0       )

    def worker_join(self):
        self.add_remove_population(     2009    )
        self.add_remove_culture(        0       )
        self.add_remove_food(           -2      )
        self.add_remove_productivity(   1       )
        self.add_remove_wealth(         -1      )

    def Bussiness_join(self):
        self.add_remove_population(     1009    )
        self.add_remove_culture(        0       )
        self.add_remove_food(           -2      )
        self.add_remove_productivity(   1       )
        self.add_remove_wealth(         1       )

    # earthquake event
    def Earthquake(self):
        self.add_remove_population(     -8000    )
        self.add_remove_culture(        -1      )
        self.add_remove_food(           -3      )
        self.add_remove_productivity(   -3      )
        self.add_remove_wealth(         -5      )


    # trade event
    def Trade_port_open(self):
        self.TradeState = True

    def Trade_port_close(self):
        self.TradeState = False

    def Trade_with_other_city(self, trade_city):
            self.add_remove_population(     0       )
            self.add_remove_culture(        5       )
            self.add_remove_food(           2       )
            self.add_remove_productivity(   3       )
            self.add_remove_wealth(         2       )
            trade_city.add_remove_population(     0       )
            trade_city.add_remove_culture(        5       )
            trade_city.add_remove_food(           2       )
            trade_city.add_remove_productivity(   3       )
            trade_city.add_remove_wealth(         2       )
            
#---------------------------------------------------------------------------------------------------------------------
#city -> smallcity class -> bigcity class---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
class BigCity(SmallCity):
    """
    A class representing a big city, inheriting from SmallCity.
    Attributes:
        name (str): The name of the city.
        CityType (str): The type of the city.
        population_size (int): The population size of the city.
        culture (int): The culture level of the city.
        food (int): The food resources of the city.
        productivity (int): The productivity level of the city.
        wealth (int): The wealth level of the city.
    Methods:
        __init__(name, CityType, population_size, culture, food, productivity, wealth):
            Initializes a BigCity object with the given attributes.
        Acttack(acttack_city):
            Simulates an attack event on another city, modifying the population, culture, food, productivity, and wealth of both cities.
    """
    def __init__(self, name, CityType, population_size, culture, food, productivity, wealth):
        super().__init__(name, CityType, population_size, culture, food, productivity, wealth)

    # Attack event
    def Attack(self, acttack_city):
        self.add_remove_population(     -100   )
        self.add_remove_culture(        0      )
        self.add_remove_food(           +5      )
        self.add_remove_productivity(   +3      )
        self.add_remove_wealth(         +5      )
        acttack_city.add_remove_population(     -500       )
        acttack_city.add_remove_culture(        -2       )
        acttack_city.add_remove_food(           -5       )
        acttack_city.add_remove_productivity(   -3       )
        acttack_city.add_remove_wealth(         -4       )



#------------------------------------------------------------
#test code
##---------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    baseunits = [11000, 10, 10, 10, 10]
    city_names = ["Hong Kong", "London", "New York", "Tokyo", "Paris", "Sydney", "Beijing", "Dubai", "Singapore", "Toronto"]
    running_city = []

    for name in city_names:
        city_manager = SmallCity(name, "smallcity", *baseunits)
        running_city.append(city_manager)
        print("---")
        print(city_manager)
        print("---")

    running_city[0].add_remove_population(-100000)
    
    print(running_city[0])

    running_city[0].professional_join()

    print(running_city[0])

    running_city[0].Earthquake()
    running_city[0].Earthquake()
    running_city[0].Earthquake()
    running_city[0].Earthquake()


    print(running_city[0])

    #test trade
