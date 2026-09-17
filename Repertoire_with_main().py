from random import choice


Contacts={"Lorick": "71688168", "DEF": "57584735"}

class Phone:
    
    global Contacts
    
    def __init__(self, brand, model, colour, contacts, confam, utilités):
        self.brand=brand
        self.model=model
        self.colour=colour
        self.contacts=contacts
        self.confam=confam
        self.utilités=utilités
    
    def add_nmb(self):
        while True:
            try:
                num=int(input(f"\nEntrez votre numéro : "))
                try:
                    sur_0=input(choice(self.utilités["sureté"]))
                    if sur_0.lower().strip().replace(" ","") in self.confam:
                        nom=input("Nom : ")
                        sur_1=input(choice(self.utilités["sureté"]))
                        if sur_1.lower().strip().replace(" ","") in self.confam:                                            
                            self.contacts[nom] = str(num)
                            break
                        else:
                            lve_0=input(f"\nQuitter ? : ")
                            if lve_0.lower().strip().replace(" ","") in self.confam:
                                break
                            else:
                                print("--retour--")                               
                    else:
                        lve_0=input(f"\nQuitter ? : ")
                        if lve_0.lower().strip().replace(" ","") in self.confam:
                            break
                        else:
                            print("---retour en arrière en exécution---")
                except:
                    print("Erreur inattendu")
                else:
                    print("\nOpération exécutée avec succès !\n")
                    break
            except ValueError:
                print("Erreur : Numéro invalide")
            
    def make_call_nmber(self, number):
        try:
            if number in self.contacts.values():
                print(f"\nAppelant {number} \n ---Sortant de {self.brand}{self.model}---\n")
            else:
                print("Erreur : Numéro inexistant")
                ajout=input(f"\nVoulez-vous ajouter ce numéro ? : ")
                if ajout.lower().strip().replace(" ","") in self.confam:
                    self.add_nmb()
                else:
                    print("Je suppose qu'une prochaine fois.\n")                
        except:
            print("Erreur avec les contacts.\n")
    
    def infos(self):
        quest=input("Client : ")
        if quest.lower().strip().replace(" ","")=="admin":
            Mdp=input("Mot de passe : ")
            if Mdp in self.utilités["Mot_de_pa"]:
                print(f"Infos for an Admin\n-brand: {self.brand}\n--model: {self.model}\n---colour: {self.colour}\n----contacts: {self.contacts}\n-----confirmations: {self.confam}\n------utilités: {self.utilités}")
            else:
                print(f"Usurpateur...")
                return -1
        else:
            print(f"Infos pour {quest}\n-brand: {self.brand}\n--model: {self.model}\n---colour: {self.colour}")
        
def show(a):
    print(f"\n{a}")
    return 0


def main():
    while True:
        global Contacts
        mot_de_confirmation=["oui","ouais","yes","ok","okay","sansprobleme","sansproblème"]
        SER={"sureté":["êtes vous sûr ? : ", "On continue ? : ", "On y go ? : ", "On y va ? : "], "Mot_de_pa":["arepl"]}
        
        A=Phone("Samsung ", "Galaxy S25 Ultra ", "Black ", Contacts, mot_de_confirmation, SER)

        try:
            thg_0=int(input("1- Appel \n2- Voir les contacts \n3- Ajouter un contact \n4- Voir infos \n5- Quitter\n-----------Que veux tu faire ? : "))
            if thg_0==1:
                num=input(f"\nNuméro : ")
                A.make_call_nmber(num)
            elif thg_0==2:
                show(Contacts)
            elif thg_0==3:
                A.add_nmb()
            elif thg_0==4:
                A.infos()
            elif thg_0==5:
                print("Bye")
                break
            else:
                print("Error : -2")            
        except ValueError:
            print("Donne un entier\n")
    
if __name__=="__main__": main()
        
