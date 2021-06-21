maps = {
    # Africa
    "botswana",
    "kenya",
    "lesotho",
    "senegal",
    "south-africa",
    # Asia
    "bangladesh",
    "cambodia",
    "india",
    "indonesia",
    "israel",
    "japan",
    "malaysia",
    "mongolia",
    "philippines",
    "russia",
    "singapore",
    "south-korea",
    "taiwan",
    "thailand",
    # Europe
    "belgium",
    "bulgaria",
    "croatia",
    "czech-republic",
    "denmark",
    "estonia",
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
    "luxembourg",
    "netherlands",
    "norway",
    "poland",
    "portugal",
    "romania",
    "serbia",
    "slovakia",
    "slovenia",
    "spain",
    "sweden",
    "switzerland",
    "turkey",
    "ukraine",
    "uk",
    # North America
    "canada",
    "greenland",
    "guatemala",
    "mexico",
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

    #custom maps
    "5e818e96b3ec17842c0bcce8",
    "59a1514f17631e74145b6f47",

    #custom map aliases
    "urban-world-norbr",
    "diverse-world",
}

options = {
    "default",
    "nm",
    "nz",
    "nmnz",
    "nmnpnz",
}


def checkCustom(map):
    if map == "urban-world-nobrr":
        map = "5e818e96b3ec17842c0bcce8"
        return map
    if map == "diverse-world":
        map = "59a1514f17631e74145b6f47"
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

