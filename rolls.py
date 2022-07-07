# This is a sample Python script.
import importlib

import tesouro, dice

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def RollLoot(nd):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Rolagem para ND: {nd}')  # Press Ctrl+F8 to toggle the breakpoint.
    rollDadoD = dice.roll('1d100')
    rollDadoL = dice.roll('1d100')
    #print(f'rollD: {rollDadoD[0]}')
    #print(f'rollL: {rollDadoL[0]}')
    #print(dice.roll('1d1'))
    rollTesouro = tesouro.Search(nd, rollDadoL[0])
    rollDinheiro = tesouro.Search(nd, rollDadoD[0])

    Tesouro = rollTesouro.dinheiro.replace("'","")
    Dinheiros = rollDinheiro.dinheiro.replace("'","")
    if Dinheiros == "-":
        Dinheiros = "Nada!"
    else:
        #print(Dinheiros)
        Lista = Dinheiros.split(" ")
        #print(Lista)

        dadoDinheiro = dice.roll(Lista[0].__str__().replace("x","*"))
        #print(dadoDinheiro)
        Dinheiros = f'{dadoDinheiro}{Lista[1]}'
        Dinheiros = Dinheiros.replace("s","$")
    Items = rollTesouro.item.replace("'","")
    if Items == "-":
        Items = "Nada!"
    loot = f' Você recebeu de dinheiro: {Dinheiros} e de items: {Items}'
    print(f' Você recebeu de dinheiro: {Dinheiros} e de items: {Items}')
    return loot


def DiceRoll(Dado):

    VanDis = ""
    print(Dado," DADO")
    DadoC = Dado.lower()
    DadoC = DadoC.split(" ")

    try:

        if DadoC[1] == "adv":
            print("Com Vantagem")
            VanDis = "adv"
            DadoL = DadoC[0]
            print(VanDis,"VanDis")
        elif DadoC[1] == "dis":
            print("Com Desvantagem")
            VanDis = "dis"
            DadoL = DadoC[0]
            print(VanDis,"VanDis")
        else:
            VanDis = ""
            DadoL = Dado
    except:
        print("Sem Vantagem ou Desvantagem!")
        VanDis = ""
        DadoL = Dado
        pass

    DadoS = DadoL.split("d")
    print(DadoS," DADOS")
    seMod = f'{DadoS[1]}'
    Mod = ""
    Tdado = DadoS[1]
    TMod = ""

    print(Dado, "DADO")

    if seMod.find("+") != -1 :
        seMod = seMod.split("+")
        print("+")
        print(seMod)
        Tdado = seMod[0]
        Mod = seMod[1]
        TMod = "+"
        #print(DadoS, Tdado, Mod, " ISSO")
    elif seMod.find("-") != -1 :
        seMod = seMod.split("-")
        Tdado = seMod[0]
        Mod = seMod[1]
        TMod = "-"
    elif seMod.find("*"or"x") != -1 :
        seMod = seMod.split("*")
        Tdado = seMod[0]
        Mod = seMod[1]
        TMod = "*"
    elif seMod.find("/") != -1 :
        seMod = seMod.split("/")
        Tdado = seMod[0]
        Mod = seMod[1]
        TMod = "/"
    else:
        Tdado = DadoS[1]
        print(Tdado," Tdado")
    #print(DadoS,Tdado,Mod," ISSO")

    if isinstance(seMod, int) :
        print("DadoS é INT!!")
    else:
        FDados = f'{DadoS[0]}d{Tdado}'
        maxDice = dice.roll_max(FDados)
    #    maxDice = maxDice[0].__str__()
        minDice = dice.roll_min(FDados)
    #    minDice = minDice[0].__str__()
    #    print(f'{maxDice},{minDice}')
        rolls = dice.roll(FDados)
    #    print(minDice,maxDice,rolls)
        rolls.sort()
        c = 0
        rollsF = []
        Soma = 0
        for i in rolls:
    #        print(f'I={i}')
            if (i == maxDice[0] or i == minDice[0]):

                rollsF.append(f'**{i}**')
                #print(rollsF)
            else:
                rollsF.append(f'{i}')
            c = c + 1
            Soma = Soma + i
        if TMod == "+":
            FSoma = Soma + int(Mod)
        elif TMod == "-":
            FSoma = Soma - int(Mod)
        elif TMod == "*":
            FSoma = Soma * int(Mod)
        elif TMod == "/":
            FSoma = Soma / int(Mod)
        else:
            FSoma = Soma
        if VanDis != "":
            if VanDis == "adv":
                for i in rollsF:
                    FSoma = i
                    print(FSoma," Atual FSoma")
            if VanDis == "dis":
                FSoma = rollsF[0]
                print(FSoma," FSoma")

        lenRolls = rollsF.__len__()
        print(lenRolls," lenRolls")
        rollsF = rollsF.__str__().replace("'","")
        FSoma = int(FSoma)
        PCrit = 0
        NCrit = 0

        if lenRolls >> 1:
            print("Rolagem de multiplos dados")
            for i in dice.roll_max(FDados):
                PCrit = PCrit + i
            for i in dice.roll_min(FDados):
                NCrit = NCrit + i
            print(PCrit,NCrit,"P N")
            if FSoma >= PCrit:
                RollRusult = f' ```ini\n[{FSoma}]``` Rolagem: {rollsF}=**{Soma}**{TMod}{Mod} | ***{Dado}***'
                print(RollRusult)
            elif FSoma <= NCrit:
                RollRusult = f' ```css\n[{FSoma}]``` Rolagem: {rollsF}=**{Soma}**{TMod}{Mod} | ***{Dado}***'
                print(RollRusult)
            else:
                RollRusult = f' ```fix\n[{FSoma}]``` Rolagem: {rollsF}=**{Soma}**{TMod}{Mod} | ***{Dado}***'
                print(RollRusult)
        else:
            print("Rolagem de Dado Unico")
            PCrit = dice.roll_max(FDados)
            NCrit = dice.roll_min(FDados)
            PCrit = str(PCrit).replace("[","")
            PCrit = str(PCrit).replace("]", "")
            NCrit = str(NCrit).replace("[", "")
            NCrit = str(NCrit).replace("]", "")
            PCrit = f'[**{PCrit}**]'
            NCrit = f'[**{NCrit}**]'
            print(PCrit, NCrit, "P N")
            print(rollsF, " rollsF ",rollsF)
            #rollsF = rollsF.replace("[","")
            #rollsF = rollsF.replace("]","")
            #rollsF = int(rollsF)

            try:
                if rollsF == PCrit:
                    RollRusult = f' ```ini\n[{FSoma}]``` Rolagem: {rollsF}=**{Soma}**{TMod}{Mod} | ***{Dado}***'
                    print(RollRusult)
                elif rollsF == NCrit:
                    RollRusult = f' ```css\n[{FSoma}]``` Rolagem: {rollsF}=**{Soma}**{TMod}{Mod} | ***{Dado}***'
                    print(RollRusult)
                else:
                    RollRusult = f' ```fix\n[{FSoma}]``` Rolagem: {rollsF}=**{Soma}**{TMod}{Mod} | ***{Dado}***'
                    print(RollRusult)
            except:
                print(" Deu Cocô :/")
        #rolls = rolls.replace(maxDice, f'**{maxDice}**')
        #rolls = rolls.replace(minDice, f'**{minDice}**')
        #print(f'Rolei {rollsF}')
        print("RR: ",RollRusult)
    return  RollRusult

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    RollLoot('3')

    #DiceRoll("5d10")
    print(DiceRoll("5d10/2"))
    #print(dice.roll("3d20"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
