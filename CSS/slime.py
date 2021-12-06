def slimestat() :
    slimehp = stage*5
    slimeap = stage
    slimedp = int(stage/2)
    slimetp = turn
    slimest = ""

def slimebattle() :
    if tp % 3 == 0 :
        sleep(1)
        print()
        print("슬라임은 자연회복을 사용했다!")
        slimest = "자연회복"
    else :
        sleep(1)
        print()
        print("슬라임은 공격을 했다!")
        charhp 
