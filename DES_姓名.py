

#IP置换表
IP_table=[58, 50, 42, 34, 26, 18, 10,  2,
  60, 52, 44, 36, 28, 20, 12,  4,
  62, 54, 46, 38, 30, 22, 14,  6,
  64, 56, 48, 40, 32, 24, 16,  8,
  57, 49, 41, 33, 25, 17,  9,  1,
  59, 51, 43, 35, 27, 19, 11,  3,
  61, 53, 45, 37, 29, 21, 13,  5,
  63, 55, 47, 39, 31, 23, 15,  7
]
#逆IP置换表
_IP_table=[40,  8, 48, 16, 56, 24, 64, 32,
  39,  7, 47, 15, 55, 23, 63, 31,
  38,  6, 46, 14, 54, 22, 62, 30,
  37,  5, 45, 13, 53, 21, 61, 29,
  36,  4, 44, 12, 52, 20, 60, 28,
  35,  3, 43, 11, 51, 19, 59, 27,
  34,  2, 42, 10, 50, 18, 58, 26,
  33,  1, 41,  9, 49, 17, 57, 25
]
#S盒中的S1盒
S1=[14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7,
0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8,
4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0,
  15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13
]
#S盒中的S2盒
S2=[15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10,
3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5,
0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15,
  13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9
]
#S盒中的S3盒
S3=[10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8,
  13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1,
  13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7,
1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12
]
#S盒中的S4盒
S4=[7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15,
  13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9,
  10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4,
3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14
]
#S盒中的S5盒
S5=[2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9,
  14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6,
4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14,
  11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3
]
#S盒中的S6盒
S6=[12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11,
  10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8,
9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6,
4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13
]
#S盒中的S7盒
S7=[4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1,
  13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6,
1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2,
6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12
]
#S盒中的S8盒
S8=[13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7,
1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2,
7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8,
2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11
]
# S盒
S=[S1,S2,S3,S4,S5,S6,S7,S8]
#P盒
P_table=[16,  7, 20, 21,
  29, 12, 28, 17,
1, 15, 23, 26,
5, 18, 31, 10,
2,  8, 24, 14,
  32, 27,  3,  9,
  19, 13, 30,  6,
  22, 11,  4, 25
]
#压缩置换表1，不考虑每字节的第8位，将64位密钥减至56位。然后进行一次密钥置换。
yasuo1_table=[ 57, 49, 41, 33, 25, 17,  9,
1, 58, 50, 42, 34, 26, 18,
  10,  2, 59, 51, 43, 35, 27,
  19, 11,  3, 60, 52, 44, 36,
  63, 55, 47, 39, 31, 23, 15,
7, 62, 54, 46, 38, 30, 22,
  14,  6, 61, 53, 45, 37, 29,
  21, 13,  5, 28, 20, 12,  4
]


#压缩置换表2，用于将循环左移和右移后的56bit密钥压缩为48bit
yasuo2_table=[14, 17, 11, 24,  1,  5,
3, 28, 15,  6, 21, 10,
  23, 19, 12,  4, 26,  8,
  16,  7, 27, 20, 13,  2,
  41, 52, 31, 37, 47, 55,
  30, 40, 51, 45, 33, 48,
  44, 49, 39, 56, 34, 53,
  46, 42, 50, 36, 29, 32
]


#用于对数据进行扩展置换，将32bit数据扩展为48bit
extend_table=[32,  1,  2,  3,  4,  5,
4,  5,  6,  7,  8,  9,
8,  9, 10, 11, 12, 13,
  12, 13, 14, 15, 16, 17,
  16, 17, 18, 19, 20, 21,
  20, 21, 22, 23, 24, 25,
  24, 25, 26, 27, 28, 29,
  28, 29, 30, 31, 32,1
]
#将字符变为ASCII码
def char2ascii(Input):
  Output = []
  for i in Input:
      Output.append(ord(i))
  return Output

#将ASCII码变为十六进制
def ascii2HEX(Input):
  Output = ''
  for each in Input:
    Output = Output + str(hex(each)).split('x')[1]
  return Output

#将十六进制变为ASCII码
def HEX2ascii(Input):
    Output = ''
    for each in range(int(len(Input)/2)):
        Output = Output + str(int(Input[each*2]+Input[each*2+1], 16))
    return Output

#将ASCII码变为字符
def ascii2char(Input):
    Output = ''
    temp = ''
    flag = 0
    for each in Input:
        if each != '0':
            flag = 1
        if flag != 0:
            temp = temp + each
    for each in range(int(len(temp)/2)):
        Output = Output + chr(int(temp[each*2]+temp[each*2+1]))
    return Output

#将十六进制变为二进制
def HEX2BIN(Input):
  Output = ''
  temp = []
  for each in Input:
    temp.append(str(bin(int(each, 16))).split('b')[1])
  for each in temp:
    while(len(each) < 4):
      each = '0'+each
    Output = Output + each
  return Output

#将二进制变为十六进制
def BIN2HEX(Input):
  Output = ''
  for i in range(int(len(Input)/4)):
    Output = Output + str(hex(int(Input[i*4:i*4+4], 2))).split('x')[1]
  return Output

def createKEYS(inkeys):
  keyResult = []
  #asciikey = char2ascii(inkeys)
  #keyinit = HEX2BIN(ascii2HEX(asciikey))
  keyinit = HEX2BIN(inkeys)
  print('inkeys:',keyinit,',',len(keyinit))
  key0 = ''
  key1 = ''
  tempKey = []
  #进行第一次PC1置换
  for i in range(56):
    key0 = key0 + keyinit[yasuo1_table[i] - 1]
  for each in key0:
    tempKey.append(each)
  # 进行16轮的密码生成
  for i in range(16):
    # 确定左移的次数
    if i == 0 or i == 1 or i == 8 or i == 15:
      moveStep = 1
    else:
      moveStep = 2

    # 分两部分，每28bit位一部分，进行循环左移
    for j in range(moveStep):
      temp = tempKey[0]
      for k in range(27):
        tempKey[k] = tempKey[k + 1]
      tempKey[27] = temp

      temp = tempKey[28]
      for k in range(28, 55):
        tempKey[k] = tempKey[k + 1]
      tempKey[55] = temp

    #PC2 对56位密钥进行压缩置换，压缩为48位
    for k in range(48):
      key1 = key1 + tempKey[yasuo2_table[k] - 1]
    keyResult.append(key1)
    key1 = ''

  print('Keys:',keyResult)
  return keyResult

#IP置换
def IP_EXCHANGE(Input):
  Output = ''
  for i in range(64):
    Output = Output + Input[IP_table[i] - 1]

  print('IP:'+Output)
  return  Output

#逆IP置换
def _IP_EXCHANGE(Input):
  Output = ''
  for i in range(64):
    Output = Output + Input[_IP_table[i] - 1]
  print('_IP:' + Output)
  return Output

#对R部分进行扩展
def EXTEND_R(Input):
  Output = ''
  for i in range(48):
    Output = Output + Input[extend_table[i] - 1]
  print('EXTEND:' + Output)
  return Output

#异或运算
def XOR(A,B):
  Output = ''
  for i in range(len(A)):
    if A[i] != B[i]:
      Output = Output + '1'
    else:
      Output = Output + '0'
  print('XOR:' + Output)
  return Output

#P置换
def P_EXCHANGE(Input):
  Output = ''
  for i in range(32):
    Output = Output + Input[P_table[i] - 1]
  print('P:' + Output)
  return Output

#ECB模式加解密
def DES_ECB(bitT, key, option):
  if option == 1:
    #获得16轮加密
    print('this is DES_ECB')
    keys = createKEYS(key)
    result_bit = ''
    result_hex = ''

    #IP置换
    initT = IP_EXCHANGE(bitT)
    # 将64位明文分为左右两部分
    L = ''
    for i in range(32):
      L = L + initT[i]
    R = ''
    for i in range(32, 64):
      R = R + initT[i]

    #16轮运算
    for i in range(16):
      #扩展R部分
      extendR = EXTEND_R(R)

      #与keys[i]进行异或运算
      XORresult = XOR(extendR, keys[i])

      #S盒运算
      Sresult = ''
      for k in range(8):
        Sk = XORresult[k*6:k*6+6]
        temp1 = Sk[0] + Sk[5]
        temp2 = Sk[1] + Sk[2] + Sk[3] + Sk[4]
        temp3 = str(bin(S[k][int(temp1, 2) * 16 + int(temp2, 2)])).split('b')[1]
        if len(temp3) != 4:
          for j in range(4-len(temp3)):
            temp3 = '0' + temp3
        Sresult = Sresult + temp3

      #P盒置换
      Presult = P_EXCHANGE(Sresult)

      #与L部分进行异或
      XORwithL = XOR(Presult, L)

      #XORwithL 与 L部分交换
      L = R
      R = XORwithL

    #左右交换
    tempR = R
    R = L
    L = tempR

    #逆IP置换
    result_temp = L + R
    result_bit = _IP_EXCHANGE(result_temp)
    result_hex = BIN2HEX(result_bit)

  else:
    #获得16轮加密
    print('this is DES_ECB')
    keys = createKEYS(key)
    result_bit = ''
    result_hex = ''

    #IP置换
    initT = IP_EXCHANGE(bitT)
    # 将64位明文分为左右两部分
    L = ''
    for i in range(32):
      L = L + initT[i]
    R = ''
    for i in range(32, 64):
      R = R + initT[i]

    #16轮运算
    for i in range(16):
      #扩展R部分
      extendR = EXTEND_R(R)

      #与keys[i]进行异或运算
      XORresult = XOR(extendR, keys[15-i])

      #S盒运算
      Sresult = ''
      for k in range(8):
        Sk = XORresult[k*6:k*6+6]
        temp1 = Sk[0] + Sk[5]
        temp2 = Sk[1] + Sk[2] + Sk[3] + Sk[4]
        temp3 = str(bin(S[k][int(temp1, 2) * 16 + int(temp2, 2)])).split('b')[1]
        if len(temp3) != 4:
          for j in range(4-len(temp3)):
            temp3 = '0' + temp3
        Sresult = Sresult + temp3

      #P盒置换
      Presult = P_EXCHANGE(Sresult)

      #与L部分进行异或
      XORwithL = XOR(Presult, L)

      #XORwithL 与 L部分交换
      L = R
      R = XORwithL

    #左右交换
    tempR = R
    R = L
    L = tempR

    #逆IP置换
    result_temp = L + R
    result_bit = _IP_EXCHANGE(result_temp)
    result_hex = BIN2HEX(result_bit)

  return result_hex

#CBC模式加解密
def DES_CBC(bitT, key, option, lastC):
  if option == 1:
    # 获得16轮加密
    bitT = XOR(bitT, lastC)
    print('this is DES_ECB')
    keys = createKEYS(key)
    result_bit = ''
    result_hex = ''

    # IP置换
    initT = IP_EXCHANGE(bitT)
    # 将64位明文分为左右两部分
    L = ''
    for i in range(32):
      L = L + initT[i]
    R = ''
    for i in range(32, 64):
      R = R + initT[i]

    # 16轮运算
    for i in range(16):
      # 扩展R部分
      extendR = EXTEND_R(R)

      # 与keys[i]进行异或运算
      XORresult = XOR(extendR, keys[i])

      # S盒运算
      Sresult = ''
      for k in range(8):
        Sk = XORresult[k * 6:k * 6 + 6]
        temp1 = Sk[0] + Sk[5]
        temp2 = Sk[1] + Sk[2] + Sk[3] + Sk[4]
        temp3 = str(bin(S[k][int(temp1, 2) * 16 + int(temp2, 2)])).split('b')[1]
        if len(temp3) != 4:
          for j in range(4 - len(temp3)):
            temp3 = '0' + temp3
        Sresult = Sresult + temp3

      # P盒置换
      Presult = P_EXCHANGE(Sresult)

      # 与L部分进行异或
      XORwithL = XOR(Presult, L)

      # XORwithL 与 L部分交换
      L = R
      R = XORwithL

    # 左右交换
    tempR = R
    R = L
    L = tempR

    # 逆IP置换
    result_temp = L + R
    result_bit = _IP_EXCHANGE(result_temp)
    result_hex = BIN2HEX(result_bit)

  else:
    # 获得16轮加密
    print('this is DES_ECB')
    keys = createKEYS(key)
    result_bit = ''
    result_hex = ''

    # IP置换
    initT = IP_EXCHANGE(bitT)
    # 将64位明文分为左右两部分
    L = ''
    for i in range(32):
      L = L + initT[i]
    R = ''
    for i in range(32, 64):
      R = R + initT[i]

    # 16轮运算
    for i in range(16):
      # 扩展R部分
      extendR = EXTEND_R(R)

      # 与keys[i]进行异或运算
      XORresult = XOR(extendR, keys[15 - i])

      # S盒运算
      Sresult = ''
      for k in range(8):
        Sk = XORresult[k * 6:k * 6 + 6]
        temp1 = Sk[0] + Sk[5]
        temp2 = Sk[1] + Sk[2] + Sk[3] + Sk[4]
        temp3 = str(bin(S[k][int(temp1, 2) * 16 + int(temp2, 2)])).split('b')[1]
        if len(temp3) != 4:
          for j in range(4 - len(temp3)):
            temp3 = '0' + temp3
        Sresult = Sresult + temp3

      # P盒置换
      Presult = P_EXCHANGE(Sresult)

      # 与L部分进行异或
      XORwithL = XOR(Presult, L)

      # XORwithL 与 L部分交换
      L = R
      R = XORwithL

    # 左右交换
    tempR = R
    R = L
    L = tempR

    # 逆IP置换
    result_temp = L + R
    result_bit = XOR(_IP_EXCHANGE(result_temp), lastC)
    result_hex = BIN2HEX(result_bit)

  return result_hex
#主函数
def main():
    #加密
    with open('des_messages.txt', 'r') as f:
      Mtexts = f.read().splitlines()
    with open('des_key.txt', 'r') as f:
      keys = f.read().splitlines()
    with open('des_iv.txt', 'r') as f:
      iv = f.read().splitlines()
    bitIV = []
    for i in range(len(iv)):
      bitIV.append(HEX2BIN(iv[i]))

    # cipher_CBC = []
    cipher_ECB = []
    for i in range(len(Mtexts)):
      print(Mtexts[i])
      hexText = ascii2HEX(char2ascii(Mtexts[i]))
      bitText = HEX2BIN(ascii2HEX(char2ascii(Mtexts[i])))
      #bitText = HEX2BIN(Mtexts[i])
      if len(bitText) % 64 != 0:
        for k in range(64 - (len(bitText) % 64)):
          bitText = '0' + bitText

      #进入ECB加密运算
      for k in range(int(len(bitText)/64)):
        cipher_ECB.append(DES_ECB(bitText[k*64 : (k+1)*64], keys[i], 1))
      #进入CBC加密运算
      for k in range(int(len(bitText)/64)):
        if k == 0:
          cipher_CBC.append(DES_CBC(bitText[k*64 : (k+1)*64], keys[i], 1, bitIV[i]))
          print('k=0')
        else:
          cipher_CBC.append(DES_CBC(bitText[k*64 : (k+1)*64], keys[i], 1, HEX2BIN(cipher_CBC[k-1])))
    #写入des_secret.txt
    Cresult_ECB = ''
    Cresult_CBC = ''
    with open('des_secret.txt', 'w') as f:
      for each in cipher_ECB:
        Cresult_ECB = Cresult_ECB + each
      f.write(Cresult_ECB)
      f.write('\n')
      for each in cipher_CBC:
        Cresult_CBC = Cresult_CBC + each
      f.write(Cresult_CBC)

    #解密：
    with open('des_secret.txt', 'r') as f:
      Ctexts = f.read().splitlines()

    texts_CBC = []
    texts_ECB = []
    for i in range(int(len(Ctexts)/2)):
      print(Ctexts[i])
      bitText_ECB = HEX2BIN(Ctexts[i*2])
      bitText_CBC = HEX2BIN(Ctexts[i*2+1])
      #bitText_ECB = HEX2BIN(Ctexts[i*2])
      #bitText_CBC = HEX2BIN(Ctexts[i*2+1])
      #进入ECB解密运算
      for k in range(int(len(bitText_ECB)/64)):
        print(Ctexts[0], Ctexts[1])
        texts_ECB.append(DES_ECB(bitText_ECB[k*64 : (k+1)*64], keys[i], 0))
      #进入CBC解密运算
      for k in range(int(len(bitText_CBC)/64)):
        if k == 0:
          texts_CBC.append(DES_CBC(bitText_CBC[k * 64: (k + 1) * 64], keys[i], 0, bitIV[i]))
        else:
          print(texts_CBC[k-1])
          texts_CBC.append(DES_CBC(bitText_CBC[k * 64: (k + 1) * 64], keys[i], 0, bitText_CBC[(k-1)*64:k*64]))

    #写入des_decrypted.txt文件
    Mresult_ECB = ''
    Mresult_CBC = ''
    with open('des_decrypted.txt', 'w') as f:
      for each in texts_ECB:
        Mresult_ECB = Mresult_ECB + each
      f.write(ascii2char(HEX2ascii(Mresult_ECB)))
      f.write('\n')
      for each in texts_CBC:
        Mresult_CBC = Mresult_CBC + each
      f.write(ascii2char(HEX2ascii(Mresult_CBC)))

if __name__ == '__main__':
    main()
