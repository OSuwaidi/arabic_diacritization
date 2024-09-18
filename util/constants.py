"""
Constants that are used by the model
"""
HARAQAT = ["ْ", "ّ", "ٌ", "ٍ", "ِ", "ً", "َ", "ُ"]
ARAB_CHARS = "ىعظحرسيشضق ثلصطكآماإهزءأفؤغجئدةخوبذتن"
STOPPERS = [".", "؟", "!"]
VALID_ARABIC = HARAQAT + list(ARAB_CHARS) + STOPPERS
BASIC_HARAQAT = {
    "َ": "Fatha  ",
    "ً": "Fathatah           ",
    "ُ": "Damma              ",
    "ٌ": "Dammatan           ",
    "ِ": "Kasra              ",
    "ٍ": "Kasratan           ",
    "ْ": "Sukun              ",
    "ّ": "Shaddah            ",
}
ALL_POSSIBLE_HARAQAT = {
    "": "No Diacritic       ",
    "َ": "Fatha              ",
    "ً": "Fathatah           ",
    "ُ": "Damma              ",
    "ٌ": "Dammatan           ",
    "ِ": "Kasra              ",
    "ٍ": "Kasratan           ",
    "ْ": "Sukun              ",
    "ّ": "Shaddah            ",
    "َّ": "Shaddah + Fatha    ",
    "ًّ": "Shaddah + Fathatah ",
    "ُّ": "Shaddah + Damma    ",
    "ٌّ": "Shaddah + Dammatan ",
    "ِّ": "Shaddah + Kasra    ",
    "ٍّ": "Shaddah + Kasratan ",
}
