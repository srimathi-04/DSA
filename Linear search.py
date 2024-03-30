
def locate_cards(cards,query):
  position = 0
  print("position:",position)

  while position < len(cards):
    if cards[position] == query:
      return position
    position +=1
  return -1
cards=[]
card = [19,18,14,13,12,7,3,1,5]
query = 3
print("cards:",cards)
print("query:",query)
print("position of the card is:",locate_cards(cards,query))
print("position of the card is:",locate_cards(card,query))