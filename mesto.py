# -*- coding: UTF-8 -*-

from mesta_seznam import state_capitals
import random

incorrect_answers = []

print "Nauči se glavna mesta držav!\n\n"


while len(state_capitals)>0:
        izbira = random.choice(state_capitals.keys())
        correct_answer = state_capitals.get(izbira)

        print "Katero je glavno mesto", izbira, "?"
        answer=raw_input("# ")
        if answer.lower() == correct_answer.lower():
            print "Odgovoril si pravilno!\n"
            del state_capitals[izbira]
        else:
            print "Napačen odgovor."
            print "Pravilen odgovor je",correct_answer
            incorrect_answers.append(izbira)

