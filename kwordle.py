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

    for guessNumber in range(0,6):
        userInput = input("Guess the word: ").upper()
        if len(userInput) != 5:
            print("Sorry, only 5 letter words accepted. Try again")
            return
        output,finish = compare(userInput, wordle)
        print(output)
        if finish == True:
            print("Congrats, you guessed the word!")
            return

    print("Sorry, try again. The word was " + wordle)


def compare(input1, wordle):
    output = []
    finish = input1 == wordle

    for ix in [0,1,2,3,4]:
        if input1[ix] == wordle[ix]:
            output.append(input1[ix]+"*")
        elif input1[ix] in wordle:
            output.append(input1[ix]+"?")
        else:
            output.append(input1[ix])
    
    return(output, finish)


if __name__ == "__main__":
    main()
