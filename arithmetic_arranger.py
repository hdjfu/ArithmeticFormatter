def arithmetic_arranger(problems, respostas= False):

    if(len(problems) > 5):
      return 'Error: Too many problems.'
    line1 = ''
    line2 = ''
    finalLine1 = ''
    finalLine2 = ''
    finalLine3 = ''
    finalLine4 = ''

    for conta in problems:
      elementos = conta.split()

      if elementos[1] != '+' and elementos[1] != '-':
        return "Error: Operator must be '+' or '-'."
      if len(elementos[0]) > 4 or len(elementos[2]) > 4 :
        return 'Error: Numbers cannot be more than four digits.'
      if elementos[0].isdigit() == False or elementos[2].isdigit() == False:
        return 'Error: Numbers must only contain digits.'
      
      line1 = elementos[0]
      line2 = elementos[2]
      if elementos[1] == '+':
        line4 = str(int(elementos[0]) + int(elementos[2]))
      else:
        line4 = str(int(elementos[0]) - int(elementos[2]))
      
      maxSize = max(len(line1)+2, len(line2)+2, len(line4) +1)
      line2 = line2.rjust(maxSize)
      line2 = elementos[1] + line2[1:]
      finalLine1 += line1.rjust(maxSize) + '    '
      finalLine2 += line2 + '    '
      finalLine3 += '-' * (maxSize) + '    '
      finalLine4 += line4.rjust(maxSize) + '    '
        
    
    arranged_problems = finalLine1.rstrip() + '\n' + finalLine2.rstrip() + '\n' + finalLine3.rstrip()
    if respostas:
      arranged_problems += '\n' + finalLine4.rstrip()
      

    return arranged_problems