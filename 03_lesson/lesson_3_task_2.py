from smartphone import Smartphone
  
catalog = [
   Smartphone(brand="Samsung",model="А-31",number="+79174586444"),
   Smartphone(brand="Realme",model="R-11",number="+79174444444"),
   Smartphone(brand="Sony",model="S-44",number="+79154586433"),
   Smartphone(brand="Nokia",model="Pro-12",number="+79051745864"),
   Smartphone(brand="Huawei",model="Pro-10",number="+79051732121") 
]  
  
for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")