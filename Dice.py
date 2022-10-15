import random
random_numb = random.randrange(1,6)
dice_one = ['- - - - -','|       |','|   *   |','|       |','- - - - -']
dice_two = ['- - - - -','|     * |','|       |','| *     |','- - - - -']
dice_three = ['- - - - -','|     * |','|   *   |','| *     |','- - - - -']
dice_four = ['- - - - -','| *   * |','|       |','| *   * |','- - - - -']
dice_five = ['- - - - -','| *   * |','|   *   |','| *   * |','- - - - -']
dice_six = ['- - - - -','| *   * |','| *   * |','| *   * |','- - - - -']
def dice_drawer(random_numb):  
    print('Dice: ' + str(random_numb)) 
    for i in range(0,5):
        match random_numb:
            case 1:
                print(dice_one[i])
            case 2:
                print(dice_two[i])
            case 3:
                print(dice_three[i])
            case 4:
                print(dice_four[i])
            case 5:
                print(dice_five[i])
            case 6:
                print(dice_six[i])

dice_drawer(random_numb)
