# TPK4186 - 2023 - Assignment 1

# Fredrik Faanes Slagsvold, Group: Fredrik Faanes Slagsvold

# ---------------------
# 1. Imported modules
# ---------------------

import sys
import random
import string
import time

# ---------------------
# 2. Containers
# ---------------------

def Container_New(serialNumber, length, weight, cargo):
    # 40: Require: 0 <= cargo <= 22 20: Require: 0 <= cargo <= 20
    return [serialNumber, length, weight, cargo]

def Container_NewSmall(serialNumber, cargo):
        # Require: 0 <= cargo <= 20
    return Container_New(serialNumber, 20, 2, cargo)

def Container_NewBig(serialNumber, cargo):
    # Require: 0 <= cargo <= 20

    return Container_New(serialNumber, 40, 4, cargo)

def Container_GetSerialNumber(container):
    return container[0]

def Container_SetSerialNumber(container, serialNumber):
    container[0] = serialNumber
    
def Container_GetLength(container):
    return container[1]

def Container_SetLength(container, length):
    container[1] = length

def Container_GetWeight(container):
    totalWeight = 0
    if len(container) != 2:
        return int(container[2])
    else:
        for subContainer in container:
            totalWeight += int(subContainer[2])
        return totalWeight

def Container_SetWeight(container, weight):
    container[2] = weight


def Container_GetCargo(container):
    totalWeight = 0
    if len(container) != 2:
        return int(container[3])
    else:
        for subContainer in container:
            totalWeight += int(subContainer[3])
        return totalWeight

def Container_SetCargo(container, cargo):
    container[3] = cargo
    

def Container_GetTotalWeight(container):
    return Container_GetWeight(container) + Container_GetCargo(container)



def Container_GenerateSerialNumber():
    randomFirstLetter = random.choice(string.ascii_uppercase)
    randomSecondLetter = random.choice(string.ascii_uppercase)
    randomThirdLetter = random.choice(string.ascii_uppercase)
    randomNumber = ""
    for i in range(0,5):
        randomNumber += str(random.randint(0,9))
    serialNumber = "{}{}{}-{}".format(\
        randomFirstLetter, randomSecondLetter, randomThirdLetter, randomNumber)
    return serialNumber


def Container_GenerateRandomContainer():
    available_sizes = [20, 40]
    serialNumber = Container_GenerateSerialNumber()
    size_chosen = random.choice(available_sizes)
    if size_chosen == 20:
        cargo = random.randint(0, 20)
        container = Container_NewSmall(serialNumber, cargo)
    else:
        cargo = random.randint(0, 22)
        container = Container_NewBig(serialNumber, cargo)
    return container

def Container_GenerateRandomEmptyContainer():
    available_sizes = [20, 40]
    serialNumber = Container_GenerateSerialNumber()
    size_chosen = random.choice(available_sizes)
    if size_chosen == 20:
        cargo = 0
        container = Container_NewSmall(serialNumber, cargo)
    else:
        cargo = 0
        container = Container_NewBig(serialNumber, cargo)
    return container

def Container_GenerateRandomFullContainer():
    available_sizes = [20, 40]
    serialNumber = Container_GenerateSerialNumber()
    size_chosen = random.choice(available_sizes)
    if size_chosen == 20:
        cargo = 20
        container = Container_NewSmall(serialNumber, cargo)
    else:
        cargo = 22
        container = Container_NewBig(serialNumber, cargo)
    return container


# --------------------
# 3. Container Set
# --------------------

def ContainerSet_GenerateRandomContainerSet(numberOfContainers):
    container_set = []
    for i in range(0, numberOfContainers):
        container = Container_GenerateRandomContainer()
        container_set.append(container)
    return container_set

def ContainerSet_GenerateRandomEmptyContainerSet(numberOfContainers):
    container_set = []
    for i in range(0, numberOfContainers):
        container = Container_GenerateRandomEmptyContainer()
        container_set.append(container)
    return container_set

def ContainerSet_GenerateRandomFullContainerSet(numberOfContainers):
    container_set = []
    for i in range(0, numberOfContainers):
        container = Container_GenerateRandomFullContainer()
        container_set.append(container)
    return container_set


def ContainerSet_PairSmallContainers(containerSet):
    pairOfSmallContainers = []
    fixedContainerSet = []
    for container in containerSet:
        if Container_GetLength(container) == 20:
            if len(pairOfSmallContainers) == 1:
                pairOfSmallContainers.append(container)
                fixedContainerSet.append(pairOfSmallContainers)
                pairOfSmallContainers = []
            else:
                pairOfSmallContainers.append(container)
        else:
            fixedContainerSet.append(container)
    return fixedContainerSet


def ContainerSet_CountPairOf20s(containerSet):
    count = 0
    for container in containerSet:
        if (Container_GetLength(container) == 20):
            count += 1
    return count

def ContainerSet_CountPairOf20sInFixed(containerSet):
    count = 0
    for container in containerSet:
        if (Container_GetLength(container) == 20):
            count += 1
        elif len(container) == 2:
            count += 2
    return count


# -------------------
# 4. Sections
# -------------------


def Section_FrontStarboard():
    stack = []
    return [stack for i in range(4*11)]

def Section_FrontPortside():
    stack = []
    return [stack for i in range(4*11)]

def Section_MiddleStarboard():
    stack = []
    return [stack for i in range(4*11)]

def Section_MiddlePortside():
    stack = []
    return [stack for i in range(4*11)]

def Section_BackStarboard():
    stack = []
    return [stack for i in range(4*11)]

def Section_BackPortside():
    stack = []
    return [stack for i in range(4*11)]


# --------------------
# 5. Ships
# --------------------


def Ship_New(length, width, height):
    return [length, width, height, [Section_FrontStarboard(), Section_FrontPortside(), Section_MiddleStarboard(), Section_MiddlePortside(), Section_BackStarboard(), Section_BackPortside()]]


def Ship_GetLength(ship):
    return ship[0]

def Ship_SetLength(ship, length):
    ship[0] = length

def Ship_GetWidth(ship):
    return ship[1]

def Ship_SetWidth(ship, width):
    ship[1] = width

def Ship_GetHeight(ship):
    return ship[2]

def Ship_SetHeight(ship, height):
    ship[2] = height

def Ship_GetListOfSections(ship):
    return ship[3]

def Ship_GetSectionFrontStarboard(ship):
    return ship[3][0]

def Ship_GetSectionFrontPortside(ship):
    return ship[3][1]

def Ship_GetSectionMiddleStarboard(ship):
    return ship[3][2]

def Ship_GetSectionMiddlePortside(ship):
    return ship[3][3]

def Ship_GetSectionBackStarboard(ship):
    return ship[3][4]

def Ship_GetSectionBackPortside(ship):
    return ship[3][5]

def Ship_GetNthSection(ship, sectionNumber):
    # 0 ≤ x ≤ 5
    return ship[3][sectionNumber]

def Ship_GetContainers(ship):
    containers = []
    sections = Ship_GetListOfSections(ship)
    for section in sections:
        for stack in section:
            for stackedContainer in stack:
                containers.append(stackedContainer)
    return containers


def Ship_GetNthStackFromNthSection(ship, sectionIndex, stackIndex):
    # 0 ≤ n ≤ 5
    chosenSection = Ship_GetNthSection(ship, sectionIndex)
    chosenStack = chosenSection[stackIndex]
    return chosenStack

def Ship_PopContainerFromNthStack(ship, sectionIndex, stackIndex):
    chosenStack = Ship_GetNthStackFromNthSection(ship, sectionIndex, stackIndex)
    chosenStack.pop()

def Ship_GetNumberOfStacksInSection(sectionNumber):
    return len(Ship_GetNthSection(sectionNumber))


def Ship_FindContainerInShip(ship, container):
    sections = Ship_GetListOfSections(ship)
    found = False
    for sectionIndex, section in enumerate(sections):
        for stackIndex, stack in enumerate(section):
            for containerIndex, stackedContainer in enumerate(stack):
                if len(stackedContainer) == 2:
                    for subContainerIndex, subContainer in enumerate(stackedContainer):
                        if Container_GetSerialNumber(subContainer) == Container_GetSerialNumber(container):
                            found = True
                            return f"Container: {container} found in section: {sectionIndex}, stack: {stackIndex}, floor: {containerIndex}, containerpair index: {subContainerIndex}"
                else:
                    if stackedContainer == container:
                        found = True
                        return f"Container: {container} found in section: {sectionIndex}, stack: {stackIndex}, floor: {containerIndex}"
    if found == False:
        return f"Container: {container} not found!"


def Ship_GetNthSectionLoad(ship, n):
    ShipLoad = Ship_GetListOfSections(ship)
    sectionWeight = 0
    chosenSection = ShipLoad[n]
    weight = 0
    for stack in chosenSection:
        for container in stack:
            if (Container_GetWeight(container) != None) and (Container_GetCargo(container) != None):
                weight = Container_GetTotalWeight(container)
                sectionWeight += weight
            else: None
    return sectionWeight

def Ship_GetTotalShipLoad(ship):
    totalWeight = 0
    sections = Ship_GetListOfSections(ship)
    for i in range(len(sections)):
        totalWeight += Ship_GetNthSectionLoad(ship, i)
    return totalWeight

def Ship_GetLoadStarboardSide(ship):
    totalWeight = 0
    sections = Ship_GetListOfSections(ship)
    for i in range(0, len(sections), 2):
        totalWeight += Ship_GetNthSectionLoad(ship, i)
    return totalWeight

def Ship_GetLoadPortsideSide(ship):
    totalWeight = 0
    sections = Ship_GetListOfSections(ship)
    for i in range(1, len(sections), 2):
        totalWeight += Ship_GetNthSectionLoad(ship, i)
    return totalWeight

def Ship_GetLoadFrontSection(ship):
    totalWeight = 0
    for i in range(2):
        totalWeight += Ship_GetNthSectionLoad(ship, i)
    return totalWeight

def Ship_GetLoadMiddleSection(ship):
    totalWeight = 0
    for i in range(2, 4):
        totalWeight += Ship_GetNthSectionLoad(ship, i)
    return totalWeight

def Ship_GetLoadBackSection(ship):
    totalWeight = 0
    for i in range(4, 6):
        totalWeight += Ship_GetNthSectionLoad(ship, i)
    return totalWeight

def Ship_isBalanced(ship):
    balanced = False
    lightestSectionindex = Ship_GetLightestSectionIndex(ship)
    lightestSectionWeight = Ship_GetNthSectionLoad(ship, lightestSectionindex)
    heaviestSectionIndex = Ship_GetHeaviestSectionIndex(ship)
    heaviestSectionWeight = Ship_GetNthSectionLoad(ship, heaviestSectionIndex)
    weightStarboard = Ship_GetLoadStarboardSide(ship)
    weightPortside = Ship_GetLoadPortsideSide(ship)
    maxPercentDifferenceInSections = 0
    percentDifferenceStarboardPortside = 0
    if heaviestSectionWeight != 0:
        maxPercentDifferenceInSections = 100 - (lightestSectionWeight/heaviestSectionWeight)*100
    if weightStarboard != 0 and weightPortside != 0:
        if weightStarboard < weightPortside:
            percentDifferenceStarboardPortside = 100 - (weightStarboard/weightPortside)*100
        else:
            percentDifferenceStarboardPortside = 100 - (weightPortside/weightStarboard)*100
    if maxPercentDifferenceInSections <= 10 and percentDifferenceStarboardPortside <= 5:
        balanced = True
    return balanced, percentDifferenceStarboardPortside, maxPercentDifferenceInSections


def Ship_GetLightestSectionIndex(ship):
    shipLoad = Ship_GetListOfSections(ship)
    lightestSectionWeight = 0
    currentSectionIndex = 0
    nextSectionWeight = 0
    for i in range(len(shipLoad)):
        lightestSectionWeight = Ship_GetNthSectionLoad(ship, currentSectionIndex)
        nextSectionWeight = Ship_GetNthSectionLoad(ship, i)
        if nextSectionWeight < lightestSectionWeight:
            lightestSectionWeight = nextSectionWeight
            currentSectionIndex = i
    return currentSectionIndex

def Ship_GetLightestSection(ship):
    lighestSectionIndex = Ship_GetLightestSectionIndex(ship)
    return Ship_GetNthSection(ship, lighestSectionIndex)

def Ship_GetHeaviestSectionIndex(ship):
    shipLoad = Ship_GetListOfSections(ship)
    heaviestSectionWeight = 0
    currentSectionIndex = 0
    nextSectionWeight = 0
    for i in range(len(shipLoad)):
        heaviestSectionWeight = Ship_GetNthSectionLoad(ship, currentSectionIndex)
        nextSectionWeight = Ship_GetNthSectionLoad(ship, i)
        if nextSectionWeight > heaviestSectionWeight:
            heaviestSectionWeight = nextSectionWeight
            currentSectionIndex = i
    return currentSectionIndex

def Ship_GetHeaviestSection(ship):
    heaviestSectionIndex = Ship_GetHeaviestSectionIndex(ship)
    return Ship_GetNthSection(ship, heaviestSectionIndex)


def Ship_GetLoadFromNthStackInSection(ship, sectionIndex, stackIndex):
    # 0 ≤ n ≤ 5
    weight = 0
    chosenSection = Ship_GetNthSection(ship, sectionIndex)
    chosenStack = chosenSection[stackIndex]
    for container in chosenStack:
        weight += Container_GetTotalWeight(container)
    return weight

def Ship_GetLoadFromChosenStack(ship, stack):
    totalWeight = 0
    for container in stack:
        containerWeight = Container_GetTotalWeight(container)
        totalWeight += containerWeight
    return totalWeight

def Ship_GetLightestStackIndexInSection(ship, sectionIndex):
    chosenSection = Ship_GetNthSection(ship, sectionIndex)
    chosenStackIndex = 0
    for i in range(len(chosenSection)):
        if Ship_GetLoadFromNthStackInSection(ship, sectionIndex, i) < Ship_GetLoadFromNthStackInSection(ship, sectionIndex,chosenStackIndex):
            chosenStackIndex = i
    return chosenStackIndex

def Ship_GetHeaviestStackIndexInSection(ship, sectionIndex):
    chosenSection = Ship_GetNthSection(ship, sectionIndex)
    chosenStackIndex = 0
    for i in range(len(chosenSection)):
        if Ship_GetLoadFromNthStackInSection(ship, sectionIndex, i) > Ship_GetLoadFromNthStackInSection(ship, sectionIndex,chosenStackIndex):
            chosenStackIndex = i
    return chosenStackIndex

def Ship_GetHeaviestStackInSection(ship, sectionIndex):
    chosenSection = Ship_GetNthSection(ship, sectionIndex)
    stackIndex = Ship_GetHeaviestStackIndexInSection(ship, sectionIndex)
    return chosenSection[stackIndex]


def Ship_GetLightestStackInSection(ship, sectionIndex):
    chosenSection = Ship_GetNthSection(ship, sectionIndex)
    stackIndex = Ship_GetLightestStackIndexInSection(ship, sectionIndex)
    return chosenSection[stackIndex]
    
def Ship_findLightestFirstAvailableStack(ship, sectionIndex):
    chosenSection = Ship_GetNthSection(ship, sectionIndex)
    availableStacks = []
    for i in range(len(chosenSection)):
        if len(chosenSection[i]) < 18:
            availableStacks.append(chosenSection[i])
    availableStacks.sort(key = lambda stack : Ship_GetLoadFromChosenStack(ship, stack))
    if len(availableStacks) > 0:
        return availableStacks[0]
    else: 
        return None

def Ship_GetIndexOfSectionWithAvailableStack(ship):
    sections = Ship_GetListOfSections(ship)
    lightestAvailableSectionIndex = 0
    for i in range(len(sections)):
        newSectionIndex = i
        if (Ship_findLightestFirstAvailableStack(ship, newSectionIndex) != None) and (Ship_GetNthSectionLoad(ship, newSectionIndex) < Ship_GetNthSectionLoad(ship, lightestAvailableSectionIndex)):
            lightestAvailableSectionIndex = newSectionIndex
    return lightestAvailableSectionIndex


def Ship_findLightestRemainingStacks(ship):
    sections = Ship_GetListOfSections(ship)
    availableStacks = []
    for section in sections:
        for stack in section:
            if len(stack) < 18:
                availableStacks.append(stack)
    availableStacks.sort(key = lambda stack : Ship_GetLoadFromChosenStack(ship, stack))
    if len(availableStacks) > 0:
        return availableStacks[0]
    else:
        return None


def Ship_PlaceContainerAndSortStack(ship, stack, container):
    poppedContainers = []
    newContainerWeight = Container_GetTotalWeight(container)
    index = len(stack)-1
    operations = 0

    while index >= 0:
        if (Container_GetTotalWeight(stack[index])) < newContainerWeight:
            poppedContainers.append(stack[index])
            operations += 1
            stack.remove(stack[index])
        index -= 1

    stack.append(container)
    operations += 1
    for i in range(len(poppedContainers)-1, -1, -1):
        stack.append(poppedContainers[i])
        operations += 1
    return operations


def Ship_IsShipFullyLoaded(ship):
    stacks = Ship_findLightestRemainingStacks(ship)
    if stacks == None:
        return True
    else: return False

def Ship_isEmpty(ship):
    empty = True
    sections = Ship_GetListOfSections(ship)
    for section in sections:
        for stack in section:
            if len(stack) != 0:
                empty = False
    return empty


def Ship_loadSingleContainer(ship, container):
    chosenSectionIndex = 0
    stackIndex = 0
    chosenSectionIndex = Ship_GetLightestSectionIndex(ship)
    chosenSection = Ship_GetNthSection(ship, chosenSectionIndex)
    stackIndex = Ship_GetLightestStackIndexInSection(ship, chosenSectionIndex)
    chosenStack = chosenSection[stackIndex]
    operations = 0
    operationsFront = 0
    operationsMiddle = 0
    operationsBack = 0

    if len(chosenSection[stackIndex]) == 0:
        chosenSection[stackIndex] = [container]
    else:            
        if len(chosenStack) < 18:
            operations += Ship_PlaceContainerAndSortStack(ship, chosenStack, container)
        else:
            nextStack = Ship_findLightestFirstAvailableStack(ship, chosenSectionIndex)
            if nextStack != None:
                operations += Ship_PlaceContainerAndSortStack(ship, nextStack, container)
            else: 
                nextStack = Ship_findLightestRemainingStacks(ship)
                if nextStack != None:
                    operations += Ship_PlaceContainerAndSortStack(ship, nextStack, container)

    if chosenSectionIndex == 0 or chosenSectionIndex == 1:
        operationsFront += operations
    elif chosenSectionIndex == 2 or chosenSectionIndex == 3:
        operationsMiddle += operations
    elif chosenSectionIndex == 4 or chosenSectionIndex == 5:
        operationsBack += operations

    return operationsFront, operationsMiddle, operationsBack


def Ship_loadCargo(ship, containerSet):
    fixedContainerSet = ContainerSet_PairSmallContainers(containerSet)
    totalOperations = 0
    operationsFront = 0
    operationsMiddle = 0
    operationsBack = 0
    for container in fixedContainerSet:
        totalOperations = Ship_loadSingleContainer(ship, container)
        operationsFront += totalOperations[0]
        operationsMiddle += totalOperations[1]
        operationsBack += totalOperations[2]

    if Ship_IsShipFullyLoaded(ship) == True:
        return operationsFront, operationsMiddle, operationsBack, "The ship is fully loaded!"
    return operationsFront, operationsMiddle, operationsBack, "There is still available space on the ship!"

                
def Ship_RemoveContainerFromShip(ship, container):
    sections = Ship_GetListOfSections(ship)
    found = False
    poppedContainers = []
    for section in sections:
        for stack in section:
            for stackedContainerIndex, stackedContainer in enumerate(stack):
                if len(stackedContainer) == 2:
                    for subContainer in stackedContainer:
                        if Container_GetSerialNumber(subContainer) == Container_GetSerialNumber(container):
                            found = True
                            for i in range(len(stack)-1, stackedContainerIndex, -1):
                                poppedContainer = stack[i]
                                poppedContainers.append(poppedContainer)
                                stack.remove(poppedContainer)
                            stack.remove(stackedContainer)
                            for i in range(len(poppedContainers)-1, -1, -1):
                                stack.append(poppedContainers[i])
                            return f"Container: {container} successfully removed from ship!"
                else:
                    if stackedContainer == container:
                        found = True
                        for i in range(len(stack)-1, stackedContainerIndex, -1):
                            poppedContainer = stack[i]
                            poppedContainers.append(poppedContainer)
                            stack.remove(poppedContainer)
                        stack.remove(stackedContainer)
                        for i in range(len(poppedContainers)-1, -1, -1):
                            stack.append(poppedContainers[i])
                        return f"Container: {container} successfully removed from ship!"

    if found == False:
        return f"Container: {container} not found!"

def Ship_UnloadShip(ship):
    popped = []
    operationsFront = 0
    operationsMiddle = 0
    operationsBack = 0

    while Ship_isEmpty(ship) != True:
        chosenSectionIndex = Ship_GetHeaviestSectionIndex(ship)
        chosenStack = Ship_GetHeaviestStackInSection(ship, chosenSectionIndex)
        popped.append(chosenStack.pop())
        if chosenSectionIndex == 0 or chosenSectionIndex == 1:
            operationsFront += 1
        elif chosenSectionIndex == 2 or chosenSectionIndex == 3:
            operationsMiddle += 1
        elif chosenSectionIndex == 4 or chosenSectionIndex == 5:
            operationsBack += 1
    return popped, ship, operationsFront, operationsMiddle, operationsBack


def Ship_CountContainersInShip(ship):
    count = 0
    sections = Ship_GetListOfSections(ship)
    for section in sections:
        for stack in section:
            for stackedContainer in stack:
                if len(stackedContainer) != 2:
                    count += 1
                else:
                    count += 2
    return count


def Ship_CalculateTimeToLoadShipOneCrane(ship, containerSet):
    operationsFront, operationsMiddle, operationsBack, message = Ship_loadCargo(ship, containerSet)
    totalOperations = operationsFront + operationsMiddle + operationsBack
    minutesUsed = totalOperations * 4
    hoursUsed = minutesUsed/60
    daysUsed = hoursUsed/24
    return round(daysUsed, 1)

def Ship_CalculateTimeToLoadShipOneCraneWithAssumption(ship):
    numberOfContainers = Ship_CountContainersInShip(ship)
    minutesUsed = numberOfContainers * 4
    hoursUsed = minutesUsed/60
    daysUsed = hoursUsed/24
    return round(daysUsed, 1)

def Ship_CalculateTimeToUnloadShipOneCrane(ship):
    popped, ship, operationsFront, operationsMiddle, operationsBack = Ship_UnloadShip(ship)
    totalOperations = operationsFront + operationsMiddle + operationsBack
    minutesUsed = totalOperations * 4
    hoursUsed = minutesUsed/60
    daysUsed = hoursUsed/24
    return round(daysUsed, 1)

def Ship_CalculateTimeToLoadShipThreeCranes(ship, containerSet):
    operationsFront, operationsMiddle, operationsBack, message = Ship_loadCargo(ship, containerSet)
    if operationsFront >= operationsMiddle and operationsFront >= operationsBack:
        largestOperationsCount = operationsFront
    elif operationsMiddle >= operationsFront and operationsMiddle >= operationsBack:
        largestOperationsCount = operationsMiddle
    elif operationsBack >= operationsFront and operationsBack >= operationsMiddle:
        largestOperationsCount = operationsBack

    minutesUsed = largestOperationsCount * 4
    hoursUsed = minutesUsed/60
    daysUsed = hoursUsed/24
    return round(daysUsed, 1)

def Ship_CalculateTimeToUnloadShipThreeCranes(ship):
    popped, ship, operationsFront, operationsMiddle, operationsBack = Ship_UnloadShip(ship)
    if operationsFront >= operationsMiddle and operationsFront >= operationsBack:
        largestOperationsCount = operationsFront
    elif operationsMiddle >= operationsFront and operationsMiddle >= operationsBack:
        largestOperationsCount = operationsMiddle
    elif operationsBack >= operationsFront and operationsBack >= operationsMiddle:
        largestOperationsCount = operationsBack

    minutesUsed = largestOperationsCount * 4
    hoursUsed = minutesUsed/60
    daysUsed = hoursUsed/24
    return round(daysUsed, 1)

# --------------
# 6: Printer
# --------------

def Printer_PrintContainer(container):
    serialNumber = Container_GetSerialNumber(container)
    length = Container_GetLength(container)
    weight = Container_GetWeight(container)
    cargo = Container_GetCargo(container)
    totalWeight = Container_GetTotalWeight(container)
    print(str(serialNumber) + " " + str(length) + " " + str(weight) + " " + str(cargo) + " " + str(totalWeight))


def Printer_PrintShipSections(ship):
    ShipLoad = Ship_GetListOfSections(ship)
    for sectionIndex, section in enumerate(ShipLoad):
        print(f"\nSection {sectionIndex}: \n")
        firstRow = section[0:11]
        secondRow = section[11:22]
        thirdRow = section[22:33]
        fourthRow = section[33:44]
        print(f"{firstRow}\n{secondRow}\n{thirdRow}\n{fourthRow}\n")


def Printer_PrintShip(ship):
    length = Ship_GetLength(ship)
    width = Ship_GetWidth(ship)
    height = Ship_GetHeight(ship)
    sections = Ship_GetListOfSections(ship)
    print(f"Length:{length}\nWidth: {width}\nHeight: {height}\n{sections}")


def Printer_PrintNumberOfContainersInFloors(ship):
    sections = Ship_GetListOfSections(ship)
    floorCounts = [0 for i in range(18)]
    print("\nNumber of container spaces used on each floor: \n")
    for section in sections:
        for stack in section:
            for i, container in enumerate(stack):
                if i < len(floorCounts):
                    floorCounts[i] += 1
    floorLabels = ['First', 'Second', 'Third', 'Fourth', 'Fifth',
                    'Sixth', 'Seventh', 'Eighth', 'Ninth', 'Tenth',
                    'Eleventh', 'Twelfth', 'Thirteenth', 'Fourteenth',
                    'Fifteenth', 'Sixteenth', 'Seventeenth', 'Eighteenth']
    for i, floorCount in enumerate(floorCounts):
        print(f"{floorLabels[i]} floor: {floorCount}")
    print()


def Printer_PrintSectionWithWeightOfStacks(ship):
    sections = Ship_GetListOfSections(ship)
    print("\nWeight of each stack in each section: ")
    for sectionIndex, section in enumerate(sections):
        print(f"\nSection {sectionIndex}: \n")
        for i in range(4):
            for j in range(11):
                stackIndex = i + j * 4
                if stackIndex < len(section):
                    print(f"{Ship_GetLoadFromNthStackInSection(ship, sectionIndex, stackIndex)}\t", end='')
            print('\n', end='')
    print()

def Printer_PrintNumberOfContainersInShip(ship):
    count = Ship_CountContainersInShip(ship)
    print(f"\nThe ship contains {count} containers!\n")


def Printer_PrintWeightInAllSixSections(ship):
    frontStarboardWeight = Ship_GetNthSectionLoad(ship, 0)
    frontPortsideWeight = Ship_GetNthSectionLoad(ship, 1)
    middleStarboardWeight = Ship_GetNthSectionLoad(ship, 2)
    middlePortsideWeight = Ship_GetNthSectionLoad(ship, 3)
    backStarboardWeight = Ship_GetNthSectionLoad(ship, 4)
    backPortsideWeight = Ship_GetNthSectionLoad(ship, 5)
    print(f"Front portside weight: {frontPortsideWeight}\tFront starboard weight: {frontStarboardWeight}\nMiddle portside weight: {middlePortsideWeight}\tMiddle starboard weight: {middleStarboardWeight}\nBack portside weight: {backPortsideWeight}\tBack starboard weight: {backStarboardWeight}\n")

def Printer_PrintFrontMiddleBackWeight(ship):
    frontWeight = Ship_GetLoadFrontSection(ship)
    middleWeight = Ship_GetLoadMiddleSection(ship)
    backWeight = Ship_GetLoadBackSection(ship)
    print(f"Weight front section: {frontWeight}\nWeight middle section: {middleWeight}\nWeight back section: {backWeight}\n")

def Printer_PrintStaboardPortsideWeight(ship):
    starboardWeight = Ship_GetLoadStarboardSide(ship)
    portsideWeight = Ship_GetLoadPortsideSide(ship)
    print(f"Weight portside: {portsideWeight}\tWeight starboard: {starboardWeight}\n")

def Printer_PrintShipBalanceStatus(ship):
    balanced, percentDifferenceStarboardPortside, maxPercentDifferenceInSections = Ship_isBalanced(ship)
    if balanced == True:
        print(f"The ship is balanced beacause the difference in weight between starboard and portside is: {round(percentDifferenceStarboardPortside, 2)}% and the maximum difference in weight between sections is: {round(maxPercentDifferenceInSections, 2)}%\n")
    else:
        print(f"The ship is not balanced beacause the difference in weight between starboard and portside is: {round(percentDifferenceStarboardPortside, 2)}% and the maximum difference in weight between sections is: {round(maxPercentDifferenceInSections, 2)}%\n")


def Printer_PrintTotalWeightShip(ship):
    totalWeight = Ship_GetTotalShipLoad(ship)
    print(f"The total weight of the loaded containers is: {totalWeight}\n")


# ----------------------
# 7. Container Manager
# ----------------------

def ContainerManager_WriteContainerSetToFile(filename, container_set):
    f = open(filename, "a")
    for container in container_set:
        if len(container) != 2:
            identifier = Container_GetSerialNumber(container)
            length = Container_GetLength(container)
            weight_empty = Container_GetWeight(container)
            cargo = Container_GetCargo(container)
            total_weight = Container_GetTotalWeight(container)
            f.write(f"{identifier}\t{length}\t{weight_empty}\t{cargo}\t{total_weight}\n")   
        else:
            for subcontainer in container:
                identifier = Container_GetSerialNumber(subcontainer)
                length = Container_GetLength(subcontainer)
                weight_empty = Container_GetWeight(subcontainer)
                cargo = Container_GetCargo(subcontainer)
                total_weight = Container_GetTotalWeight(subcontainer)
                f.write(f"{identifier}\t{length}\t{weight_empty}\t{cargo}\t{total_weight}\n")  
    f.close()

def ContainerManager_LoadContainerSetFromFile(filename):
    f = open(filename, "r")
    containerSet = []
    container_list = f.readlines()
    for line in container_list:
        attribute_list = line.strip().split("\t")
        if len(attribute_list) != 0:
            code = attribute_list[0]
            length = int(attribute_list[1])
            weight = int(attribute_list[2])
            cargo = int(attribute_list[3])
            container = Container_New(code, length, weight, cargo)
            containerSet.append(container)
    f.close()
    return containerSet

def ContainerManager_WriteShipLoadToFile(filename, ship):
    f = open(filename, "a")
    containers = Ship_GetContainers(ship)
    ContainerManager_WriteContainerSetToFile(filename, containers)
    f.close()

def ContainerManager_LoadShipLoadFromFile(filename):
    f = open(filename, "r")
    containerSet = ContainerManager_LoadContainerSetFromFile(filename)
    ship = Ship_New(24, 22, 18)
    Ship_loadCargo(ship, containerSet)
    f.close()
    return ship


# ------------------
# X. Main
# ------------------


start = time.time()
testContainerSet = ContainerSet_GenerateRandomContainerSet(6500)
testContainerSet2 = ContainerSet_GenerateRandomContainerSet(15)

testContainer = testContainerSet[0]

ship = Ship_New(24, 22, 18)
operationsFront, operationsMiddle, operationsBack, message = Ship_loadCargo(ship, testContainerSet)

Printer_PrintShipSections(ship)

Printer_PrintNumberOfContainersInFloors(ship)

Printer_PrintWeightInAllSixSections(ship)
Printer_PrintFrontMiddleBackWeight(ship)
Printer_PrintStaboardPortsideWeight(ship)
Printer_PrintShipBalanceStatus(ship)
Printer_PrintTotalWeightShip(ship)

print(Ship_FindContainerInShip(ship, testContainerSet[0]))
print(Ship_FindContainerInShip(ship, testContainerSet[1]))
print(Ship_FindContainerInShip(ship, testContainerSet[-1]))



Printer_PrintNumberOfContainersInShip(ship)
Printer_PrintSectionWithWeightOfStacks(ship)

print(f"Total number of operations to load the ship (one crane): {operationsFront + operationsMiddle + operationsBack}")
print(f"Total number of operations to load the ship (one crane): front: {operationsFront} middle: {operationsMiddle} back: {operationsBack}")

print(message)

end = time.time()
print()
print(f"{end - start} seconds")
print()

start2 = time.time()
popped, ship, operationsFront, operationsMiddle, operationsBack = Ship_UnloadShip(ship)
print(f"Total number of operations to unload the ship: {operationsFront + operationsMiddle + operationsBack}")
print(f"Total number of operations to unload the ship: front: {operationsFront} middle: {operationsMiddle} back: {operationsBack}")

end2 = time.time()
print()
print(f"{end2 - start2} seconds")
print()


# ---------------------
# Testing
# ---------------------

# Uncomment the different tests in order to use them

# Tests that it is possible to load the ship with several container sets as long as it is not full.
# testContainerSet = ContainerSet_GenerateRandomContainerSet(2300)
# testContainerSet2 = ContainerSet_GenerateRandomContainerSet(1500)
#Ship_loadCargo(ship, testContainerSet)
# Ship_loadCargo(ship, testContainerSet2)
# Printer_PrintShipSections(ship)

#Tests that you can save and load a container set from a file
# testContainerSet = ContainerSet_GenerateRandomContainerSet(2300)
#ContainerManager_WriteContainerSetToFile("testContainerSet.tsv", testContainerSet
#Cset = ContainerManager_LoadContainerSetFromFile("testContainerSet.tsv")
#print(Cset)

#Tests that you can write the load from a ship to a file
# testContainerSet = ContainerSet_GenerateRandomContainerSet(2300)
# ship = Ship_New(24, 22, 18)
# Ship_loadCargo(ship, testContainerSet)
# ContainerManager_WriteShipLoadToFile("test3.tsv", ship)


#Tests that you can load the ship load from a chosen file
# ship2 = ContainerManager_LoadShipLoadFromFile("test2.tsv")
# Printer_PrintShipSections(ship)
# Printer_PrintWeightInAllSixSections(ship2)
# Printer_PrintFrontMiddleBackWeight(ship2)
# Printer_PrintStaboardPortsideWeight(ship2)
# Printer_PrintShipBalanceStatus(ship2)
# Printer_PrintTotalWeightShip(ship2)


#Tests that you can remove a given container from a ship
#testContainerSet = ContainerSet_GenerateRandomContainerSet(200)
#ship = Ship_New(24, 22, 18)
#Ship_loadCargo(ship, testContainerSet)
#print(Ship_RemoveContainerFromShip(ship, testContainerSet[-3]))
#Printer_PrintShipSections(ship)


#Tests the unload-function
#testContainerSet = ContainerSet_GenerateRandomContainerSet(200)
#ship = Ship_New(24, 22, 18)
#Ship_loadCargo(ship, testContainerSet)
#Printer_PrintShipSections(ship)
#print(Ship_isEmpty(ship))
#print(f"\n"*4)
#popped, ship = Ship_UnloadShip(ship)
#print(popped)
#print(f"\n"*4)
#Printer_PrintShip(ship)
#print(Ship_isEmpty(ship))


#Tests the time it takes to unload a ship using one crane
# ship = Ship_New(24, 22, 18)
# testContainerSet = ContainerSet_GenerateRandomContainerSet(6500)
# Ship_loadCargo(ship, testContainerSet)
# print(f"It would take about {Ship_CalculateTimeToUnloadShipOneCrane(ship)} days to unload the ship using one crane.")

#Tests the time it takes to unload a ship using one crane with assumption
# ship = Ship_New(24, 22, 18)
# testContainerSet = ContainerSet_GenerateRandomContainerSet(6500)
# Ship_loadCargo(ship, testContainerSet)
# print(f"It would take about {Ship_CalculateTimeToUnloadShipOneCraneWithAssumption(ship)} days to unload the ship using one crane.")

#Tests the time it takes to unload a ship with three cranes
# ship = Ship_New(24, 22, 18)
# testContainerSet = ContainerSet_GenerateRandomContainerSet(6500)
# Ship_loadCargo(ship, testContainerSet)
# print(f"It would take about {Ship_CalculateTimeToUnloadShipThreeCranes(ship)} days to unload the ship using one crane.")

#Tests loading time. First with the assumption that every operation takes 4 minutes. Then with the assumption that it takes 4 minutes from a container is picked until it is loaded and its stack is sorted.
# ship = Ship_New(24, 22, 18)
# testContainerSet = ContainerSet_GenerateRandomContainerSet(6500)
# print(f"It would take about {Ship_CalculateTimeToLoadShipOneCrane(ship, testContainerSet)} days to fully load the ship using one crane.")
# print(f"Assuming that it takes 4 minutes from a container is picked until its loaded, including the sorting of stacks, it would take about {Ship_CalculateTimeToLoadShipOneCraneWithAssumption(ship)} days to load the ship.")

#Tests that the stacks are sorted according to weight
# emptyContainerSet = ContainerSet_GenerateRandomEmptyContainerSet(1500)
# fullContainerSet = ContainerSet_GenerateRandomFullContainerSet(1500)
# ship = Ship_New(24, 22, 18)
# Ship_loadCargo(ship, emptyContainerSet)
# Printer_PrintShipSections(ship)
# Ship_loadCargo(ship, fullContainerSet)
# Printer_PrintShipSections(ship)


#Tests that all the containers in the containerset are loaded as long as the ship is not full.
# testContainerSet = ContainerSet_GenerateRandomContainerSet(500)
# ship = Ship_New(24, 22, 18)
# Ship_loadCargo(ship, testContainerSet)
# print(Ship_FindContainerInShip(ship, testContainerSet[0]))
# print(Ship_FindContainerInShip(ship, testContainerSet[-1]))
# print(Ship_FindContainerInShip(ship, testContainerSet[-2]))
# print(Ship_FindContainerInShip(ship, testContainerSet[-3]))

#Tests that all the containers in the containerset are not loaded if the ship is full.
# testContainerSet = ContainerSet_GenerateRandomContainerSet(6500)
# ship = Ship_New(24, 22, 18)
# Ship_loadCargo(ship, testContainerSet)
# print(Ship_FindContainerInShip(ship, testContainerSet[0]))
# print(Ship_FindContainerInShip(ship, testContainerSet[-1]))
# print(Ship_FindContainerInShip(ship, testContainerSet[-2]))
# print(Ship_FindContainerInShip(ship, testContainerSet[-3]))


#Checks if a 20-container will not be loaded. If the two numbers are the same it will be. 
# testContainerSet = ContainerSet_GenerateRandomContainerSet(500)
# print(ContainerSet_CountPairOf20s(testContainerSet))
# print(ContainerSet_CountPairOf20sInFixed(ContainerSet_PairSmallContainers(testContainerSet)))

#Tests the time it takes to load and unload the ship with one cranes
# ship = Ship_New(24, 22, 18)
# testContainerSet = ContainerSet_GenerateRandomContainerSet(6500)
# print(f"The time it takes to fully load the ship using three cranes is about: {Ship_CalculateTimeToLoadShipOneCrane(ship, testContainerSet)} days.")
# print(f"The time it takes to unload the ship using three cranes is about: {Ship_CalculateTimeToUnloadShipOneCrane(ship)} days.")


#Tests the time it takes to load and unload the ship with three cranes
# ship = Ship_New(24, 22, 18)
# testContainerSet = ContainerSet_GenerateRandomContainerSet(6500)
# print(f"The time it takes to fully load the ship using three cranes is about: {Ship_CalculateTimeToLoadShipThreeCranes(ship, testContainerSet)} days.")
# print(f"The time it takes to unload the ship using three cranes is about: {Ship_CalculateTimeToUnloadShipThreeCranes(ship)} days.")