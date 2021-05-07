from agent.base_agent import BaseAgent
import pygame

class MyAgent(BaseAgent):
    
    def WhereCanMove(self, obs, color):
        
        CanPutOrNot = []  #用串列儲存，提升效率
        if color == 'black':  #黑子
            #判斷哪個位置可以下
            for i in range(64):
                if obs[i] == -1 or obs[i] == 0:  #忽略黑子與空白格
                    continue
            
                else:  #發現白子後，去判斷其周遭八格可不可放子
                    for j in (-9, -8, -7, -1, 1, 7, 8, 9):
                        position = i + j
                    
                        if position in CanPutOrNot:  #忽略已判斷可放的
                            continue
                    
                        elif position < 0 or position > 63:  #忽略超出邊界者
                            continue
                    
                        elif obs[position] == -1 or obs[position] == 1:  #忽略已有放子者
                            continue
                    
                        elif j == -9:  #左上那格，往右下找
                            position = i + 9
                            while position < 64 and position % 8 != 0 and (i + j) % 8 != 7:
                                if obs[position] == -1:
                                    CanPutOrNot.append(i + j)
                                    break
                                elif obs[position] == 0:
                                    break
                                position += 9
                            
                        elif j == -8:  #上面那格，往下找
                            position = i + 8
                            while position < 64:
                                if obs[position] == -1:
                                    CanPutOrNot.append(i + j)
                                    break
                                elif obs[position] == 0:
                                    break
                                position += 8
                            
                        elif j == -7:  #右上那格，往左下找
                            position = i + 7
                            while position < 64 and position % 8 != 7 and (i + j) % 8 != 0:
                                if obs[position] == -1:
                                    CanPutOrNot.append(i + j)
                                    break
                                elif obs[position] == 0:
                                    break
                                position += 7
                            
                        elif j == -1:  #左邊那格，往右找
                            position = i + 1
                            while position < 64 and position % 8 != 0 and (i + j) % 8 != 7:
                                if obs[position] == -1:
                                    CanPutOrNot.append(i + j)
                                    break
                                elif obs[position] == 0:
                                    break
                                position += 1
                            
                        elif j == 1:  #右邊那格，往左找
                            position = i - 1
                            while position >= 0 and position % 8 != 7 and (i + j) % 8 != 0:
                                if obs[position] == -1:
                                    CanPutOrNot.append(i + j)
                                    break
                                elif obs[position] == 0:
                                    break
                                position -= 1
                        
                        elif j == 7:  #左下那格，往右上找
                            position = i - 7
                            while position >= 0 and position % 8 != 0 and (i + j) % 8 != 7:
                                if obs[position] == -1:
                                    CanPutOrNot.append(i + j)
                                    break
                                elif obs[position] == 0:
                                    break
                                position -= 7
                        
                        elif j == 8:  #下面那格，往上面找
                            position = i - 8
                            while position >= 0:
                                if obs[position] == -1:
                                    CanPutOrNot.append(i + j)
                                    break
                                elif obs[position] == 0:
                                    break
                                position -= 8
                        
                        elif j == 9:  #右下那格，往左上找
                            position = i - 9
                            while position >= 0 and position % 8 != 7 and (i + j) % 8 != 0:
                                if obs[position] == -1:
                                    CanPutOrNot.append(i + j)
                                    break
                                elif obs[position] == 0:
                                    break
                                position -= 9
                             
        else:  #白子
        #判斷哪個位置可以下
            for i in range(64):
                if obs[i] == 1 or obs[i] == 0:  #忽略白子與空白格
                    continue
            
                else:  #發現黑子後，去判斷其周遭八格可不可放子
                    for j in (-9, -8, -7, -1, 1, 7, 8, 9):
                        position = i + j
                    
                        if position in CanPutOrNot:  #忽略已判斷可放的
                            continue
                    
                        elif position < 0 or position > 63:  #忽略超出邊界者
                            continue
                    
                        elif obs[position] == -1 or obs[position] == 1:  #忽略已有放子者
                            continue
                    
                        elif j == -9:  #左上那格，往右下找
                            position = i + 9
                            while position < 64 and position % 8 != 0 and (i + j) % 8 != 7:
                                if obs[position] == 1:
                                    CanPutOrNot.append(i + j)
                                    break
                                elif obs[position] == 0:
                                    break
                                position += 9
                            
                        elif j == -8:  #上面那格，往下找
                            position = i + 8
                            while position < 64:
                                if obs[position] == 1:
                                    CanPutOrNot.append(i + j)
                                    break
                                elif obs[position] == 0:
                                    break
                                position += 8
                            
                        elif j == -7:  #右上那格，往左下找
                            position = i + 7
                            while position < 64 and position % 8 != 7 and (i + j) % 8 != 0:
                                if obs[position] == 1:
                                    CanPutOrNot.append(i + j)
                                    break
                                elif obs[position] == 0:
                                    break
                                position += 7
                            
                        elif j == -1:  #左邊那格，往右找
                            position = i + 1
                            while position < 64 and position % 8 != 0 and (i + j) % 8 != 7:
                                if obs[position] == 1:
                                    CanPutOrNot.append(i + j)
                                    break
                                elif obs[position] == 0:
                                    break
                                position += 1
                            
                        elif j == 1:  #右邊那格，往左找
                            position = i - 1
                            while position >= 0 and position % 8 != 7 and (i + j) % 8 != 0:
                                if obs[position] == 1:
                                    CanPutOrNot.append(i + j)
                                    break
                                elif obs[position] == 0:
                                    break
                                position -= 1
                        
                        elif j == 7:  #左下那格，往右上找
                            position = i - 7
                            while position >= 0 and position % 8 != 0 and (i + j) % 8 != 7:
                                if obs[position] == 1:
                                    CanPutOrNot.append(i + j)
                                    break
                                elif obs[position] == 0:
                                    break
                                position -= 7
                        
                        elif j == 8:  #下面那格，往上面找
                            position = i - 8
                            while position >= 0:
                                if obs[position] == 1:
                                    CanPutOrNot.append(i + j)
                                    break
                                elif obs[position] == 0:
                                    break
                                position -= 8
                        
                        elif j == 9:  #右下那格，往左上找
                            position = i - 9
                            while position >= 0 and position % 8 != 7 and (i + j) % 8 != 0:
                                if obs[position] == 1:
                                    CanPutOrNot.append(i + j)
                                    break
                                elif obs[position] == 0:
                                    break
                                position -= 9
        return CanPutOrNot
        
    
    def step(self, reward, obs):
        
        #黑子
        if self.color == 'black':
            CanPutOrNot = self.WhereCanMove(obs, 'black')
            if 0 in CanPutOrNot:
                return (self.col_offset + 0 * self.block_len, self.row_offset + 0 * self.block_len), pygame.USEREVENT
            elif 7 in CanPutOrNot:
                return (self.col_offset + 7 * self.block_len, self.row_offset + 0 * self.block_len), pygame.USEREVENT
            elif 56 in CanPutOrNot:
                return (self.col_offset + 0 * self.block_len, self.row_offset + 7 * self.block_len), pygame.USEREVENT
            elif 63 in CanPutOrNot:
                return (self.col_offset + 7 * self.block_len, self.row_offset + 7 * self.block_len), pygame.USEREVENT
            
            else:
                score = []
                otherScore = []
                save, scoreBiggest = 0, -10
                ListCount = 0  #計算list的第幾個
                
                for i in CanPutOrNot:
                    count = 0      #翻子數
                    biggest = 0
                    Setobs = obs.copy()  #模擬下子後的結果(模擬地圖)
                    Setobs[i] = -1
                    good = 0  #判斷C位適不適合下
                
                    for j in (-9, -8, -7, -1, 1, 7, 8, 9):  #算自己下在此處將會有多少翻子數
                        
                        if i in (1, 8, 9) and obs[0] == 0:
                            
                            if i == 1 and obs[7] == -1:
                                for test in (2, 3, 4, 5, 6):
                                    if Setobs[test] == 1:  Setobs[test] = -1
                                    else:  break
                                for test in (2, 3, 4, 5, 6):
                                    if Setobs[test] != -1:  good = 1
                                if good == 1:
                                    count = -50
                                    break
                            elif i == 8 and obs[56] == -1:
                                for test in (16, 24, 32, 40, 48):
                                    if Setobs[test] == 1:  Setobs[test] = -1
                                    else:  break
                                for test in (16, 24, 32, 40, 48):
                                    if Setobs[test] != -1:  good = 1
                                if good == 1:
                                    count = -50
                                    break
                            else:
                                count = -50
                                break
                            
                        elif i in (6, 14, 15) and obs[7] == 0:
                            
                            if i == 6 and obs[0] == -1:
                                for test in (5, 4, 3, 2, 1):
                                    if Setobs[test] == 1:  Setobs[test] = -1
                                    else:  break
                                for test in (5, 4, 3, 2, 1):
                                    if Setobs[test] != -1:  good = 1
                                if good == 1:
                                    count = -50
                                    break
                            elif i == 15 and obs[63] == -1:
                                for test in (23, 31, 39, 47, 55):
                                    if Setobs[test] == 1:  Setobs[test] = -1
                                    else:  break
                                for test in (23, 31, 39, 47, 55):
                                    if Setobs[test] != -1:  good = 1
                                if good == 1:
                                    count = -50
                                    break
                            else:
                                count = -50
                                break
                            
                        elif i in (48, 49, 57) and obs[56] == 0:
                            
                            if i == 48 and obs[0] == -1:
                                for test in (40, 32, 24, 16, 8):
                                    if Setobs[test] == 1:  Setobs[test] = -1
                                    else:  break
                                for test in (40, 32, 24, 16, 8):
                                    if Setobs[test] != -1:  good = 1
                                if good == 1:
                                    count = -50
                                    break
                            elif i == 57 and obs[63] == -1:
                                for test in (58, 59, 60, 61, 62):
                                    if Setobs[test] == 1:  Setobs[test] = -1
                                    else:  break
                                for test in (58, 59, 60, 61, 62):
                                    if Setobs[test] != -1:  good = 1
                                if good == 1:
                                    count = -50
                                    break
                            else:
                                count = -50
                                break
                            
                        elif i in (54, 55, 62) and obs[63] == 0:
                            
                            if i == 55 and obs[7] == -1:
                                for test in (47, 39, 31, 23, 15):
                                    if Setobs[test] == 1:  Setobs[test] = -1
                                    else:  break
                                for test in (47, 39, 31, 23, 15):
                                    if Setobs[test] != -1:  good = 1
                                if good == 1:
                                    count = -50
                                    break
                            elif i == 62 and obs[56] == -1:
                                for test in (61, 60, 59, 58, 57):
                                    if Setobs[test] == 1:  Setobs[test] = -1
                                    else:  break
                                for test in (61, 60, 59, 58, 57):
                                    if Setobs[test] != -1:  good = 1
                                if good == 1:
                                    count = -50
                                    break
                            else:
                                count = -50
                                break
                        
                        Setobs = obs.copy()
                        Setobs[i] = -1
                        position = i + j
                        if position < 0 or position > 63:
                            continue
                    
                        elif obs[position] == 1:  #鄰邊是白子
                            tempcount = 0
                        
                            if j == -9:  #左上有白子，往左上算
                                while position >= 0 and position % 8 != 7:
                                    if obs[position] == 1:
                                        tempcount += 1
                                    elif obs[position] == -1:
                                        count += tempcount
                                        for gg in range(1, tempcount + 1):
                                            Setobs[position + 9 * gg] = -1
                                        break
                                    elif obs[position] == 0:
                                        break
                                    position -= 9
                                
                            elif j == -8:  #上有白子，往上算
                                while position >= 0:
                                    if obs[position] == 1:
                                        tempcount += 1
                                    elif obs[position] == -1:
                                        count += tempcount
                                        for gg in range(1, tempcount + 1):
                                            Setobs[position + 8 * gg] = -1
                                        break
                                    elif obs[position] == 0:
                                        break
                                    position -= 8
                            
                            elif j == -7:  #右上有白子，往右上算
                                while position >= 0 and position % 8 != 0:
                                    if obs[position] == 1:
                                        tempcount += 1
                                    elif obs[position] == -1:
                                        count += tempcount
                                        for gg in range(1, tempcount + 1):
                                            Setobs[position + 7 * gg] = -1
                                        break
                                    elif obs[position] == 0:
                                        break
                                    position -= 7
                                
                            elif j == -1:  #左有白子，往左算
                                while position >= 0 and position % 8 != 7:
                                    if obs[position] == 1:
                                        tempcount += 1
                                    elif obs[position] == -1:
                                        count += tempcount
                                        for gg in range(1, tempcount + 1):
                                            Setobs[position + 1 * gg] = -1
                                        break
                                    elif obs[position] == 0:
                                        break
                                    position -= 1
                                
                            elif j == 1:  #右有白子，往右算
                                while position < 64 and position % 8 != 0:
                                    if obs[position] == 1:
                                        tempcount += 1
                                    elif obs[position] == -1:
                                        count += tempcount
                                        for gg in range(1, tempcount + 1):
                                            Setobs[position - 1 * gg] = -1
                                        break
                                    elif obs[position] == 0:
                                        break
                                    position += 1
                                
                            elif j == 7:  #左下有白子，往左下算
                                while position < 64 and position % 8 != 7:
                                    if obs[position] == 1:
                                        tempcount += 1
                                    elif obs[position] == -1:
                                        count += tempcount
                                        for gg in range(1, tempcount + 1):
                                            Setobs[position - 7 * gg] = -1
                                        break
                                    elif obs[position] == 0:
                                        break
                                    position += 7
                                    
                            elif j == 8:  #下有白子，往下算
                                while position < 64:
                                    if obs[position] == 1:
                                        tempcount += 1
                                    elif obs[position] == -1:
                                        count += tempcount
                                        for gg in range(1, tempcount + 1):
                                            Setobs[position - 8 * gg] = -1
                                        break
                                    elif obs[position] == 0:
                                        break
                                    position += 8
                                
                            elif j == 9:  #右下有白子，往右下算
                                while position < 64 and position % 8 != 0:
                                    if obs[position] == 1:
                                        tempcount += 1
                                    elif obs[position] == -1:
                                        count += tempcount
                                        for gg in range(1, tempcount + 1):
                                            Setobs[position - 9 * gg] = -1
                                        break
                                    elif obs[position] == 0:
                                        break
                                    position += 9
                                
                    score.append(count)
                    
                    OtherCanPutOrNot = self.WhereCanMove(Setobs, 'white')
                    
                    for j in OtherCanPutOrNot:  #對方在下一步能翻的最多子數
                        count = 0
                        if 0 in OtherCanPutOrNot or 7 in OtherCanPutOrNot or 56 in OtherCanPutOrNot or 63 in OtherCanPutOrNot:
                            otherScore.append(100)
                            biggest = 1
                            break
                            
                        for k in (-9, -8, -7, -1, 1, 7, 8, 9):  
                            position = j + k
                            if position < 0 or position > 63:
                                continue
                    
                            elif Setobs[position] == -1:  #鄰邊是黑子
                                tempcount = 0
                        
                                if k == -9:  #左上有黑子，往左上算
                                    while position >= 0 and position % 8 != 7:
                                        if Setobs[position] == -1:
                                            tempcount += 1
                                        elif Setobs[position] == 1:
                                            count += tempcount
                                            break
                                        elif Setobs[position] == 0:
                                            break
                                        position -= 9
                                
                                elif k == -8:  #上有黑子，往上算
                                    while position >= 0:
                                        if Setobs[position] == -1:
                                            tempcount += 1
                                        elif Setobs[position] == 1:
                                            count += tempcount
                                            break
                                        elif Setobs[position] == 0:
                                            break
                                        position -= 8
                            
                                elif k == -7:  #右上有黑子，往右上算
                                    while position >= 0 and position % 8 != 0:
                                        if Setobs[position] == -1:
                                            tempcount += 1
                                        elif Setobs[position] == 1:
                                            count += tempcount
                                            break
                                        elif Setobs[position] == 0:
                                            break
                                        position -= 7
                                
                                elif k == -1:  #左有黑子，往左算
                                    while position >= 0 and position % 8 != 7:
                                        if Setobs[position] == -1:
                                            tempcount += 1
                                        elif Setobs[position] == 1:
                                            count += tempcount
                                            break
                                        elif Setobs[position] == 0:
                                            break
                                        position -= 1
                                
                                elif k == 1:  #右有黑子，往右算
                                    while position < 64 and position % 8 != 0:
                                        if Setobs[position] == -1:
                                            tempcount += 1
                                        elif Setobs[position] == 1:
                                            count += tempcount
                                            break
                                        elif Setobs[position] == 0:
                                            break
                                        position += 1
                                
                                elif k == 7:  #左下有黑子，往左下算
                                    while position < 64 and position % 8 != 7:
                                        if Setobs[position] == -1:
                                            tempcount += 1
                                        elif Setobs[position] == 1:
                                            count += tempcount
                                            break
                                        elif Setobs[position] == 0:
                                            break
                                        position += 7
                                    
                                elif k == 8:  #下有黑子，往下算
                                    while position < 64:
                                        if Setobs[position] == -1:
                                            tempcount += 1
                                        elif Setobs[position] == 1:
                                            count += tempcount
                                            break
                                        elif Setobs[position] == 0:
                                            break
                                        position += 8
                                
                                elif k == 9:  #右下有黑子，往右下算
                                    while position < 64 and position % 8 != 0:
                                        if Setobs[position] == -1:
                                            tempcount += 1
                                        elif Setobs[position] == 1:
                                            count += tempcount
                                            break
                                        elif Setobs[position] == 0:
                                            break
                                        position += 9
                                       
                        if biggest == 0:
                            otherScore.append(count)
                            biggest = count
                                            
                        elif count > biggest:
                            otherScore.pop()
                            otherScore.append(count)
                            biggest = count
                    
                    if biggest == 0:
                        otherScore.append(0)
                        save = i
                        scoreBiggest = 100
                    elif score[ListCount] - otherScore[ListCount] > scoreBiggest:
                        scoreBiggest = score[ListCount] - otherScore[ListCount]
                        save = i
                    elif save == 0: save = i  #預設第一個
                    ListCount += 1
                    
            return (self.col_offset + save % 8 * self.block_len, self.row_offset + save // 8 * self.block_len), pygame.USEREVENT
        
        #白子
        elif self.color == 'white':
            CanPutOrNot = self.WhereCanMove(obs, 'white')
            if 0 in CanPutOrNot:
                return (self.col_offset + 0 * self.block_len, self.row_offset + 0 * self.block_len), pygame.USEREVENT
            elif 7 in CanPutOrNot:
                return (self.col_offset + 7 * self.block_len, self.row_offset + 0 * self.block_len), pygame.USEREVENT
            elif 56 in CanPutOrNot:
                return (self.col_offset + 0 * self.block_len, self.row_offset + 7 * self.block_len), pygame.USEREVENT
            elif 63 in CanPutOrNot:
                return (self.col_offset + 7 * self.block_len, self.row_offset + 7 * self.block_len), pygame.USEREVENT
            
            else:
                score = []
                otherScore = []
                save, scoreBiggest = 0, -10
                ListCount = 0  #計算list的第幾個
                
                for i in CanPutOrNot:
                    count = 0      #翻子數
                    biggest = 0
                    Setobs = obs.copy()  #模擬下子後的結果(模擬地圖)
                    Setobs[i] = 1
                    good = 0  #判斷C位適不適合下
                    
                    for j in (-9, -8, -7, -1, 1, 7, 8, 9):  #算自己下在此處將會有多少翻子數
                        
                        if i in (1, 8, 9) and obs[0] == 0:
                            
                            if i == 1 and obs[7] == 1:
                                for test in (2, 3, 4, 5, 6):
                                    if Setobs[test] == -1:  Setobs[test] = 1
                                    else:  break
                                for test in (2, 3, 4, 5, 6):
                                    if Setobs[test] != 1:  good = 1
                                if good == 1:
                                    count = -50
                                    break
                            elif i == 8 and obs[56] == 1:
                                for test in (16, 24, 32, 40, 48):
                                    if Setobs[test] == -1:  Setobs[test] = 1
                                    else:  break
                                for test in (16, 24, 32, 40, 48):
                                    if Setobs[test] != 1:  good = 1
                                if good == 1:
                                    count = -50
                                    break
                            else:
                                count = -50
                                break
                            
                        elif i in (6, 14, 15) and obs[7] == 0:
                            
                            if i == 6 and obs[0] == 1:
                                for test in (5, 4, 3, 2, 1):
                                    if Setobs[test] == -1:  Setobs[test] = 1
                                    else:  break
                                for test in (5, 4, 3, 2, 1):
                                    if Setobs[test] != 1:  good = 1
                                if good == 1:
                                    count = -50
                                    break
                            elif i == 15 and obs[63] == 1:
                                for test in (23, 31, 39, 47, 55):
                                    if Setobs[test] == -1:  Setobs[test] = 1
                                    else:  break
                                for test in (23, 31, 39, 47, 55):
                                    if Setobs[test] != 1:  good = 1
                                if good == 1:
                                    count = -50
                                    break
                            else:
                                count = -50
                                break
                            
                        elif i in (48, 49, 57) and obs[56] == 0:
                            
                            if i == 48 and obs[0] == 1:
                                for test in (40, 32, 24, 16, 8):
                                    if Setobs[test] == -1:  Setobs[test] = 1
                                    else:  break
                                for test in (40, 32, 24, 16, 8):
                                    if Setobs[test] != 1:  good = 1
                                if good == 1:
                                    count = -50
                                    break
                            elif i == 57 and obs[63] == 1:
                                for test in (58, 59, 60, 61, 62):
                                    if Setobs[test] == -1:  Setobs[test] = 1
                                    else:  break
                                for test in (58, 59, 60, 61, 62):
                                    if Setobs[test] != 1:  good = 1
                                if good == 1:
                                    count = -50
                                    break
                            else:
                                count = -50
                                break
                            
                        elif i in (54, 55, 62) and obs[63] == 0:
                            
                            if i == 55 and obs[7] == 1:
                                for test in (47, 39, 31, 23, 15):
                                    if Setobs[test] == -1:  Setobs[test] = 1
                                    else:  break
                                for test in (47, 39, 31, 23, 15):
                                    if Setobs[test] != 1:  good = 1
                                if good == 1:
                                    count = -50
                                    break
                            elif i == 62 and obs[56] == 1:
                                for test in (61, 60, 59, 58, 57):
                                    if Setobs[test] == -1:  Setobs[test] = 1
                                    else:  break
                                for test in (61, 60, 59, 58, 57):
                                    if Setobs[test] != 1:  good = 1
                                if good == 1:
                                    count = -50
                                    break
                            else:
                                count = -50
                                break
                        
                        Setobs = obs.copy()
                        Setobs[i] = -1
                        position = i + j
                        if position < 0 or position > 63:
                            continue
                    
                        elif obs[position] == -1:  #鄰邊是黑子
                            tempcount = 0
                        
                            if j == -9:  #左上有黑子，往左上算
                                while position >= 0 and position % 8 != 7:
                                    if obs[position] == -1:
                                        tempcount += 1
                                    elif obs[position] == 1:
                                        count += tempcount
                                        for gg in range(1, tempcount + 1):
                                            Setobs[position + 9 * gg] = 1
                                        break
                                    elif obs[position] == 0:
                                        break
                                    position -= 9
                                
                            elif j == -8:  #上有黑子，往上算
                                while position >= 0:
                                    if obs[position] == -1:
                                        tempcount += 1
                                    elif obs[position] == 1:
                                        count += tempcount
                                        for gg in range(1, tempcount + 1):
                                            Setobs[position + 8 * gg] = 1
                                        break
                                    elif obs[position] == 0:
                                        break
                                    position -= 8
                            
                            elif j == -7:  #右上有黑子，往右上算
                                while position >= 0 and position % 8 != 0:
                                    if obs[position] == -1:
                                        tempcount += 1
                                    elif obs[position] == 1:
                                        count += tempcount
                                        for gg in range(1, tempcount + 1):
                                            Setobs[position + 7 * gg] = 1
                                        break
                                    elif obs[position] == 0:
                                        break
                                    position -= 7
                                
                            elif j == -1:  #左有黑子，往左算
                                while position >= 0 and position % 8 != 7:
                                    if obs[position] == -1:
                                        tempcount += 1
                                    elif obs[position] == 1:
                                        count += tempcount
                                        for gg in range(1, tempcount + 1):
                                            Setobs[position + gg] = 1
                                        break
                                    elif obs[position] == 0:
                                        break
                                    position -= 1
                                
                            elif j == 1:  #右有黑子，往右算
                                while position < 64 and position % 8 != 0:
                                    if obs[position] == -1:
                                        tempcount += 1
                                    elif obs[position] == 1:
                                        count += tempcount
                                        for gg in range(1, tempcount + 1):
                                            Setobs[position - gg] = 1
                                        break
                                    elif obs[position] == 0:
                                        break
                                    position += 1
                                
                            elif j == 7:  #左下有黑子，往左下算
                                while position < 64 and position % 8 != 7:
                                    if obs[position] == -1:
                                        tempcount += 1
                                    elif obs[position] == 1:
                                        count += tempcount
                                        for gg in range(1, tempcount + 1):
                                            Setobs[position - 7 * gg] = 1
                                        break
                                    elif obs[position] == 0:
                                        break
                                    position += 7
                                    
                            elif j == 8:  #下有黑子，往下算
                                while position < 64:
                                    if obs[position] == -1:
                                        tempcount += 1
                                    elif obs[position] == 1:
                                        count += tempcount
                                        for gg in range(1, tempcount + 1):
                                            Setobs[position - 8 * gg] = 1
                                        break
                                    elif obs[position] == 0:
                                        break
                                    position += 8
                                
                            elif j == 9:  #右下有黑子，往右下算
                                while position < 64 and position % 8 != 0:
                                    if obs[position] == -1:
                                        tempcount += 1
                                    elif obs[position] == 1:
                                        count += tempcount
                                        for gg in range(1, tempcount + 1):
                                            Setobs[position - 9 * gg] = 1
                                        break
                                    elif obs[position] == 0:
                                        break
                                    position += 9
                                
                    score.append(count)
                    
                    OtherCanPutOrNot = self.WhereCanMove(Setobs, 'black')
                    
                    for j in OtherCanPutOrNot:  #對方在下一步能翻的最多子數
                        count = 0
                        if 0 in OtherCanPutOrNot or 7 in OtherCanPutOrNot or 56 in OtherCanPutOrNot or 63 in OtherCanPutOrNot:
                            otherScore.append(100)
                            biggest = 1
                            break
                            
                        for k in (-9, -8, -7, -1, 1, 7, 8, 9):  
                            position = j + k
                            if position < 0 or position > 63:
                                continue
                    
                            elif Setobs[position] == 1:  #鄰邊是白子
                                tempcount = 0
                        
                                if k == -9:  #左上有白子，往左上算
                                    while position >= 0 and position % 8 != 7:
                                        if Setobs[position] == 1:
                                            tempcount += 1
                                        elif Setobs[position] == -1:
                                            count += tempcount
                                            break
                                        elif Setobs[position] == 0:
                                            break
                                        position -= 9
                                
                                elif k == -8:  #上有白子，往上算
                                    while position >= 0:
                                        if Setobs[position] == 1:
                                            tempcount += 1
                                        elif Setobs[position] == -1:
                                            count += tempcount
                                            break
                                        elif Setobs[position] == 0:
                                            break
                                        position -= 8
                            
                                elif k == -7:  #右上有白子，往右上算
                                    while position >= 0 and position % 8 != 0:
                                        if Setobs[position] == 1:
                                            tempcount += 1
                                        elif Setobs[position] == -1:
                                            count += tempcount
                                            break
                                        elif Setobs[position] == 0:
                                            break
                                        position -= 7
                                
                                elif k == -1:  #左有白子，往左算
                                    while position >= 0 and position % 8 != 7:
                                        if Setobs[position] == 1:
                                            tempcount += 1
                                        elif Setobs[position] == -1:
                                            count += tempcount
                                            break
                                        elif Setobs[position] == 0:
                                            break
                                        position -= 1
                                
                                elif k == 1:  #右有白子，往右算
                                    while position < 64 and position % 8 != 0:
                                        if Setobs[position] == 1:
                                            tempcount += 1
                                        elif Setobs[position] == -1:
                                            count += tempcount
                                            break
                                        elif Setobs[position] == 0:
                                            break
                                        position += 1
                                
                                elif k == 7:  #左下有白子，往左下算
                                    while position < 64 and position % 8 != 7:
                                        if Setobs[position] == 1:
                                            tempcount += 1
                                        elif Setobs[position] == -1:
                                            count += tempcount
                                            break
                                        elif Setobs[position] == 0:
                                            break
                                        position += 7
                                    
                                elif k == 8:  #下有白子，往下算
                                    while position < 64:
                                        if Setobs[position] == 1:
                                            tempcount += 1
                                        elif Setobs[position] == -1:
                                            count += tempcount
                                            break
                                        elif Setobs[position] == 0:
                                            break
                                        position += 8
                                
                                elif k == 9:  #右下有白子，往右下算
                                    while position < 64 and position % 8 != 0:
                                        if Setobs[position] == 1:
                                            tempcount += 1
                                        elif Setobs[position] == -1:
                                            count += tempcount
                                            break
                                        elif Setobs[position] == 0:
                                            break
                                        position += 9
                                       
                        if biggest == 0:
                            otherScore.append(count)
                            biggest = count
                                            
                        elif count > biggest:
                            otherScore.pop()
                            otherScore.append(count)
                            biggest = count
                    
                    if biggest == 0:
                        otherScore.append(0)
                        save = i
                        scoreBiggest = 100
                    elif score[ListCount] - otherScore[ListCount] > scoreBiggest:
                        scoreBiggest = score[ListCount] - otherScore[ListCount]
                        save = i
                    elif save == 0: save = i  #預設第一個
                    ListCount += 1
                    
            return (self.col_offset + save % 8 * self.block_len, self.row_offset + save // 8 * self.block_len), pygame.USEREVENT