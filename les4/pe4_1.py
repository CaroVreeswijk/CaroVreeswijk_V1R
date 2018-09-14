x = 30
cijferICOR = 6.0
cijferPROG = 7.0
cijferCSN = 6.3

gemiddelde = (cijferICOR + cijferPROG + cijferCSN) / 3
print(gemiddelde)

beloning = cijferCSN*x + cijferPROG*x + cijferICOR*x
print(beloning)


overzicht = 'Mijn cijfers van ' + str(cijferICOR)+', ' + str(cijferPROG )+', ' + 'en ' + str(cijferCSN) + ' leveren een belonging van € '+ str(beloning)+' op!'
print(overzicht)
