from Address import Address
from Mailing import Mailing


to_address = Address("123", "nong", 25, "24", "1"),
from_address = Address("456", "troyan", "bokoka", "47", "2")



Mailing = Mailing(to_address,from_address,1500, "12345")

print(Mailing)
