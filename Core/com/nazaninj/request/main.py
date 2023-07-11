from collections import deque


def bfs_word_transform(start_word, end_word, word_list):
  if end_word not in word_list:
    return "کلمه‌ی هدف در لیست وجود ندارد"

  visited = set()
  queue = deque([(start_word, [start_word])])

  while queue:
    current_word, path = queue.popleft()
    visited.add(current_word)

    if current_word == end_word:
      return "[+] {data}".format(data=' -> '.join(path))

    for i in range(len(current_word)):
      for char in 'abcdefghijklmnopqrstuvwxyz':
        if char == current_word[i]:
          continue
        new_word = current_word[:i] + char + current_word[i + 1:]
        if new_word in word_list and new_word not in visited:
          queue.append((new_word, path + [new_word]))

  return "هیچ مسیری برای تبدیل وجود ندارد"


if __name__ == '__main__':
  # مثال اول
  word_list = ['cord', 'cat', 'card', 'candidate', 'ward', 'warm']
  start_word = 'cold'
  end_word = 'warm'
  result = bfs_word_transform(start_word, end_word, word_list)
  print(result)

  # مثال دوم
  word_list = ['hot', 'dot', 'dog', 'cog']
  start_word = 'hit'
  end_word = 'cog'
  result = bfs_word_transform(start_word, end_word, word_list)
  print(result)
