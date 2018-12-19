SongTitle = "Home By The Sea"
Artist = "Genesis"
YearReleased = "1993"
RecordLabel = "Atlantic Records"
Genere = "Pop"
DurationSeconds = 510
AlbumTitle = "The Way We Walk: The Longs"
RecordingType = "Live"



def getGenere():
    return Genere

def getArtist():
    return Artist

def getYear():
    return YearReleased

def isEven(number):
    if (number%2) > 0:
        return False
    if (number%2) == 0:
        return True

print(getGenere())
print(getArtist())
print(getYear())

print(isEven(5))
print(isEven(6))
