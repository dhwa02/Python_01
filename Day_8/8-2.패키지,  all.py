import Travel.thailand
import Travel.vietnam
trip_to = Travel.thailand.ThailandPackage()
trip_to.detail()

from Travel.thailand import ThailandPackage 
trip_to = ThailandPackage()
trip_to.detail()

from Travel import vietnam
trip_to = Travel.vietnam.VietnamPackage()
trip_to.detail()

# __all__
from Travel import *
trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
trip_to.detail()
