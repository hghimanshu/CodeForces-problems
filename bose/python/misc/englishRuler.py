def draw_line(tickLength,tick_label=""):
    line = "-"*tickLength
    if tick_label:
        line+= " "+tick_label
    print(line)

def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length-1)
        draw_line(center_length)
        draw_interval(center_length -1)

def draw_ruler(num_inches,major_length):
    """num_inches specifies\
     the number of inches to
      draw until and major
       is the max length
        of the tick line"""
    draw_line(major_length,"0")
    for j in range(1,num_inches+1):
        draw_interval(major_length-1)
        draw_line(major_length,str(j))
        

draw_ruler(1,3)


