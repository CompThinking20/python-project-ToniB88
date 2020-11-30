#The Drip Machine is a program that tells you if your outift is good or not
#and will give you advie on what you can do to make it better. If your outfit is
#perfect it will say "Nice drip homie". The variables it takes are the inputed
#outfit pieces the user types in, which will be compared to each other to see if
#the outfit is good or not. Each piece has a set outfit but each outfit has it's
#own combination, ie. suits and skirts don't go to together but suits and pants do.

def Wardrobe():
    #These are the lists of clothing the person can choose. There will be more
    #clothing that are in most closets and some not so much
  Shirts = ["A-line Top", "Bardot Top", "Bodysuit"]
  Pants = [" Straight", "Skinny", "Sailor"]
    #This will print out the list so the user can see what clothing is in the lists
    #so they know what to input
  print(Shirts)
  print("Please type in a top.")
  #They put in the article of clothing so the program holds the variable
  Top= input("Top selection: ")

  #The same thing repeats but with different articles of clothing
  print(Pants)
  print("Please type in pants.")
  Pants = input("Pants selection: ")
  # There will be articles of clothing that won't go with each other so this will
  #raise an error to point out the bad choice of clothing
  if str(Top)=="Bodysuit" and str(Pants)=="straight":
      #With each wrong pair there will be advice on how to style the next try
      print("Try again next time. Try flarred pants.")
  else:
      #This prints out a phrase that lets users know they made a perfect outfit
    print(" Nice drip homie")
Wardrobe()

#Debating on wether I should focus on female clothing or do both men and female.
#It would also be nice to have a suggestsion box so that if there is an outfit or clothing
#that looks good it can be added to the program. I'm also unsure of having color
#color matching added to it too. 
