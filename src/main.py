import random
#how many times the user wants to play
#play = int(input("How many times do you want to play? "))
#how many words does the user want
howManyWords = int(input("How many words do you want? "))
#create a list of 20 prefixes
prefixes = ["anti", "de", "rizz", "great", "fore", "inter", "mid", "mis", "baljit", 
            "over", "tristate", "re", "semi", "sub", "trans", "un", "candice", "up",
            "reeeeee", "super", "bio"
           ]

prefixDef = [" againts a/n"," unduing a/n"," pull ladies", " amazing and great", " before"," between",
             " okish", " wrongly", " smart and nerdy", " too much", 
             " a city that doffenshrits want to concor", " again", " only  partaly", 
             " under"," cross somewehre", " undo", " not smart", " above something", 
             " angry at something", " better that other people", " study of life"
            ]
#create a list of 20 suffixes
suffixes = ["age", "ful", "ing", "less", "ly", "ment", "ness", "ous", "sion",
            "tion" ,"ed", "er", "p", "or", "ish", "en", "ing", "ity", 
             "moogaly"
           ]

suffixesDef = ["Howmany years", "Comlete", "Curently doing", "Not as much", 
               "How something is doing", "State of in", "Condition of", "Full of", 
               "State of" ,"Action of", "Past tense","More of it",
               "Perry the platapus is awsomesause", "One that soed something", 
               "Sorta", "Made of", "Its a action", 
               "It is doing",  
               "Exlamation of supprise"
              ]
#create a list of 20 root words
root_words = ["anthropo" , "chron", "dyna", "dys", "gram",
              "graph","hetero" ,"homo", "hydr", "hypo", "logy", "googaly", 
              "race", "gramp", "perry", "fun", "angent", "ill"
             ]

rootWordsDef = [" humankind." , " life." ," time." ,
                " power bad; hard; unlucky.", " thing written." ," writing.", " different." 
                ," same.", " water.", " below; beneath.", " study of.", " dispair." , 
                " competing.", " cool.", 
                " very good.", " intiresting and intertaining.",
                " doing secret mishons for govemnt.", " not feeling well."
]

for i in range(howManyWords):
  rand1= random.randint(0,len(prefixes)-1)
  rand3= random.randint(0,len(suffixes)-1)
  rand2= random.randint(0,len(root_words)-1)
  print(prefixes[rand1] + "-" + root_words[rand2] + "-"+suffixes[rand3])
  print(suffixesDef[rand3]   + prefixDef[rand1] + rootWordsDef[rand2])