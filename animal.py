class Animal():
    patas = 4
    tem_rabo = False
    pelo = True
    especie = ""
    sexo = 'Macho'

class Cachorro(Animal):
    tem_rabo = True
    especie = 'Canis lupus familiares'
    raca = 'Golden-Retriver'
    nome = 'Éros'
    porte = 'Grande'

    def latir():
        return 'AUAUAUAUAUAUAUAUAUAUAUAU'
    
    def comer():
        return 'NhameiNhamei'

    def dormir():
        return 'ZZZZZZZ'

print(Cachorro.comer())
print(Cachorro.dormir())
print(Cachorro.latir())
print(Cachorro.especie)
print(Cachorro.nome)
print(Cachorro.patas)
print(Cachorro.pelo)
print(Cachorro.porte)
print(Cachorro.raca)
print(Cachorro.sexo)
