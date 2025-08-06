from time import sleep

'''def show_character(oled_screen,character_hex,x,y,height,width):
    character_bin=[bin(hex).replace('0b','') for hex in character_hex]
    for i in range(len(character_bin)):
        single_bin=character_bin[i]
        single_bin='0'*(8-len(single_bin))+single_bin
        character_bin[i]=single_bin
    col=height//8-1
#     row=width//8-1
    for i in range(col+1):    #第x列
        for j in range(height):    #第x行
            print('\n')
            for yy in range(8):    #列
                oled_screen.pixel(x+i*8+yy,y+j,int(character_bin[16*i+j][yy]))
                print(x+i*16+yy,y+j,16*i+j,i,j,yy)
            oled_screen.show()'''

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
            


'''def show_character(oled_screen, character_hex, x, y, width, height):
    # 计算每列的字节数（高度方向每 8 行一个字节）
    bytes_per_col = height   # 32行 → 4字节/列
    total_cols = width // 8      # 32列 → 4字节/列？不，width是像素宽度，每列的字节数由height决定
    
    # 总字节数应等于 total_cols * bytes_per_col（32列 ×4字节=128字节，匹配你的wu数据）
    total_bytes = len(character_hex)
    if total_bytes != total_cols * bytes_per_col:
        raise ValueError(f"点阵数据长度错误！需要 {total_cols*bytes_per_col} 字节，实际 {total_bytes} 字节")
    
    # 转换为 8 位二进制字符串（补前导零）
    character_bin = ['0'*(8-len(str(b)))+str(b) for b in character_hex]  # 更可靠的补零方式
    
    # 遍历每一列（水平方向）
    for col in range(total_cols):  # 32列
        # 遍历该列的每一个字节（垂直方向，每字节对应8行）
        for byte_idx_in_col in range(bytes_per_col):  # 每列4字节（32行→4×8）
            # 计算当前字节在数组中的全局索引（列优先）
            global_byte_idx = col * bytes_per_col + byte_idx_in_col
            byte_data = character_bin[global_byte_idx]
            
            # 遍历当前字节的每一位（对应垂直方向的8行）
            for bit in range(8):  # 每个字节8位，对应8行
                # 计算像素的垂直坐标（当前字节对应行范围：byte_idx_in_col*8 到 (byte_idx_in_col+1)*8 -1）
                pixel_y = y + byte_idx_in_col * 8 + bit
                # 水平坐标（当前列 + 列内偏移，这里列内只有1列，所以直接是x + col）
                pixel_x = x + col
                
                # 根据二进制位设置像素（假设高位在上，即byte_data[0]对应最上行）
                # 注意：若实际显示上下颠倒，可能需要反转bit顺序（如用 7 - bit）
                if int(byte_data[bit]):
                    oled_screen.pixel(pixel_x, pixel_y, 1)'''
