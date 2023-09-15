from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Not(And(AKnight, AKnave)),  # cannot be knight and knave at the same time
    Or(AKnight, AKnave),         # will be Knight or Knave
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Not(And(AKnight, AKnave)),  # cannot be knight and knave at the same time
    Or(AKnight, AKnave),         # will be Knight or Knave
    Not(And(BKnight, BKnave)),  # cannot be knight and knave at the same time
    Or(BKnight, BKnave),         # will be Knight or Knave
    Implication(AKnight,And(AKnave,BKnave)),
    Implication(AKnave,Not(And(AKnave,BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Not(And(AKnight, AKnave)),  # cannot be knight and knave at the same time
    Or(AKnight, AKnave),         # will be Knight or Knave
    Not(And(BKnight, BKnave)),  # cannot be knight and knave at the same time
    Or(BKnight, BKnave),         # will be Knight or Knave
    Implication(AKnight,Or(And(AKnave,BKnave),And(AKnight,BKnight))),
    Implication(AKnave,Not(Or(And(AKnave,BKnave),And(AKnight,BKnight)))),
    Implication(BKnight,Or(And(AKnave,BKnight),And(AKnight,BKnave))),
    Implication(BKnave,Not(Or(And(AKnave,BKnight),And(AKnight,BKnave))))
)

# Puzzle 3 # A says either "I am a knight." or "I am a knave.", but you don't know which. 
# B says "A said 'I am a knave'." # B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Not(And(AKnight, AKnave)),  # cannot be knight and knave at the same time
    Or(AKnight, AKnave),         # will be Knight or Knave
    Not(And(BKnight, BKnave)),  # cannot be knight and knave at the same time
    Or(BKnight, BKnave),         # will be Knight or Knave
    Not(And(CKnight, CKnave)),  # cannot be knight and knave at the same time
    Or(CKnight, CKnave),         # will be Knight or Knave
    Or(
        # "I am a knight."
        And(
            Implication(AKnight, AKnight),
            Implication(AKnave, Not(AKnight))
        ),
        
        # "I am a knave."
        And(
            Implication(AKnight, AKnave),
            Implication(AKnave, Not(AKnave))
        )
    ),

    Not(And(
        # "I am a knight."
        And(
            Implication(AKnight, AKnight),
            Implication(AKnave, Not(AKnight))
        ),
        
        # "I am a knave."
        And(
            Implication(AKnight, AKnave),
            Implication(AKnave, Not(AKnave))
        )
    )),

    Implication(BKnight,And(Implication(AKnight,AKnight),Implication(AKnave,Not(AKnave)))),
    Implication(BKnave,Not(And(Implication(AKnight,AKnight),Implication(AKnave,Not(AKnave))))),
    Implication(BKnight,CKnave),
    Implication(BKnave,CKnight),
    Implication(CKnight,AKnight),
    Implication(CKnave,AKnave),
)
def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2), ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
