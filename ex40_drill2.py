class MySong(object):
  """doctstring for MySong"""
  def __init__(self, lyric):
    self.lyric = lyric

  def sing_me_a_song(self):
    for line in self.lyric:
      print(line)

intro = [
    "\nINTRO\nI can swallow a bottle of alcohol and I'll feel like Godzilla\nBetter hit the deck like the card dealer",
    "My whole squad's in here, walking around the party",
    "A cross between a zombie apocalypse and big Bobby \"The",
    "Brain\" Heenan which is probably the",
    "Same reason I wrestle with mania",
    "Shady's in this bitch, I'm posse'd up",
    "Consider it to cross me a costly mistake",
    "If they sleepin' on me, the hoes better get insomnia",
    "ADHD, hydroxycut",
    "Pass the Courvoisi' (Hey, hey)",
    "In AA with an AK, melee, finna set it like a playdate",
    "Better vacate, retreat like a vacay, mayday",
    "This beat is cray-cray, Ray J, H-A-H-A-H-A",
    "Laughing all the way to the bank, I spray flings",
    "They cannot tame or placate the"
    ]

chorus = [
    "\nCHORUS\nMonster",
    "You get in my way, I'ma feed you to the monster (Yeah)",
    "I'm normal during the day, but at night, turn to a monster (Yeah)",
    "When the moon shines like Ice Road Truckers",
    "I look like a villain outta those blockbusters",
    "Godzilla, fire spitter, monster",
    "Blood on the dance floor, and on the Louis V carpet",
    "Fire, Godzilla, fire, monster",
    "Blood on the dance floor, and on the Louis V carpet"
    ]

def main():
  eminem_godzilla_verse1 = MySong(intro)
  juicewrld_chorus = MySong(chorus)

  eminem_godzilla_verse1.sing_me_a_song()
  juicewrld_chorus.sing_me_a_song()

if __name__ == "__main__":
  main()
