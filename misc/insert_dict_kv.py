# https://techbeamers.com/python-program-insert-a-key-value-pair-to-the-dictionary/

# Call the update() method to insert the key-value pair to the dictionary.

aKey = 10
aValue = 500

aDict = {10:100, 15:120, 16:200}

aDict.update({aKey:aValue}) # it updates the value if key is already present
print(aDict)