import random


class Arcade:

    def __init__(self):
        self.name = "User"
        self.score_star = 1000
        self.score_cb = 1000
        self.score_rpsw = 0
        self.score_rpsl = 0
        self.score_hmw = 0
        self.score_hml = 0

    def cows_and_bulls(self):
        def cowbull():
            return f"{random.randint(0, 9999):04}"

        print("""*.:｡✿*ﾟ’ﾟ･✿.｡.:* *.:｡✿*ﾟ¨ﾟ✎･ ✿.｡.:* *.:｡✿*ﾟ¨ﾟ
               COWS AND BULLS
*.:｡✿*ﾟ’ﾟ･✿.｡.:* *.:｡✿*ﾟ¨ﾟ✎･ ✿.｡.:* *.:｡✿*ﾟ¨ﾟ
type RULES to view the rules of Cows and Bulls
            or start guessing
        """)

        mode = "number"
        game = True
        rules = """
*.:｡✿*ﾟ’ﾟ･✿.｡.:* *.:｡✿*ﾟ¨ﾟ✎･ ✿.｡.:* *.:｡✿*ﾟ¨ﾟ
A random 4-digit number will be generated, to win you must
guess it. If a digit in your guess is correct and in the right
place, you'll get a bull. If the digit is correct but in the
wrong place, you'll get a cow.

             EXAMPLE1: (1433)
             》3425
             Cows: 1  Bulls: 1

             EXAMPLE2: (4567)
             》4576
             ⬤⬤○○

In EXAMPLE1, 3 exists in the number, but isn't in the correct
place, thus a cow. 4 is in the right spot - a bull. 2 and 5
give nothing, because they are not in the number at all.
In EXAMPLE2, 4 and 5 are in the right places - two bulls
(filled-in circle), but 6 and 7 are switched, so they are two
cows (empty circles).

For circle-mode type "circle". You can switch back to
number-mode anytime by typing "number".
*.:｡✿*ﾟ’ﾟ･✿.｡.:* *.:｡✿*ﾟ¨ﾟ✎･ ✿.｡.:* *.:｡✿*ﾟ¨ﾟ
        """

        while game:
            num = cowbull()
            tries = 0
            print("""
          *.:｡✿*ﾟGame on!ﾟ･✿.｡.:*
            """)
            while True:

                cows = 0
                bulls = 0
                resc = ""
                resb = ""

                guess = input("》").strip().replace(" ", "").strip().lower()

                guess_l = list(guess)
                cl = list(num)

                if guess == "cheat":
                    print(num)
                    continue
                elif guess == "rules":
                    print(rules)
                    print("""
          *.:｡✿*ﾟGame on!ﾟ･✿.｡.:*
                    """)
                    continue
                elif guess == "circle":
                    mode = "circle"
                    print("Switched to circle-mode.")
                    continue
                elif guess == "number":
                    mode = "number"
                    print("switched to number-mode.")
                    continue

                if len(guess) != 4 or not guess.isdigit():
                    print("Guess must be a 4-digit number.")
                    continue

                if guess_l == cl:
                    if tries < self.score_cb:
                        self.score_cb = tries
                    print(f"\nYou win!!! °˖✧◝(⁰▿⁰)◜✧˖° It took you {tries} {'tries' if tries != 1 else 'try'}!"
                          f"\nHigh score: {self.score_cb}")
                    yn = input("Wanna play again? ◝(•ω•`)o\n").lower().strip()
                    if yn == "no":
                        print("\nBye bye!! (*＾▽＾)／")
                        game = False
                        break
                    else:
                        break

                for n, i in enumerate(guess_l):
                    if guess[n] == num[n]:
                        bulls += 1
                        cl[n] = "x"
                        guess_l[n] = "x"
                for n, i in enumerate(guess_l):
                    if i in cl and i != "x":
                        cows += 1
                        cl[cl.index(i)] = "x"
                        guess_l[guess_l.index(i)] = "x"

                tries += 1

                if mode == "number":
                    print(f"Cows: {cows}  Bulls: {bulls}  Tries: {tries}")
                else:
                    for n in range(0, bulls):
                        resb += "⬤"
                    for n in range(0, cows):
                        resc += "○"
                    print(f"{resb}{resc}   Tries: {tries}")

    def rock_paper_scissors(self):
        print("""┏━━━━━━      ༻❁༺      ━━━━━━┓
     Rock Paper Scissors
┗━━━━━━      ༻❁༺      ━━━━━━┛
type RULES to view the rules
        """)

        beg = input("•• ━━ Press enter to start ━━ ••\n").lower().strip()

        rules = """
      •• ━━━━━ ༻❁༺ ━━━━━ ••
Pick paper, scissors, or rock to start.
The game will also pick one and tell
you if you won. 

         Paper 》 Rock
         Rock 》 Scissors
         Scissors 》 Paper

Good luck! (*＾▽＾)／
      •• ━━━━━ ༻❁༺ ━━━━━ ••
        """
        while beg == "rules":
            print(rules)
            beg = input("•• ━━ Press enter to start ━━ ••\n").lower().strip()

        opt = ["rock", "paper", "scissors"]

        while True:

            player1 = input(f"""
•• ━━━━━ ༻❁ {self.name.upper()} ❁༺ ━━━━━ ••
    》rock
    》paper
    》scissors
    """).lower().strip()
            player2 = random.choice(opt)
            print(f"""
•• ━━━━━ ༻❁ GAME ❁༺ ━━━━━ ••
    》{player2}""")

            if player1 == "rules" or beg == "rules":
                print(rules)
            elif player1 == player2:
                print("\nWe tied!!! （・□・；）")
            elif player1 == "scissors":
                if player2 == "rock":
                    self.score_rpsl += 1
                    print(f"\nI beat you!! (≧∇≦)/!\nWins: {self.score_rpsw} Losses: {self.score_rpsl}")
                else:
                    self.score_rpsw += 1
                    print(f"\n{self.name} wins! Congrats!! °˖✧◝(⁰▿⁰)◜✧˖°\nWins: {self.score_rpsw}"
                          f" Losses: {self.score_rpsl}")
            elif player1 == "rock":
                if player2 == "paper":
                    self.score_rpsl += 1
                    print(f"\nI beat you!! (≧∇≦)/!\nWins: {self.score_rpsw} Losses: {self.score_rpsl}")
                else:
                    self.score_rpsw += 1
                    print(f"\n{self.name} wins! Congrats!! °˖✧◝(⁰▿⁰)◜✧˖°\nWins: {self.score_rpsw}"
                          f" Losses: {self.score_rpsl}")
            elif player1 == "paper":
                if player2 == "scissors":
                    self.score_rpsl += 1
                    print(f"\nI beat you!! (≧∇≦)/!\nWins: {self.score_rpsw} Losses: {self.score_rpsl}")
                else:
                    self.score_rpsw += 1
                    print(f"\n{self.name} wins! Congrats!! °˖✧◝(⁰▿⁰)◜✧˖°\nWins: {self.score_rpsw}"
                          f" Losses: {self.score_rpsl}")
            else:
                print("I don't understand!!! (๑･`▱´･๑)")

            print()
            replay = input("""•• ━━━━━ ༻❁ Want another go? ❁༺ ━━━━━ •• 
》 Yes
》 No
""").lower().strip()

            if replay == "no":
                print("\nBye bye!! (*＾▽＾)／")
                break

    def star(self):

        print("""╔═══*.·:·.☽✧    ✦    ✧☾.·:·.*═══╗
               STAR
╚═══*.·:·.☽✧    ✦    ✧☾.·:·.*═══╝
  type RULES to view the rules
  """)

        rules = """
          ═══════☆═══════
Think of a number between 1 and 10 and, when you're ready, 
press enter! The game will start guessing and you can reply 
'less' if the number is bigger than the one you picked and
'more' if it is smaller. Once the game guesses correctly type 
'star'.
          ═══════☆═══════

        """
        game = True
        beg = input(".·:·.☽✧ Press enter to start!✧☾.·:·.*\n").strip().lower()
        tries = 1

        while beg == "rules":
            print(rules)
            beg = input(".·:·.☽✧ Press enter to start!✧☾.·:·.*\n").strip().lower()

        while game:
            nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            print("")
            while True:
                guess = random.choice(nums)

                print(guess)
                answ = input("»•» ").strip().lower()

                if answ == "rules":
                    print(rules)
                    input(".·:·.☽✧ Press enter to start!✧☾.·:·.*\n").strip().lower()
                    continue
                elif answ == "star":
                    if tries < self.score_star:
                        self.score_star = tries
                    print(f"\nHehe, yay!! °˖✧◝(⁰▿⁰)◜✧˖° Took me {tries} {'tries' if tries > 1 else 'try'}!\n"
                          f"High score: {self.score_star}")
                    yn = input("Wanna play again? ◝(•ω•`)o\n").lower().strip()
                    if yn == "no":
                        print("\nBye bye!! (*＾▽＾)／")
                        game = False
                        break
                    else:
                        tries = 0
                        break
                elif answ == "less":
                    nums = nums[:nums.index(guess)]
                elif answ == "more":
                    nums = nums[nums.index(guess):]
                    nums.remove(guess)
                else:
                    print("I don't understand!! (͒˃̩̩⌂˂̩̩ ͒)")
                    continue

                tries += 1

                if not nums:
                    tries = 0
                    print(f"{chr(72)}{chr(101)}{chr(121)}!!! {chr(89)}{chr(111)}{chr(117)}{chr(39)}{chr(114)}{chr(101)}"
                          f" {chr(99)}{chr(104)}{chr(101)}{chr(97)}{chr(116)}{chr(105)}{chr(110)}{chr(103)}! (๑•̀ㅁ•́๑)")
                    break

    def hangman(self):
        wordbank = ["gift", "flag", "systematic", "constraint", "species", "outfit", "boot", "background", "glasses",
                    "carry",
                    "hole", "bite", "vegetation", "leg", "divorce", "try", "trench", "underline", "cow", "glacier",
                    "prayer",
                    "rebellion", "unfair", "legislature", "profession", "growth", "theory", "forward", "neck", "cheek",
                    "captain", "resist", "corner", "adjust", "fit", "drive", "restaurant", "familiar", "cheat",
                    "preparation",
                    "stage", "clerk", "knife", "award", "sell", "murder", "destruction", "palace", "advocate", "reduce",
                    "cake", "effect", "cattle", "pavement", "association", "eagle", "clerk", "depart", "side",
                    "program",
                    "object", "statement", "quarrel", "solid", "theorist", "writer", "hell", "tract", "witch", "makeup",
                    "refrigerator", "light", "frown", "unlike", "contemporary", "sniff", "weed", "tourist", "active",
                    "station", "arise", "basketball", "director", "population", "change", "rush", "tough", "chorus",
                    "hike",
                    "rain", "staircase", "gain", "misery", "bee", "revolution", "colony", "shot", "bird", "company",
                    "leaf",
                    "evaluate", "concentration", "north", "scrap", "dive", "photograph", "printer", "print", "bill",
                    "colorful",
                    "fog", "counter", "cower", "register", "storm", "shadow", "betray", "credibility", "physics",
                    "study",
                    "gallon", "deficiency", "writer", "claim", "progressive", "vision", "remain", "officer", "aid",
                    "white",
                    "volcano", "menu", "timber", "alive", "guilt", "chapter", "philosophy", "traction", "pumpkin",
                    "hate",
                    "criticism", "homosexual", "feign", "launch", "patch", "private", "month", "integrity", "ample",
                    "full"
                    ]

        reset = wordbank

        rules = """
   • ══════════════════ •
The game will choose a random word 
and display the amount of letters it has 
in form of hearts. You have 10 tries to 
guess the word or single letters from it. 
Each time you guess correctly, the letter 
will be revealed in its correct position.
If you are wrong, your guesses will go down 
by one. If you use up all of them without 
having gotten the word - you lose. You 
win if you correctly guess the word.
   • ══════════════════ •"""

        print("""╔═══━━━─── • ───━━━═══╗ 
        HANGMAN
╚═══━━━─── • ───━━━═══╝""")
        play = input("""  type RULES or press
   enter to start
        """).lower().strip()

        if play == "rules":
            print(rules)

        while True:
            win = random.choice(wordbank)
            wordbank.remove(win)

            if not wordbank:
                wordbank = reset

            word = list(win)
            wrong = 10
            guessed_letters = ""
            board = list(len(word) * "♡")

            print()
            print("".join(board))
            print(f"Guesses left: {wrong}")

            while True:
                guess = input("Guess a letter: ").lower()

                if guess == "rules":
                    print(rules)
                elif not guess.isalpha() or len(guess) != len(win) and len(guess) != 1:
                    print("\nGuess must be a letter or the word!")
                elif guess in word:
                    for ind, letter in enumerate(word):
                        if letter == guess:
                            board[ind] = word[ind]
                            word[ind] = "#"
                elif guess in guessed_letters or guess in board:
                    print("\nAlready guessed this letter.")
                elif guess not in word and guess != win:
                    print("\nWrong guess!")
                    wrong -= 1
                    if wrong == 0:
                        self.score_hml += 1
                        print("\nYou lose! (͒˃̩̩⌂˂̩̩ ͒)")
                        print(f"Word was: {win}")
                        print(f"Wins: {self.score_hmw} Losses: {self.score_hml}")
                        break
                    if len(guess) == 1:
                        guessed_letters += f"{guess}" if not guessed_letters else f", {guess}"

                if guess == win or "♡" not in board:
                    self.score_hmw += 1
                    print("\nCongratulations, you win! °˖✧◝(⁰▿⁰)◜✧˖°")
                    print(f"Word was: {win}")
                    print(f"Wins: {self.score_hmw} Losses: {self.score_hml}")
                    break

                print()
                print("".join(board))
                print(f"Guesses left: {wrong} • Guessed letters: {guessed_letters}")

            yn = input("\nWanna play again? ◝(•ω•`)o\n").lower().strip()
            if yn == "no" or yn == "n":
                print("\nBye bye!! (*＾▽＾)／")
                break


def main():
    my_arcade = Arcade()

    print("""╔═══°∴,*⋅✲══〖✰〗══✲⋅*,∴°═══╗
         A R C A D E
╚═══°∴,*⋅✲══〖✰〗══✲⋅*,∴°═══╝

   Welcome to the arcade!
    """)
    name = input("•• ━━ What's your name? ━━ ••\n").title()
    my_arcade.name = name

    while True:
        game_pick = input("""
•• ━━ Type in the number of the game you'd 
like to play or type 'exit' to leave ━━ ••

»[1] Cows and Bulls
»[2] Rock Paper Scissors
»[3] Star
»[4] Hangman

""").strip().lower()

        if game_pick == "1":
            print()
            my_arcade.cows_and_bulls()
        elif game_pick == "2":
            print()
            my_arcade.rock_paper_scissors()
        elif game_pick == "3":
            print()
            my_arcade.star()
        elif game_pick == "4":
            print()
            my_arcade.hangman()
        elif game_pick == "exit":
            break
        else:
            print("Huh?")


if __name__ == '__main__':
    main()
