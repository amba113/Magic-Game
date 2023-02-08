def smoothColor(c1, c2, c3, c4, val, top):
    percent = val/top * 100
    
    if percent >= 100:
        color = c4
        return c4
    elif percent > 75:
        l = c3
        h = c4
        newP = (percent - 75)/25 * 100
    elif percent == 75:
        color = c3
        return color
    elif percent > 50:
        l = c2
        h = c3
        newP = (percent - 50)/25 * 100
    elif percent == 50:
        color = c2
        return color
    elif percent > 20:
        l = c1
        h = c2
        newP = (percent - 20)/30 * 100
    elif percent >= 0:
        color = c1
        return color
        
    if newP == 100:
        color = h
    elif newP == 0:
        color = l
    else:
        r1, g1, b1 = h
        r2, g2, b2 = l
        
        rD = r1 - r2
        gD = g1 - g2
        bD = b1 - b2
                
        color = (r2 + (rD * (newP/100)), g2 + (gD * (newP/100)), b2 + (bD * (newP/100)))
    
    return color
    
