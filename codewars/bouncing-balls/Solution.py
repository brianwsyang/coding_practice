def bouncing_ball(h, bounce, window):
    # if 3 conditions aren't met, invalid experiment
    # condition 1: 0 < h
    # condition 2: 0 < bounce < 1
    # condition 3: window < h 
    if (not 0 <= window < h) or (not 0 < bounce < 1):
        return -1
    
    # rebound count as seeing the ball twice
    def check_rebound(h, bounce, window):
        if h > window:
            return 2 + check_rebound(h * bounce, bounce, window)
        else:
            return 0
    
    # initial drop + rebound
    return 1 + check_rebound(h * bounce, bounce, window)