import nltk
import random
english_vocab_five = []


def main():
    # english_vocab is a list with 234,377 words. It includes proper nouns too.
    # For loop creates a variable english_vocab_five which only calls the five letter words in english_vocab.
    english_vocab = list(w.upper() for w in nltk.corpus.words.words())
    for w in english_vocab:
        if len(w) == 5:
            english_vocab_five.append(w)
    wordle = random.choice(english_vocab_five)
    #print(wordle)
    input1 = input("Guess the word: ").upper()
    if len(input1) != 5:
        print("Sorry, only 5 letter words accepted. Try again")
        return
    output,finish = compare(input1, wordle)
    print(output)
    if finish == True:
        print("Congrats, you guessed the word!")
        return

    input2 = input("Guess the word: ").upper()
    if len(input2) != 5:
        print("Sorry, only 5 letter words accepted. Try again")
        return
    output,finish = compare(input2, wordle)
    print(output)
    if finish == True:
        print("Congrats, you guessed the word!")
        return

    input3 = input("Guess the word: ").upper()
    if len(input3) != 5:
        print("Sorry, only 5 letter words accepted. Try again")
        return
    output,finish = compare(input3, wordle)
    print(output)
    if finish == True:
        print("Congrats, you guessed the word!")
        return

    input4 = input("Guess the word: ").upper()
    if len(input4) != 5:
        print("Sorry, only 5 letter words accepted. Try again")
        return
    output,finish = compare(input4, wordle)
    print(output)
    if finish == True:
        print("Congrats, you guessed the word!")
        return

    input5 = input("Guess the word: ").upper()
    if len(input5) != 5:
        print("Sorry, only 5 letter words accepted. Try again")
        return
    output,finish = compare(input5, wordle)
    print(output)
    if finish == True:
        print("Congrats, you guessed the word!")
        return

    input6 = input("Guess the word: ").upper()
    if len(input6) != 5:
        print("Sorry, only 5 letter words accepted. Try again")
        return
    output,finish = compare(input6, wordle)
    print(output)
    if finish == True:
        print("Congrats, you guessed the word!")
        return

    print("Sorry, try again. The word was " + wordle)


def compare(input1, wordle):
    output = []
    finish = input1 == wordle


    if input1[0] == wordle[0]:
        output.append(input1[0]+"*")
    elif input1[0] in wordle:
        output.append(input1[0]+"?")
    else:
        output.append(input1[0])

    if input1[1] == wordle[1]:
        output.append(input1[1]+"*")
    elif input1[1] in wordle:
        output.append(input1[1]+"?")
    else:
        output.append(input1[1])

    if input1[2] == wordle[2]:
        output.append(input1[2]+"*")
    elif input1[2] in wordle:
        output.append(input1[2]+"?")
    else:
        output.append(input1[2])

    if input1[3] == wordle[3]:
        output.append(input1[3]+"*")
    elif input1[3] in wordle:
        output.append(input1[3]+"?")
    else:
        output.append(input1[3])

    if input1[4] == wordle[4]:
        output.append(input1[4]+"*")
    elif input1[4] in wordle:
        output.append(input1[4]+"?")
    else:
        output.append(input1[4])

    return(output, finish)


if __name__ == "__main__":
    main()
