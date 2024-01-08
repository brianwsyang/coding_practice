def sq_in_rect(lng, wdth):
    
    # recursively calculate all squares in rectangle
    def calc_sq(lng, wdth):
        if lng * wdth != 0:
            return [min(lng, wdth)] * (max(lng, wdth) // min(lng, wdth)) + calc_sq(min(lng, wdth), max(lng, wdth) % min(lng, wdth)) 
        else:
            return []

    if lng == wdth:
        return None
    else:
        return calc_sq(lng, wdth)