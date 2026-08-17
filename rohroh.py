import random


secret = random.randint(1,1000)         

print("Je pense à un nombre entre 1 et 10. À toi de deviner !")
for i in range (1,6):

    proposition = int(input("Ton essai : "))

    if proposition == secret:
        print("🎉 Bravo, tu as trouvé !")
        trouve = True
    elif proposition < secret:
        print("C'est plus grand ⬆️")
    else:
        print("C'est plus petit ⬇️")

print("Fin du jeu. Merci d'avoir joué !")