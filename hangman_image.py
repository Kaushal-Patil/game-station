def hangman_func(index):
   '''
   This function returns the hangman is different forms based on the integer input passed into the funtion
   Returns : An ascii art of hangman
   Rtype   : String
   '''
   hangman_pic = ['''
    +-----+
       |  |
          |
          |
          |
          |
    +----+|
    ''',
    '''
    +-----+
       |  |
       O  |
          |
          |
          |
    +----+|
    ''',
    '''
    +-----+
       |  |
       O  |
       |  |
          |
          |
    +----+|
    ''',
    '''
    +-----+
       |  |
       O  |
      /|  |
          |
          |
    +----+|
    ''',
    '''
    +-----+
       |  |
       O  |
      /|\\ |
          |
          |
    +----+|
    ''',
    '''
    +-----+
       |  |
       O  |
      /|\\ |
      /   |
          |
    +----+|
    ''',
    '''
    +-----+
       |  |
       O  |
      /|\\ |
      / \\ |
          |
    +----+|
    ''']

   return hangman_pic[index]




