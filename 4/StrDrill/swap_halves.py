def swap_halves(s):
    """DS"""
    i_mid = len(s) // 2
    output = s[i_mid:] + s[:i_mid]
    return output