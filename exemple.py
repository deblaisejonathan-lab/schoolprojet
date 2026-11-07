inscription = input()
print("bonjour votre Nom!:")
for Inscription in inscription:
    with open('nom.txt', 'w \n') as file_etu:
        print(file_etu.write(inscription))
        file_etu.close()

