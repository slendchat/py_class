
yo = int(input("ВОЗРАСТ В ГОДАХ:"))
height = int(input("РОСТ В СМ:"))
sex = input("ПОЛ (М или Ж):")
real_weight = int(input("ВАШ ВЕС В КГ:"))


ideal_weight = 0;

if sex == "М":
  ideal_weight = height-100-((height-150)/4 + yo -20)/4
elif sex == "Ж":
  ideal_weight = height-100-((height-150)/2.5 + yo -20)/6

ideal_weight=round(ideal_weight)
print("Ваш идеальный вес в кг:",ideal_weight)

if real_weight < ideal_weight:
  print("Немножко поднажмите и наберите вес чтобы быть в идеальной форме а именно:",ideal_weight-real_weight,"кг")
  if (yo>=25) and (yo<=60):
    print("Идеальный возраст чтобы начать занятия спортом и набрать килограммы мышц")
else:
  print("Немножко потрудитесь и сбросьте чтобы быть в идеальной форме а именно:", real_weight-ideal_weight,"кг")
  if (yo>=25) and (yo<=60):
    print("Идеальный возраст чтобы начать занятия спортом и сбросить лишний вес")
  elif yo>60:
    print("С возрастом обмен веществ замедляется, и объём пищи необходимо снизить")