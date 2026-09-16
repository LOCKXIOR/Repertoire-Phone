from random import choice

# Dictionnaire de contacts 
Contacts = {"Lorick": "71688168", "DEF": "57584735"}

# Liste de mots pour accepter
mot_de_confirmation = ["oui","ouais","yes","ok","okay","sansprobleme","sansproblème"]

# Dictionnaire contenant les phrases de sûreté et le mot de passe admin
SER = {
    "sureté": ["êtes vous sûr ? : ", "On continue ? : ", "On y go ? : ", "On y va ?"],
    "Mot_de_pa": ["arepl"]
}

class Phone:
    # le init
    def __init__(self, brand, model, colour, contacts, confam, utilités):
        self.brand = brand
        self.model = model
        self.colour = colour
        self.contacts = contacts
        self.confam = confam
        self.utilités = utilités
    
    # Method to add a number
    def add_nmb(self):
        while True:
            try:
                num = int(input("Entrez votre numéro : "))
                try:
                    # Question de confirmation aléatoire
                    sur_0 = input(choice(self.utilités["sureté"]))
                    if sur_0.lower().strip().replace(" ","") in self.confam:
                        nom = input("Nom : ")
                        sur_1 = input(choice(self.utilités["sureté"]))
                        if sur_1.lower().strip().replace(" ","") in self.confam:                                            
                            # Ajout du contact
                            self.contacts[nom] = str(num)
                            break
                        else:
                            # To leave
                            lve_0 = input("Quitter ? : ")
                            if lve_0.lower().strip().replace(" ","") in self.confam:
                                break
                            else:
                                print("--retour--")                               
                    else:
                        lve_0 = input("Quitter ? : ")
                        if lve_0.lower().strip().replace(" ","") in self.confam:
                            break
                        else:
                            print("--retour--")
                except:
                    print("Erreur inattendu")
                else:
                    print("Numéro ajouté avec succès !")
                    break
            except ValueError:
                print("Erreur : Numéro invalide")
            
    # Simulate a call
    def make_call_nmber(self, number):
        try:
            if number in self.contacts.values():
                print(f"Appelant {number} \n ---Sortant de {self.brand}{self.model}---")
            else:
                print("Erreur : Numéro inexistant")
                ajout = input("Voulez-vous ajouter ce numéro ? : ")
                if ajout.lower().strip().replace(" ","") in self.confam:
                    self.add_nmb()
                else:
                    print("Je suppose qu'une prochaine fois.")                
        except:
            print("Erreur avec les contacts.")
    
    # Just infos
    def infos(self):
        quest = input("Client : ")
        if quest.lower().strip().replace(" ","") == "admin":
            Mdp = input("Mot de passe : ")
            if Mdp in self.utilités["Mot_de_pa"]:
                print(f"Infos for an Admin\n-brand: {self.brand}\n--model: {self.model}\n---colour: {self.colour}\n----contacts: {self.contacts}\n-----confirmations: {self.confam}\n------utilités: {self.utilités}")
            else:
                print(f"Usurpateur...")
                return -1
        else:
            print(f"Infos pour {quest}\n-brand: {self.brand}\n--model: {self.model}\n---colour: {self.colour}")

# Création d'un objet Phone
A = Phone("Samsung ", "Galaxy S25 Ultra ", "Black ", Contacts, mot_de_confirmation, SER)
