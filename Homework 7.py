# Homework 7 Python Is Easy course
# Steve Boyls

SongDictionary = {"SongTitle" : "Home By The Sea", 
    "Artist": "Genesis", 
    "YearReleased": "1993", 
    "RecordLabel" : "Atlantic Records",
    "Genere" : "Pop",
    "DurationSeconds" : "510",
    "AlbumTitle" : "The Way We Walk: The Longs", 
    "RecordingVenue" : "Live"  
   }

for key in SongDictionary:
    value = SongDictionary[key]
    print(key, " : ", value)
    
def TakeAGuess(k, v):
    if k in SongDictionary:
        value = SongDictionary[k]
        if value == v:   
            return True
        else:          
            return False

Continue = True  

while(Continue):
    print()
    print("Guess a an attribute of my favorit song!")
    print("Enter exit to stop game")
    print()
    key = input("Enter a song attribute: ")
    if key == "exit":
        Continue = False
        print("Continue = ", key)
        print("Game over!")      
    else:
        value = input("Enter an attribute value: ")
        result = TakeAGuess(key, value)
        if result == True:
            print("Great job! You got it right!")
        else:
            print("Sorry, better luck next time")



