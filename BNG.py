import random


titles = ["Gigantic","sour","steamy","gross","stupid",
		  "ironic","greasy","tangy","smelly","small",
		  "inventive","spherical", "Spiritual","green",
		  "blue", "pot bellied", "pickled", "prickly"]

adjs = ["tiny", "fat", "shiny", "ecclectic","fluffy", "bright",
		"corrupt", "aggressive", "alarming", "amazing", "magical",
		"courageous", "fierce", "colorlessds", "red", "thoughtless",
		"smart", "delirious","fabulous","fergaliciouss", "dangerous"]

plural_nouns = ["apples","oranges","kiwis","clementines",
				"wildabeasts", "mammoths", "rabbits", "sloths",
				"spices", "eggs","herbs", "pony tails","bears",
				"unicorns", "kermits", "signs", "indians", "cowboys"]

def title():
	return random.choice(titles)

def adj():
	return random.choice(adjs)

def plural_noun():
	return random.choice(plural_nouns)

def main():
	while True:
		name = raw_input("Enter your name: ")
		if name == "q":
			break
		random.seed(name)
		print title(), name, "and the", adj(), plural_noun()

main()