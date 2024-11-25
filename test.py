import pytest
from city import SmallCity, BigCity

def test_city_metrics():
    baseunits = [11000, 10, 10, 10, 10]
    
    # Initialize cities
    c = SmallCity("Erith", "smallcity", *baseunits)
    bc = BigCity("Furness", "bigcity", *baseunits)

    # Execute operations for SmallCity
    c.Earthquake()
    c.Earthquake()
    c.professional_join()
    c.Farmer_join()
    c.worker_join()
    c.Bussiness_join()
    c.Trade_with_other_city(bc)

    # Execute operations for BigCity
    bc.professional_join()
    bc.Farmer_join()
    bc.worker_join()
    bc.Bussiness_join()
    bc.Earthquake()

    # Test SmallCity metrics
    assert c.population_size == 5036
    assert c.culture == 14
    assert c.food == 2
    assert c.productivity == 9
    assert c.wealth == 3

    # Test BigCity metrics
    assert bc.population_size == 8036
    assert bc.culture == 15
    assert bc.food == 5
    assert bc.productivity == 12
    assert bc.wealth == 7
