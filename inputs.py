maps = {
    # Africa
    "africa",
    "botswana",
    "eswatini",
    "ghana",
    "kenya",
    "lesotho",
    "madagascar",
    "nigeria",
    "senegal",
    "south-africa",
    "sri-lanka",
    "tunisia",
    "uganda",
    "vietnam",

    # Asia
    "bangladesh",
    "bhutan",
    "cambodia",
    "india",
    "indonesia",
    "israel",
    "japan",
    "jordan",
    "kyrgyzstan",
    "laos",
    "malaysia",
    "mongolia",
    "philippines",
    "russia",
    "singapore",
    "south-korea",
    "taiwan",
    "thailand",


    # Europe
    "albania",
    "andorra",
    "belgium",
    "bulgaria",
    "croatia",
    "czech-republic",
    "denmark",
    "estonia",
    "faroe-islands",
    "finland",
    "france",
    "germany",
    "greece",
    "hungary",
    "iceland",
    "ireland",
    "italy",
    "latvia",
    "lithuania",
    "london",
    "luxembourg",
    "malta",
    "monaco",
    "montenegro",
    "netherlands",
    "north-macedonia",
    "norway",
    "paris",
    "poland",
    "portugal",
    "romania",
    "san-marino",
    "serbia",
    "slovakia",
    "slovenia",
    "spain",
    "sweden",
    "switzerland",
    "turkey",
    "uk",
    "ukraine",

    # North America
    "canada",
    "greenland",
    "guatemala",
    "mexico",
    "newyork",
    "philadelphia",
    "san-francisco",
    "usa",

    # Oceania
    "australia",
    "new-zealand",

    # South America
    "argentina",
    "bolivia",
    "brazil",
    "chile",
    "colombia",
    "ecuador",
    "peru",
    "uruguay",

    #other
    "american-samoa",
    "christmas-island",
    "curacao",
    "dominican-republic",
    "european-union",
    "famous-places",
    "gibraltar",
    "isle-of-man",
    "jersey",
    "northern-mariana-islands",
    "puerto-rico",
    "us-virgin-islands",
    "world",

    #custom map aliases
    "urban-world-nobrr",
    "diverse-world",

}

options = {
    "default",
    "nm",
    "nz",
    "nmz",
    "nmpz",
}

africa = {
    "africa",
    "botswana",
    "eswatini",
    "ghana",
    "kenya",
    "lesotho",
    "madagascar",
    "nigeria",
    "senegal",
    "south-africa",
    "sri-lanka",
    "tunisia",
    "uganda",
}

asia = {
    "bangladesh",
    "bhutan",
    "cambodia",
    "india",
    "indonesia",
    "israel",
    "japan",
    "jordan",
    "kyrgyzstan",
    "laos",
    "malaysia",
    "mongolia",
    "philippines",
    "russia",
    "singapore",
    "south-korea",
    "taiwan",
    "thailand",
    "vietnam",
}

europe = {
    "albania",
    "andorra",
    "belgium",
    "bulgaria",
    "croatia",
    "czech-republic",
    "denmark",
    "estonia",
    "faroe-islands",
    "finland",
    "france",
    "germany",
    "greece",
    "hungary",
    "iceland",
    "ireland",
    "italy",
    "latvia",
    "lithuania",
    "london",
    "luxembourg",
    "malta",
    "monaco",
    "montenegro",
    "netherlands",
    "north-macedonia",
    "norway",
    "paris",
    "poland",
    "portugal",
    "romania",
    "san-marino",
    "serbia",
    "slovakia",
    "slovenia",
    "spain",
    "sweden",
    "switzerland",
    "turkey",
    "uk",
    "ukraine",
}

na = {
    "canada",
    "greenland",
    "guatemala",
    "mexico",
    "newyork",
    "philadelphia",
    "san-francisco",
    "usa",
}

sa ={
    "argentina",
    "bolivia",
    "brazil",
    "chile",
    "colombia",
    "ecuador",
    "peru",
    "uruguay",
}


oceania = {
    "australia",
    "new-zealand",
}

misc = {
    "american-samoa",
    "christmas-island",
    "curacao",
    "dominican-republic",
    "european-union",
    "famous-places",
    "gibraltar",
    "isle-of-man",
    "jersey",
    "northern-mariana-islands",
    "puerto-rico",
    "us-virgin-islands",
    "world",
}

custom = { 
    "urban-world-nobrr",
    "diverse-world",
}

definitions = {
    "default = Play with default settings",
    "nm = Play with the no move setting on.",
    "nz = Play with the no zoom setting on.",
    "nmz = Play with the no move, no zoom setting on.",
    "nmpz = Play with the no move, no pan, no zoom setting on.",
}

# Map and Option check functions

def checkCustom(map):
    if map == "urban-world-nobrr":
        map = "5e818e96b3ec17842c0bcce8"
        return map
    if map == "diverse-world":
        map = "59a1514f17631e74145b6f47"
        return map
    if map == "africa":
        map = "5f4a6c9d8c3ef000010a8fc2"
        return map
    else:
        return map

def checkMap(map):
    if map not in  maps:
        return False
    else:
        return map

def checkOptions(option):
    if option not in  options:
        return False
    else:
        return option

