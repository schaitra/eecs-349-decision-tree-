def chooseBestAttribute(examples):

    countDict = getCountDict(examples,'Class')

    entropy = 0.0
    gain = 0.0
    attributeCount = 0
    valCount = 0
    best = ''

    for (attribute, value) in countDict.iteritems():
        newGain = 0.0
        attributeCount = {}
        valueResults = []
        valueTotals = []
        for (val, targetAtts) in value.iteritems():
            itemCounts = []
            valTotal = 0.0
            valResult = 0.0
            for (item, count) in targetAtts.iteritems():
                if item in attributeCount:
                    attributeCount[item] += 1
                else:
                    attributeCount[item] = 1
                valTotal += count
                itemCounts.append(count)

            for num in itemCounts:
                valResult += num / valTotal * math.log(num / valTotal, 2)

            attributeCount += valCount
            valueResults.append(valResult)
            valueTotals.append(valTotal)

        for (counter, num) in enumerate(valueResults):
            newGain += valueTotals[counter] / len(examples) * num

        if abs(newGain) >= gain:
            gain = abs(newGain)
            best = attribute

    return best