class Car:
  def __init__(self, model, year, engine, price):
    self.model = str(model)
    self.year = int(year)
    self.engine = int(engine)
    self.price = float(price)

  def addTiers(self, tierCompany, tierWidth, tierPressure):
    self.tierCompany = str(tierCompany)
    self.tierWidth = (tierWidth)
    self.tierPressure = int(tierPressure)



## Q1
fh_cars_input = open('cars.txt','r')

car_list = []
for line in fh_cars_input.readlines():
  line = line.split('@')
  for i in range(1,3):
    line[i] = int(line[i])
  #line[3] = float(line[3])
  car_list.append(Car(line[0], line[1], line[2], line[3]))


fh_cars_input.close()

print(car_list)

## Q2
# נניח שכל שורה ברשימת הצמיגים תואמת לאותה השורה ברשימת המכוניות
fh_tiers_input = open('tiers.txt','r')
i = 0
for line in fh_tiers_input.readlines():
  line = line.split('@')
  line[1] = line[1].split(' ')
  car_list[i].addTiers(line[0], line[1][0], line[1][1])
  i += 1

## Q3
print('If you want to sort by Model, insert 1.')
print('If you want to sort by price, insert 2.')
sorting_criteria = input("Please insert one option")

if sorting_criteria == '1':
  sorting_criteria = "model"
elif sorting_criteria == '2':
  sorting_criteria = "price"
else:
  print("Unvalid option! Sorting by model name.")
  sorting_criteria = "model"

for i in range(1,len(car_list)):
    idx = i
    while idx >= 0 and car_list[idx].__getattribute__(sorting_criteria) < car_list[idx-1].__getattribute__(sorting_criteria):
      car_list[idx], car_list[idx-1] = car_list[idx-1], car_list[idx]
      idx -= 1


fh_cars_output = open('cars_output.txt','w')

for car in car_list:
  fh_cars_output.write('Model: ' + car.model + '\n')
  fh_cars_output.write('Year: ' + str(car.year) + '\n')
  fh_cars_output.write('Engine: ' + str(car.engine) + '\n')
  fh_cars_output.write('Price: ' + str(car.price) + '\n')
  fh_cars_output.write('Tier company: ' + car.tierCompany + '\n')
  fh_cars_output.write('Tier width: ' + str(car.tierWidth) + '\n')
  fh_cars_output.write('Tier pressure: ' + str(car.tierPressure) + '\n')
  fh_cars_output.write('\n\n\n')


fh_cars_output.close()

##Q4
sum_of_money = float(input("How much money do you have?"))

recommended_car = None
for car in car_list:
  if sum_of_money >= car.price and (recommended_car == None or car.price > recommended_car.price):
    recommended_car = car

print("The recommended car is:",recommended_car.model)
