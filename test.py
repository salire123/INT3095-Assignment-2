#---
#test.py
#---

# using pytest to test the game function

import gameplay, city

baseunits = [11000, 10, 10, 10, 10]
c = city.SmallCity("Erith", "smallcity", *baseunits)
c.Earthquake()
c.Earthquake()
c.professional_join()
c.Farmer_join()
c.worker_join()
c.Bussiness_join()

bc=city.BigCity("Furness", "bigcity", *baseunits)
c.Trade_with_other_city(bc)
bc.professional_join
bc.Farmer_join()
bc.worker_join()
bc.Bussiness_join()
bc.Earthquake()

print(c,bc)


