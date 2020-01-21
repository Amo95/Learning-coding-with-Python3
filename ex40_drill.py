class Song(object):
  """docstring for Song"""
  def __init__(self, lyrics):
    self.lyrics = lyrics

  def sec_lyric(self):
    for line in self.lyrics:
      print(line)

fireboy_song = Song([
  "Know one can love you",
  "Like I do",
  "Blaming nobody\n"
  ])

my_song = Song([
  "Hello, Its me",
  "How you doing girl",
  "No one can love you boo"
  ])

def main():
  fireboy_song.sec_lyric()
  my_song.sec_lyric()

if __name__ == '__main__':
  main()
