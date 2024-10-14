"""None"""

def num_rushes(slope_height, rush_height_gain, back_sliding):
    """Calculates the number of rushes needed for Hilda the Heffalump to climb the slope."""
    current_height = 0
    rushes = 0
    while current_height < slope_height:
        rushes += 1
        current_height += rush_height_gain
        if current_height < slope_height:
            current_height -= back_sliding
    return rushes
