which = input("What damage type do you want?\n1 - Normal damage\n2 - Critical damage\n3 - Ability damage\nInput here: ")

if which == "1":
    weaponDamage = int(input("Enter the weapon damage: "))
    strength = int(input("Enter your strength: "))
    baseMultiplier = int(input("Enter your base damage multiplier: "))
    postMultiplier = int(input("Enter your post damage multiplier: "))

    damageOutput = (5 + weaponDamage) * (1 + strength / 100) * (1 + baseMultiplier / 100) * (1 + postMultiplier / 100)

    print(damageOutput)

elif which == "2":
    weaponDamage = int(input("Enter the weapon damage: "))
    strength = int(input("Enter your strength: "))
    critDamage = int(input("Enter your crit damage: "))
    baseMultiplier = int(input("Enter your base damage multiplier: "))
    postMultiplier = int(input("Enter your post damage multiplier: "))

    critDamageOutput = (5 + weaponDamage) * (1 + strength / 100) * (1 + baseMultiplier / 100) * (1 + postMultiplier / 100) * (1 + critDamage / 100)

    print(critDamageOutput)

elif which == "3":
    abilityDamage = int(input("Enter your ability damage: "))
    intelligence = int(input("Enter your intelligence: "))
    abilityScaling = int(input("Enter your ability scaling stat: "))
    critDamage = int(input("Enter your crit damage: "))
    baseMultiplier = int(input("Enter your base damage multiplier: "))
    postMultiplier = int(input("Enter your post damage multiplier: "))

    abilityDamageOutput = abilityDamage * (1 + intelligence / 100 * abilityScaling) * (1 + critDamage / 100) * (1 + baseMultiplier / 100) * (1 + postMultiplier / 100)

    print(abilityDamageOutput)
