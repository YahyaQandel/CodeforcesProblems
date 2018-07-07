import string


class NAM:
  def __init__(self):
      self.pivot = 'a'
      self.rotations = 0

  def get_char_index(self,selected_char):
      assert isinstance(selected_char, object)
      return alphabet.index(selected_char)

  def shortest_diff(self,selected_char):
      diff=0
      diff = abs(self.get_char_index(self.pivot) - self.get_char_index(selected_char))
      if diff <= 13:
          # print('less than 13')
          clockwise = abs(self.get_char_index(self.pivot) - self.get_char_index(selected_char))
      else:
          if self.pivot == 'a':
              clockwise = len(alphabet) - self.get_char_index(selected_char)
          else:
              if self.get_char_index(self.pivot) > 13:
                clockwise = abs(len(alphabet) - self.get_char_index(self.pivot)) + self.get_char_index(selected_char)
              else:
                clockwise = abs(len(alphabet) - self.get_char_index(selected_char)) + self.get_char_index(self.pivot)
      return clockwise

  def total_rotations(self,word):
      for j in word:
          self.rotations +=self.shortest_diff(j)
          # self.rotations += self.get_length(j)
          self.pivot=j
      return self.rotations


alphabet = list(string.ascii_lowercase)


nam = NAM()
print(nam.total_rotations(input()))
