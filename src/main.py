

def fair_sharer(values, num_interations, share=0.1):
    for a in range(num_interations):
        max_val = max(values)
        share_as_val = max(values)*share
        for pos, val in enumerate(values):
            if val == max_val:
                values[pos-1] += share_as_val
                values[pos+1] += share_as_val
                values[pos] = values[pos]-share_as_val*2
    return values
