weekly_playlist = ["Blinding Lights", "Levitating", "As It Was", "Heat Waves", "Good 4 u"]
print("This is your weekly playlist:", weekly_playlist)

print("This songs will be added to your playlist: ")
weekly_playlist.append("Drivers License")

print("I will add this song to the beginning of your playlist:")
weekly_playlist.insert(0, "Bohemian Rhapsody")
print(weekly_playlist)

print("I will remove this song from your list: ")
weekly_playlist.remove("Good 4 u")
weekly_playlist.index("Levitating")
weekly_playlist.count("As It Was")
print(weekly_playlist)


throwback_thursday = weekly_playlist.copy()
throwback_thursday.reverse()
print(throwback_thursday)

throwback_thursday = weekly_playlist.copy()
throwback_thursday.sort()

print(weekly_playlist)