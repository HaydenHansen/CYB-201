#Hayden Hansen
#Python encrytpion game
import sys
YesNo = ["yes", "no"]
directions = ["PGP", "SHA1","Des","AES"]
name = input("Welcome travler, before we can begin we must know you name: ")
print("Welcome " + name + " now that we have become friends we can travel into the forest of encryptions!")
print("Are you ready! (yes/no)")
answer = input()
if answer == "no":
    print("then why have you come travler")
    print("go away until you're ready to go")
    sys.exit()
else:
    print("then let us begin!")
    print("this game can be ran 5 times in a row so explore every option!")

count = 0
while count < 5:
    print("")
    print("")
    print("")
    print("")
    print("")
    print("Quickly "+ name +" we must choose a direction to encrypt fast as this forest is brimming with hackers")
    print("choose a way to go! But be wary one wrong move in this forest will lead to certain death!")
    print("Charge forward blindly into the forest towards the PGP Encryption")
    print("Retreat towards the way we came into the SHA1 Encryption")
    print("Sidestep to the right into the Des encryption method")
    print("Barrel to the left towards the AES Encryption")
    print("Jump into the branches above your head into the SHA3 Encryption")
    print("Enter the encryption method you wish to head too: PGP, SHA1, Des, AES, or SHA3")
    response = input()
    if response == "PGP":
        print("You charge blindly into the forst of encryption and quickly find yourself breached, unfortunally PGP is not the best encryption method. First of all PGP is old, and is losing support on newer devices and when computers become able to handle better encyption methods. This being the case you have lost by choosing this method")
        count = count + 1
    if response == "SHA1":
        print("While retreating towards the SHA1 ecryption you slipped on a banana peel and died. SHA1 is old has has become obsolete in the ways of encryption, becomeing trivial for well funded groups to hack. In addition many web vendors have removed support for acceptance of this encryption method.")
        count = count + 1
    if response == "Des":
        print("You sidestep to the left towards the Des encryption method, but find yourself quickly out numbered by those who saw through your move. des is an outdated security method with a relativly short key length that leads to hackers being able to break through quickly, for example there was a public event in which they broke a DES key in just 22 hours")
        count = count + 1
    if response == "AES":
        print("You barrel to the left towards the AES encryption, a great choice, allowing safe passage through the forest. AES is the advencement of the DES method, included in many standards of encryption, even used in the NSA for top secret information protection. The key lengths in AES are all longer than DES providing more security.")
        count = count + 1
    if response == "SHA3":
        print("You jump up into the SHA3 Encryption branches, a great choice that allows passage through the forest. The SHA3 encryption is relativly new, and provides a good amount of security with encyrption. In compasrison to SHA1 and 2 is a different type of hash method, and while SHA3 is not meant to replace SHA2 it was meant to be a different type in order to provide an alternative.")
        count = count + 1
    
