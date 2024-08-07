locations = {
    "Your House": {"North" : "Boat Ramp", "East" : "Optional One", "South" : "School", "West" : "Woods"},
    "Optional One": {"East" : "Tim's Auto Repair"},
    "Tim's Auto Repair": {"South" : "Get It Groceries", "West" : "Optional One"},
    "Get It Groceries": {"North" : "Tim's Auto Repair", "West" : "School"},
    "School": {"North" : "Your House", "East" : "Get It Groceries", "West" : "Abandoned Mansion"},
    "Boat Ramp": {"South" : "Your House", "West" : "Optional Two"},
    "Optional Two": {"East" : "Boat Ramp", "West" : "Uncle Mike's Trailer"},
    "Uncle Mike's Trailer": {"East" : "Optional Two", "South" : "Woods"},
    "Woods": {"North" : "Uncle Mike's Trailer", "East" : "Your House", "South" : "Abandoned Mansion"},
    "Abandoned Mansion": {"North" : "Woods", "East" : "Optional Three"},
    "Optional Three": {"East" : "School", "West" : "Abandoned Mansion"}
}

vowels = ["a", "e", "i", "o", "u"]

inventory = ["rock", "rope", "concrete mix", "shovel"]
currLocation = "Your House"
currMsg = ""