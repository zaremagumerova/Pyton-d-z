from address import Address
from mailing import Mailing


from_address=Address(index="475205",city="Уфа",street="Ленина",house="25",apartment="7")
to_address=Address(index="455202",city="Туймазы",street="Мичурина",house="17",apartment="58")


mailing=Mailing(from_address,to_address, track="154",cost="1500")
print(mailing)