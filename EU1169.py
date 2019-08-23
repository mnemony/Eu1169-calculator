
def energycalc():
    while True:
        print("Welcome in food energy converter")
        product = input("Please, type your product. Press 'q' to exit program: ")
        if product == 'q':
            print('see you next time')
            break
        else:
            try:
                print("All values have to be numbers, if decimal separate them with dot")
                carbs = float(input("Type total grams of carbs per 100 g: "))
                protein = float(input("Type total grams of protein per 100 g: "))
                fat = float(input("Type total grams of fat per 100 g: "))
                fibre = float(input("Type total grams of fibre per 100 g: "))

                total = carbs + protein + fat + fibre

                if total >= 100:
                    print('Sum of values must be less than 100')
                    break
                else:

                    #converting macroelements into energy values                     
                    carbsKcal = carbs * 4
                    carbsKj = carbs * 17
                    proteinKcal = protein * 4 
                    proteinKj = protein * 17
                    fatKcal = fat * 9
                    fatKj = fat * 37
                    fibreKcal = fibre * 2
                    fibreKj = fibre *8

                    #total energy values
                    totalKj = carbsKj + proteinKj + fatKj + fibreKj
                    totalKcal = carbsKcal + proteinKcal + fatKcal + fibreKcal

                    # DAILY REFERENCE IN %
                    percentTotal = (totalKcal/2000) * 100
                    percentcarb = (carbs/260) * 100
                    percentfat = (fat/70) * 70
                    percentprotein = (protein/50) * 100

                
                    print("\n\nYour prouduct " + product + " have " + str(totalKj) + " kj and " + str(totalKcal) + " kcal per 100 g"
                    "\nDaily reference intakes for energy in 100 g of product is " + str(percentTotal) + " %.\n"
                    "\nMacro elements:"
                    "\n- from carbs " + str(percentcarb) + " % DRI " +  str(carbsKj) + " kj and " + str(carbsKcal) + " kcal per 100 g"
                    "\n- from protein " + str(percentprotein) + " % DRI " +  str(proteinKj) + " kj and " + str(proteinKcal) + " kcal per 100 g"
                    "\n- from fat " + str(percentfat) + " % DRI " +  str(fatKj) + " kj and " + str(fatKcal) + " kcal per 100 g")


                    # nutrition and health claims made on foods
                    if proteinKcal >= (0.12 * totalKcal):
                        print(product + " is source of protein")
                    if proteinKcal >= (0.2 * totalKcal):
                        print(product + " is source of protein")    
                    if fibre >= 3:
                        print(product + " is source of fibre")
                    if fibre >= 6:
                        print(product + " is high fibre product")
                    if totalKcal <= 40:
                        print(product + " is low energy product") 
                    if fat <= 3:
                        print(product + " is low fat product")   
                    print("--------------------------")
                    print("--------------------------")
                    print("--------------------------\n")
                          

            except ValueError:
                print('\nwrong data - only numbers allowed, for example: 12 or 5.7 ')
                        
energycalc()