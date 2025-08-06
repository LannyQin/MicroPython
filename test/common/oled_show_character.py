"""使用Pctolcd生成character_hex的时候一定要将每行显示的点阵数设为height"""
from time import sleep


def show_character(oled_screen,character_hex_old,x,y,height,width):
    character_hex=character_hex_old.copy()
    try:
        for c in character_hex:
            for r in range(len(c)):
                c[r]=bin(c[r]).replace('0b','')
                c[r]='0'*(8-len(c[r]))+c[r]
    except ValueError:
        pass
    for i in range(width//8):
        for j in range(height):
            for small_col in range(8):
                oled_screen.pixel(x+i*8+small_col,y+j,int(character_hex[i][j][small_col]))
    oled_screen.show()