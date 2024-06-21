def percentage_strings_in_whitelist(tags, whitelist):
    if not whitelist:
        return 0
    count = 0
    for tag in tags:
        if any(item in whitelist for item in tag.split()):
            count += 1
    return (count / len(tags)) * 100 if tags else 0


whitelistLegume = [
    'pepene galia', 'ananas', 'pere packmas', 'avocado', 'pepene galben', 'capsuni romanesti',
    'pere abate', 'capsuni', 'clementine', 'coacaze rosii', 'fructul pasiunii', 'grapefruit rosu',
    'lamai', 'limes', 'mandarine', 'mango', 'mix mere', 'mere rosii', 'mere', 'zmeura', 'kiwi',
    'afine', 'lamai', 'portocale', 'avocado', 'mure', 'nuca cocos', 'papaya', 'pepene verde',
    'pere conference', 'physalis', 'piersici', 'portocale', 'struguri albi seedless', 'struguri roze seedless',
    'rodii', 'afine', 'ciuperci galbiori uscati gradina padurii', 'ciuperci uscate trambita piticului',
    'curmale deshidratate jasmin', 'curmale deshidratate', 'ghebe uscate gradina padurii', 'goji deshidratate',
    'merisoare uscate', 'mix fructe uscate power noberasco', 'mix fructe confiate lux', 'prune deshidratate noberasco',
    'prune uscate', 'amestec fructe deshidratate nuci', 'smochine deshidratate noberasco', 'smochine deshidratate',
    'prune uscate fara samburi', 'prune uscate fara samburi', 'rosii cherry alungite'
]

tags = ['pepene', 'ananas', 'avocado', 'mango', 'mere', 'rosii']

max_percentage = 0
best_match = None

for item in whitelistLegume:
    percentage = percentage_strings_in_whitelist(tags, item)
    if percentage > max_percentage:
        max_percentage = percentage
        best_match = item

print(f"The string '{best_match}' has the highest percentage of tags: {max_percentage}%")
