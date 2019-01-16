#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 23:17:30 2019

@author: jonah
"""
import random
import copy
def create_rubix_dict():
    rule_dict = dict()
    
    for a in range(0, 54):
        for b in range(0, 54):
            rule_dict[(a,b)] = set()
            
    for a in range(0, 54):
        for b in range(0, 54):
            for c in range(0, 54):
                for d in range(0, 54):
                    
                    if int(a/9) == int(c/9):
                        if int(b/9) == int(d/9):
                            rule_dict[(a,c)].add((b,d))
                        
                    if int(a/9) != int(c/9):
                        if int(b/9) != int(d/9):
                            rule_dict[(a,c)].add((b,d))
    return rule_dict

def move_cube(cube, move):
    if move == 0:
        old_pos = []
        for x in range(0, 12):
            old_pos.append(cube[x*3])
        for x in range(0, 12):
            cube[x*3] = old_pos[(x - 3) % 12]
        
        old_pos = []
        for x in range(36, 45):
            old_pos.append(cube[x])
        cube[36] = old_pos[2]
        cube[37] = old_pos[5]
        cube[38] = old_pos[8]
        cube[39] = old_pos[1]
        cube[40] = old_pos[4]
        cube[41] = old_pos[7]
        cube[42] = old_pos[0]
        cube[43] = old_pos[3]
        cube[44] = old_pos[6]
    
    elif move == 1:
        old_pos = []
        for x in range(0, 12):
            old_pos.append(cube[(3*x) + 1])
        
        for x in range(0, 12):
            cube[(3*x) + 1] = old_pos[(x-3) % 12]
            
    elif move == 2:
        old_pos = []
        for x in range(0, 12):
            old_pos.append(cube[(3*x) + 2])
        
        for x in range(0, 12):
            cube[(3*x) + 2] = old_pos[(x-3) % 12]
            
        old_pos = []
        for x in range(45, 54):
            old_pos.append(cube[x])
        cube[45] = old_pos[6]
        cube[46] = old_pos[3]
        cube[47] = old_pos[0]
        cube[48] = old_pos[7]
        cube[49] = old_pos[4]
        cube[50] = old_pos[1]
        cube[51] = old_pos[8]
        cube[52] = old_pos[5]
        cube[53] = old_pos[2]
        
    elif move == 3:
        old_pos = []
        for x in range(0, 12):
            old_pos.append(cube[x*3])
        for x in range(0, 12):
            cube[x*3] = old_pos[(x + 3) % 12]
        
        old_pos = []
        for x in range(36, 45):
            old_pos.append(cube[x])
        cube[36] = old_pos[6]
        cube[37] = old_pos[3]
        cube[38] = old_pos[0]
        cube[39] = old_pos[7]
        cube[40] = old_pos[4]
        cube[41] = old_pos[1]
        cube[42] = old_pos[8]
        cube[43] = old_pos[5]
        cube[44] = old_pos[2]
    
    elif move == 4:
        old_pos = []
        for x in range(0, 12):
            old_pos.append(cube[(3*x) + 1])
        
        for x in range(0, 12):
            cube[(3*x) + 1] = old_pos[(x+3) % 12]
            
    elif move == 5:
        old_pos = []
        for x in range(0, 12):
            old_pos.append(cube[(3*x) + 2])
        
        for x in range(0, 12):
            cube[(3*x) + 2] = old_pos[(x+3) % 12]
            
        old_pos = []
        for x in range(45, 54):
            old_pos.append(cube[x])
        cube[45] = old_pos[2]
        cube[46] = old_pos[5]
        cube[47] = old_pos[8]
        cube[48] = old_pos[1]
        cube[49] = old_pos[4]
        cube[50] = old_pos[7]
        cube[51] = old_pos[0]
        cube[52] = old_pos[3]
        cube[53] = old_pos[6]
        
    elif move == 6:
        old_pos = []
        changed_list = [0, 1, 2, 45, 46, 47, 26, 25, 24, 36, 37, 38]
        for item in changed_list:
            old_pos.append(cube[item])
        
        counter = 0
        for item in changed_list:
            cube[item] = old_pos[(counter-3) % 12]
            counter += 1
            
        old_pos = []
        
        for x in range(9, 18):
            old_pos.append(cube[x])
        cube[9] = old_pos[2]
        cube[10] = old_pos[5]
        cube[11] = old_pos[8]
        cube[12] = old_pos[1]
        cube[13] = old_pos[4]
        cube[14] = old_pos[7]
        cube[15] = old_pos[0]
        cube[16] = old_pos[3]
        cube[17] = old_pos[6]
    
    elif move == 7:
        old_pos = []
        changed_list = [3, 4, 5, 48, 49, 50, 23, 22, 21, 39, 40, 41]
        for item in changed_list:
            old_pos.append(cube[item])
        
        counter = 0
        for item in changed_list:
            cube[item] = old_pos[(counter-3) % 12]
            counter += 1
         
    elif move == 8:
        old_pos = []
        changed_list = [6, 7, 8, 51, 52, 53, 20, 19, 18, 42, 43, 44]
        for item in changed_list:
            old_pos.append(cube[item])
        
        counter = 0
        for item in changed_list:
            cube[item] = old_pos[(counter-3) % 12]
            counter += 1
            
        old_pos = []        
        for x in range(27, 36):
            old_pos.append(cube[x])
        cube[27] = old_pos[6]
        cube[28] = old_pos[3]
        cube[29] = old_pos[0]
        cube[30] = old_pos[7]
        cube[31] = old_pos[4]
        cube[32] = old_pos[1]
        cube[33] = old_pos[8]
        cube[34] = old_pos[5]
        cube[35] = old_pos[2]
        
    elif move == 9:
        old_pos = []
        changed_list = [0, 1, 2, 45, 46, 47, 26, 25, 24, 36, 37, 38]
        for item in changed_list:
            old_pos.append(cube[item])
        
        counter = 0
        for item in changed_list:
            cube[item] = old_pos[(counter+3) % 12]
            counter += 1
            
        old_pos = []
        
        for x in range(9, 18):
            old_pos.append(cube[x])
        cube[9] = old_pos[6]
        cube[10] = old_pos[3]
        cube[11] = old_pos[0]
        cube[12] = old_pos[7]
        cube[13] = old_pos[4]
        cube[14] = old_pos[1]
        cube[15] = old_pos[8]
        cube[16] = old_pos[5]
        cube[17] = old_pos[2]
    
    elif move == 10:
        old_pos = []
        changed_list = [3, 4, 5, 48, 49, 50, 23, 22, 21, 39, 40, 41]
        for item in changed_list:
            old_pos.append(cube[item])
        
        counter = 0
        for item in changed_list:
            cube[item] = old_pos[(counter+3) % 12]
            counter += 1
         
    elif move == 11:
        old_pos = []
        changed_list = [6, 7, 8, 51, 52, 53, 20, 19, 18, 42, 43, 44]
        for item in changed_list:
            old_pos.append(cube[item])
        
        counter = 0
        for item in changed_list:
            cube[item] = old_pos[(counter+3) % 12]
            counter += 1
            
        old_pos = []        
        for x in range(27, 36):
            old_pos.append(cube[x])
        cube[27] = old_pos[2]
        cube[28] = old_pos[5]
        cube[29] = old_pos[8]
        cube[30] = old_pos[1]
        cube[31] = old_pos[4]
        cube[32] = old_pos[7]
        cube[33] = old_pos[0]
        cube[34] = old_pos[3]
        cube[35] = old_pos[6]
    
    elif move == 12:
        old_pos = []
        changed_list = [27, 28, 29, 51, 48, 45, 17, 16, 15, 38, 41, 44]
        for item in changed_list:
            old_pos.append(cube[item])
        
        counter = 0
        for item in changed_list:
            cube[item] = old_pos[(counter-3) % 12]
            counter += 1
            
        old_pos = []
        
        for x in range(0, 9):
            old_pos.append(cube[x])
        cube[0] = old_pos[2]
        cube[1] = old_pos[5]
        cube[2] = old_pos[8]
        cube[3] = old_pos[1]
        cube[4] = old_pos[4]
        cube[5] = old_pos[7]
        cube[6] = old_pos[0]
        cube[7] = old_pos[3]
        cube[8] = old_pos[6]
    
    elif move == 13:
        old_pos = []
        changed_list = [30, 31, 32, 52, 49, 46, 14, 13, 12, 37, 40, 43]
        for item in changed_list:
            old_pos.append(cube[item])
        
        counter = 0
        for item in changed_list:
            cube[item] = old_pos[(counter-3) % 12]
            counter += 1
    
    elif move == 14:
        old_pos = []
        changed_list = [33, 34, 35, 53, 50, 47, 11, 10, 9, 36, 39, 42]
        for item in changed_list:
            old_pos.append(cube[item])
        
        counter = 0
        for item in changed_list:
            cube[item] = old_pos[(counter-3) % 12]
            counter += 1
            
        old_pos = []
        
        for x in range(18, 27):
            old_pos.append(cube[x])
        cube[18] = old_pos[6]
        cube[19] = old_pos[3]
        cube[20] = old_pos[0]
        cube[21] = old_pos[7]
        cube[22] = old_pos[4]
        cube[23] = old_pos[1]
        cube[24] = old_pos[8]
        cube[25] = old_pos[5]
        cube[26] = old_pos[2]
        
    elif move == 15:
        old_pos = []
        changed_list = [27, 28, 29, 51, 48, 45, 17, 16, 15, 38, 41, 44]
        for item in changed_list:
            old_pos.append(cube[item])
        
        counter = 0
        for item in changed_list:
            cube[item] = old_pos[(counter+3) % 12]
            counter += 1
            
        old_pos = []
        
        for x in range(0, 9):
            old_pos.append(cube[x])
        cube[0] = old_pos[6]
        cube[1] = old_pos[3]
        cube[2] = old_pos[0]
        cube[3] = old_pos[7]
        cube[4] = old_pos[4]
        cube[5] = old_pos[1]
        cube[6] = old_pos[8]
        cube[7] = old_pos[5]
        cube[8] = old_pos[2]
    
    elif move == 16:
        old_pos = []
        changed_list = [30, 31, 32, 52, 49, 46, 14, 13, 12, 37, 40, 43]
        for item in changed_list:
            old_pos.append(cube[item])
        
        counter = 0
        for item in changed_list:
            cube[item] = old_pos[(counter+3) % 12]
            counter += 1
    
    elif move == 17:
        old_pos = []
        changed_list = [33, 34, 35, 53, 50, 47, 11, 10, 9, 36, 39, 42]
        for item in changed_list:
            old_pos.append(cube[item])
        
        counter = 0
        for item in changed_list:
            cube[item] = old_pos[(counter+3) % 12]
            counter += 1
            
        old_pos = []
        
        for x in range(18, 27):
            old_pos.append(cube[x])
        cube[18] = old_pos[2]
        cube[19] = old_pos[5]
        cube[20] = old_pos[8]
        cube[21] = old_pos[1]
        cube[22] = old_pos[4]
        cube[23] = old_pos[7]
        cube[24] = old_pos[0]
        cube[25] = old_pos[3]
        cube[26] = old_pos[6]
        
    return cube

if __name__ == "__main__":
    rules = create_rubix_dict()
    cb = []
    for x in range(0, 54):
        cb.append(x)
    
    
    
    for x in range(0, 250):
        mv = random.randint(0, 17)
        cb = move_cube(cb, mv)
    
    lst = []
    for x in range(0,54):
        lst.append([0])
        for y in range(0, 53):
            lst[x].append(0)
    while True:
        satisfied = 0
        for x in range(0, 54):
            for y in range(0, 54):
                if (cb[x], cb[y]) in rules[(x, y)]:
                    satisfied += 1
                    lst[x][y] = 1
                else:
                    lst[x][y] = 0
        print(satisfied)

        
        new_sat = 0
        best_move = [0]
        rd = random.random()
        
        if rd < 0.45:
            moves_list = []
            for move in range(0, 18):                
                cbn = copy.deepcopy(cb)
                cbn = move_cube(cbn, move)
                for move_2 in range(0, 18):
                    if (int(move/6) == int(move_2/6)) and ((move == move_2 + 3) or (move == move_2 - 3)):
                        continue
                    else:
                        cbn_2 = copy.deepcopy(cbn)
                        cbn_2 = move_cube(cbn_2, move_2)
                        for move_3 in range(0, 18):
                            if (int(move_2/6) == int(move_3/6)) and ((move_2 == move_3 + 3) or (move_2 == move_3 - 3)):
                                continue
                            else:
                                new_sat_move = 0
                                cbn_3 = copy.deepcopy(cbn_2)
                                cbn_3 = move_cube(cbn_3, move_3)
                                for x in range(0, 54):
                                    for y in range(0, 54):
                                        if (cbn_3[x], cbn_3[y]) in rules[(x, y)]:
                                            new_sat_move += 1
                                moves = [move, move_2, move_3]
                                moves.sort()
                                if not (moves == [0,1,2]) and not (moves == [3, 4, 5]) and not (moves == [6, 7, 8]) and not (moves == [9, 10, 11]) and not (moves == [12, 13, 14]) and not (moves == [15, 16, 17]):                            
                                    moves_list.append((new_sat_move, move, move_2, move_3))
                                    
            moves_list.sort(reverse = True)            
            rand = random.randint(0, 9)               
            best_move = [moves_list[rand][1], moves_list[rand][2], moves_list[rand][3]]
            
        elif rd < 9:
            moves_list = []
            for move in range(0, 18):                
                cbn = copy.deepcopy(cb)
                cbn = move_cube(cbn, move)
                for move_2 in range(0, 18):   
                    if (int(move/6) == int(move_2/6)) and ((move == move_2 + 3) or (move == move_2 - 3)):
                        continue
                    else:
                        cbn_2 = copy.deepcopy(cbn)
                        cbn_2 = move_cube(cbn_2, move_2)
                        for move_3 in range(0, 18):
                            if (int(move_2/6) == int(move_3/6)) and ((move_2 == move_3 + 3) or (move_2 == move_3 - 3)):
                                continue
                            else:
                                new_sat_move = 0
                                cbn_3 = copy.deepcopy(cbn_2)
                                cbn_3 = move_cube(cbn_3, move_3)
                                for x in range(0, 54):
                                    for y in range(0, 54):
                                        if (cbn_3[x], cbn_3[y]) in rules[(x, y)]:
                                            if lst[x][y] == 0:
                                                new_sat_move += 1
                                moves = [move, move_2, move_3]
                                moves.sort()
                                if not (moves == [0,1,2]) and not (moves == [3, 4, 5]) and not (moves == [6, 7, 8]) and not (moves == [9, 10, 11]) and not (moves == [12, 13, 14]) and not (moves == [15, 16, 17]):                            
                                    moves_list.append((new_sat_move, move, move_2, move_3))
                                    
            moves_list.sort(reverse = True)
            rand = random.randint(0, 9)               
            best_move = [moves_list[rand][1], moves_list[rand][2], moves_list[rand][3]]
            
        else:
            best_move = [random.randint(0, 17), random.randint(0, 17)]
        print(rd, best_move)
        for mv in best_move:
            cb = move_cube(cb, mv)
        