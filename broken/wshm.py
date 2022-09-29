import random
words = ["ability", "able", "about", "above", "accept", "according", "account", "across", "act", "action", "activity", "actually", "add", "address", "administration", "admit", "adult", "affect", "after", "again", "against", "age", "agency", "agent", "ago", "agree", "agreement", "ahead", "air", "all", "allow", "almost", "alone", "along", "already", "also", "although", "always", "american", "among", "amount", "analysis", "and", "animal", "another", "answer", "any", "anyone", "anything", "appear", "apply", "approach", "area", "argue", "arm", "around", "arrive", "art", "article", "artist", "as", "ask", "assume", "at", "attack", "attention", "attorney", "audience", "author", "authority", "available", "avoid", "away", "baby", "back", "bad", "bag", "ball", "bank", "bar", "base", "be", "beat", "beautiful", "because", "become", "bed", "before", "begin", "behavior", "behind", "believe", "benefit", "best", "better", "between", "beyond", "big", "bill", "billion", "bit", "black", "blood", "blue", "board", "body", "book", "born", "both", "box", "boy", "break", "bring", "brother", "budget", "build", "building", "business", "but", "buy", "by", "call", "camera", "campaign", "can", "cancer", "candidate", "capital", "car", "card", "care", "career", "carry", "case", "catch", "cause", "cell", "center", "central", "century", "certain", "certainly", "chair", "challenge", "chance", "change", "character", "charge", "check", "child", "choice", "choose", "church", "citizen", "city", "civil", "claim", "class", "clear", "clearly", "close", "coach", "cold", "collection", "college", "color", "come", "commercial", "common", "community", "company", "compare", "computer", "concern", "condition", "conference", "Congress", "consider", "consumer", "contain", "continue", "control", "cost", "could", "country", "couple", "course", "court", "cover", "create", "crime", "cultural", "culture", "cup", "current", "customer", "cut", "dark", "data", "daughter", "day", "dead", "deal", "death", "debate", "decade", "decide", "decision", "deep", "defense", "degree", "democrat", "democratic", "describe", "design", "despite", "detail", "determine", "develop", "development", "die", "difference", "different", "difficult", "dinner", "direction", "director", "discover", "discuss", "discussion", "disease", "do", "doctor", "dog", "door", "down", "draw", "dream", "drive", "drop", "drug", "during", "each", "early", "east", "easy", "eat", "economic", "economy", "edge", "education", "effect", "effort", "eight", "either", "election", "else", "employee", "end", "energy", "enjoy", "enough", "enter", "entire", "environment", "environmental", "especially", "establish", "even", "evening", "event", "ever", "every", "everybody", "everyone", "everything", "evidence", "exactly", "example", "executive", "exist", "expect", "experience", "expert", "explain", "eye", "face", "fact", "factor", "fail", "fall", "family", "far", "fast", "father", "fear", "federal", "feel", "feeling", "few", "field", "fight", "figure", "fill", "southern", "space", "speak", "special", "specific", "speech", "spend", "sport", "spring", "staff", "stage", "stand", "standard", "star", "start", "state", "statement", "station", "stay", "step", "still", "stock", "stop", "store", "story", "strategy", "street", "strong", "structure", "student", "study", "stuff", "style", "subject", "success", "successful", "such", "suddenly", "suffer", "suggest", "summer", "support", "sure", "surface", "system", "table", "take", "talk", "task", "tax", "teach", "teacher", "team", "technology", "television", "tell", "ten", "tend", "term", "test", "than", "thank", "that", "the", "their", "them", "themselves", "then", "theory", "there", "these", "they", "thing", "think", "third", "this", "those", "though", "thought", "thousand", "threat", "three", "through", "throughout", "throw", "thus", "time", "to", "today", "together", "tonight", "too", "top", "total", "tough", "toward", "town", "trade", "traditional", "training", "travel", "treat", "treatment", "tree", "trial", "trip", "trouble", "true", "truth", "try", "turn", "two", "type", "under", "understand", "unit", "until", "upon", "use", "usually", "value", "various", "very", "victim", "view", "violence", "visit", "voice", "vote", "wait", "walk", "wall", "want", "war", "watch", "water", "way", "weapon", "wear", "week", "weight", "well", "west", "western", "what", "whatever", "when", "where", "whether", "which", "while", "white", "who", "whole", "whom", "whose", "why", "wide", "wife", "will", "win", "wind", "window", "wish", "with", "within", "without", "woman", "wonder", "word", "work", "worker", "world", "worry", "would", "write", "writer", "wrong", "yard", "yeah", "year", "yes", "yet", "you", "young", "your", "yourself"]
hangs = ["",
    "    _________\n    |/      |\n" + "    |\n" * 7 + "____|____",
    "    _________\n    |/      |\n    |       O\n" + "    |\n" * 6 + "____|____",
    "    _________\n    |/      |\n    |       O\n" + "    |       |\n" * 2 + "    |\n" * 4 + "____|____",
    "    _________\n    |/      |\n    |       O\n    |      /|\n    |       |\n" + "    |\n" * 4 + "____|____",
    "    _________\n    |/      |\n    |       O\n    |      /|\\\n    |       |\n" + "    |\n" * 4 + "____|____",
    "    _________\n    |/      |\n    |       O\n    |      /|\\\n    |       |\n    |      /\n" + "    |\n" * 2 + "____|____",
    "    _________\n    |/      |\n    |       O\n    |      /|\\\n    |       |\n    |      / \\\n" + "    |\n" * 2 + "____|____"
]

while True:
    reveal = []
    hang = 0
    win = False
    dead = False
    word = random.choice(words)
    while True:
        if hang == 0:
          print("let's play hangman!")
          hang = 1
        print(hangs[hang])
        word2 = [char for char in word]
        availible_letters = [char for char in "abcdefghijklmnopqrstuvwxyz"]
        guess = input("What letter do you guess?")
        for i in range(len(word)):
            if guess[i] == " ": reveal.append(" ")
            else: reveal.append("_")
        for i in [char for char in guess]:
            if i == guess:
                reveal[i] = guess
        availible_letters.remove(guess)
        bad_letters = []
        if guess in word:
          guess = "good"
        else:
          guess = "bad"
        if guess == "bad":
          bad_letters.append(guess)
        print(word2)
        print(availible_letters)
        if guess in word2:
          word_completion = ""
        else:
          hang = int(hang) + 1
        if hang == 8:
          dead = True
          
        if dead or win == True:
          break
    
    if (input("press enter to play again otherwise enter any character")) != "":
      print("Well bye then")
      break
