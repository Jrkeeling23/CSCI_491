
class Terms:
    def __init__(self,list_of_words):
        self.terms = list_of_words
        print(self.terms.sort())

def main():
    words = "to do is to be to be is to do to be or not to be I am what I am I think therefore I am do be do be do do do do da da da let it be let it be"
    print(sorted(words.split()))

    Terms(words.split())

if __name__ is "__main__":
    main()
main()