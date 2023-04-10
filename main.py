#piedra paple y tijeras
import random 

Options = ["Rock","Paper","Scisors"]

def juez(Person,Pc):
    
    if Person == Pc:
        result = "Tie"

    elif (Person == "Paper" and Pc == "Rock"):
        result = "Win"

    elif (Person == "Rock" and Pc == "Scisors"):
        result = "Win"
 
    elif (Person == "Scisors" and Pc == "Paper"):
        result = "Win"
    
    else:
        result = "Lose"

    return result

def save(Person,Pc):
    result = juez(Person,Pc)
    jsonSave = {f"{Person}",
     f"{Pc}",
     f"{result}"}
    return jsonSave

def Game():
    print("""
              Select One thing 
        1) Rock
        
        2) Paper

        3) Scisors  
      
      """)
    Person = input(" ::: ")
    Pc = random.choice(Options)
    juicio = juez(Person,Pc)
    print(f"{juicio}")
    save(Person,Pc)
    pass 



while True:
    print("""  Selecciona """)
    print("""

    1) Iniciar juego
    2) Terminar juego 
    3) Ver historial de jugadas
    
    """)
    init = input(":: ")
    if init == "1":
        Game()

    elif init == "3":
        print("Option no works")

    else:
        print("Incorrect option")

    if init == "2":
        break

