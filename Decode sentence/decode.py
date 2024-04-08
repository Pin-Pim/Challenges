def decode(message_file):
  dictionary = {}
  wordList = []
  with open(message_file, 'r') as file:
    lines = [line.strip() for line in file.readlines()]
    for line in lines:
      wordList.append(line)
  wordList = sorted(wordList)
  wordList = [item.split() for item in wordList]
  dictionary = {num: word for num, word in wordList}
  i = 1
  ii = 2
  final = []
  while i <= 300:
    final.append(dictionary[str(i)])
    i += ii
    ii += 1
  return ' '.join(final)

decode('code.txt')