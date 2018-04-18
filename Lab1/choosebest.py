def chooseBestAttribute(examples):

    countDict = getCountDict(examples,'Class')

    entropy = 0.0
    gain = float("inf")
    attributeCount = 0
    valCount = 0
    best = ''
    newgain = 0.0

    print gain
    for (attribute, value) in countDict.iteritems():
        print attribute 
        newGain = 0.0
        attributeCount = 0.0
        valueResults = []
        valueTotals = []
        for (val, targetAtts) in value.iteritems():
            itemCounts = []
            valTotal = 0.0
            valResult = 0.0
            for (item, count) in targetAtts.iteritems():
                valTotal += count
                itemCounts.append(count)

            for num in itemCounts:
                valResult -= num / valTotal * math.log(num / valTotal,
                        2)

            attributeCount += valCount
            valueResults.append(valResult)
            valueTotals.append(valTotal)
        
        print ("valueResults",valueResults)
        print ("valueTotals",valueTotals)
        print ("Length",len(examples))

        for (counter, num) in enumerate(valueResults):
            newGain += valueTotals[counter] / len(examples) * num
            print newGain
            gain[attribute] = newGain


    
    print min(gain.values())

    return best