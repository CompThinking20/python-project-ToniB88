#The Drip Machine is a program that tells you if your outift is good or not
#and will give you advie on what you can do to make it better. If your outfit is
#perfect it will say "Nice drip homie". The variables it takes are the inputed
#outfit pieces the user types in, which will be compared to each other to see if
#the outfit is good or not. Each piece has a set outfit but each outfit has it's
#own combination, ie. suits and skirts don't go to together but suits and pants do.
def introduction():
    print(" Welcome to The Drip Machine! This machine will help measure how good your drip is. Don't worry about any hardfeelings as even with the worst drip ADVICE is always given if it's not 100%. A list of clothing will also be shown and you must choose the items you'll be wearing as they are written. Enjoy and I hope you find the perfect drip.\n")
introduction()

def Wardrobe():
    #These are the lists of clothing the person can choose. I only wrote 5 because
    #writing more would take way too long and confusing
  Tops = ["Off Shoulder top", "Long Sleeve top", "Crop top", "Sweater", "T-shirt"]

  Bottoms = ["Leggings", "Flarred jeans", "Boyfriend Jeans", "Sweatpants", "Skirt"]

  Shoes = [ "Flats", "Sneakers", "Wedges","Platforms", "Army Boots"]
    #This will print out the list so the user can see what clothing is in the lists
  Good_drip = ["Flats", "Sneakers", "Wedges","Platforms", "Army Boots""Leggings", "Flarred jeans", "Boyfriend Jeans", "Sweatpants", "Skirt", "Off Shoulder top", "Long Sleeve top", "Crop top", "Sweater", "T-shirt"]
    #so they know what to input
  print(Tops)
  print("Please type in a top from the list.\n")
  #They put in the article of clothing so the program holds the variable
  Top= input("Top selection: ")

  #The same thing repeats but with different articles of clothing
  print(Bottoms)
  print("Please type in pants.")
  Bottom = input("Pants selection: ")

  print(Shoes)
  print("Please type in Shoes.")
  Shoe = input("Shoe selection: ")



  if Good_drip == True:
    print("Good Drip homie")

    if str(Top)=="Off Shoulder top" and str(Bottom)=="Flarred jeans" and str(Shoe)=="Platforms":
      print("Try again next time. Try a skirt with flats.")
      #These are elif statments that if you choose a specific clothing it will give you a
      #specific advice and if you get it right it will tell you "nice drip homie"
  elif str(Top)=="Off Shoulder Top" and str(Bottom)=="Flarred jeans" and str(Shoe)=="Army Boots":
      print("Try again next time.Try some sneakers.")


  elif str(Top)=="Long Sleeve Top" and str(Bottom)== "Leggings" and str(Shoe)== "Flats" or "Sneakers" or "Wedges" or "Platforms" or "Army Boots":
      print("Try again next time. Try some boyfriend jeans with flats.")
  elif str(Top)=="Long Sleeve Top" and str(Bottom)== "Flarred jeans" and str(Shoe)== "Flats" or "Sneakers" or "Wedges" or "Platforms" or "Army Boots":
      print("Try again next time. Try some boyfriend jeans with sneakers.")
  elif str(Top)=="Long Sleeve Top" and str(Bottom)== "Sweatpants" and str(Shoe)== "Flats" or"Sneakers" or "Wedges" or "Platforms" or "Army Boots":
      print("Try again next time. Try some boyfriend jeans with army boots.")
  elif str(Top)=="Long Sleeve Top" and str(Bottom)== "Skirt" and str(Shoe)== "Flats" or "Sneakers" or "Wedges" or "Platforms" or "Army Boots":
      print("Try again next time. Try some boyfriend jeans wwith platforms.")

  elif str(Top)=="Crop top" and str(Bottom)== "Flarred jeans" and str(Shoe)== "Flats" or "Sneakers" or "Wedges" or "Platforms" or "Army Boots":
      print("Try again next time. Try some sweatpants with army boots.")

  elif str(Top)=="Sweater" and str(Bottom)== "Sweatpants" and str(Shoe)== "Flats" or "Sneakers" or "Wedges" or "Platforms" or "Army Boots":
      print("Try again next time. Try a skirt with platforms.")
  elif str(Top)=="T-shirt" and str(Bottom)== "Flarred jeans" and str(Shoe)== "Flats" or "Sneakers" or "Wedges" or "Platforms" or "Army Boots":
      print("Try again next time. Try some leggings with some sneakers.")
  else:
      print("Wrong input dude.")
      #This prints out a phrase that lets users know they made a perfect outfit
    print(" Nice drip homie")
Wardrobe()


#Fixed on womans clothing but not sure how to get it so that when someone puts in
#gobbldy gook the program desn't take it and stops them and has them rewrite in answer
