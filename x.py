for i in range(1, 100):
  result = ''
  i_bin = bin(i)[2:]
  if i % 2 != 0:
    result = '10' + i_bin[:-2] + '01'
  else:
    result = '11' + i_bin[2:] + '1'
  final_result = int(result, 2)
  if i >= 42:
    print(i, i_bin, result, final_result)
