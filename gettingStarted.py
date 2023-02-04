### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    #Students do not have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.
    if question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted " \
                     "by a TA?":
        answer = "mTCP"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "No"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question == "What is the SHA256 hashing value to the following message: 'NYU Computer Networking' " \
                     "- Use SHA256 hash generator and use the answer in your code":
        answer = "883c13da6a24949c9a23231b60119e2ace58459da4f8bbdd812cc37764548bdd"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an " \
                     "integer number":
        answer = "7"
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an " \
                     "integer number":
        answer = "3"
    else:
        ### you should understand why this else case should be included
        ### what happens if there is a typo in one of the questions?
        ### maybe put something here to flag an issue
        answer = "There is a typo in the question, please revisit your question."
    return answer
# Complete all the questions.


if __name__ == "__main__":
    #use this space to debug and verify that the program works
    debug_question_1 = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question_1))

    debug_question_2 = "Is it possible to decrypt a message without a key? - Yes/No"
    print(welcome_assignment_answers(debug_question_2))

    debug_question_3 = "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?"
    print(welcome_assignment_answers(debug_question_3))

    debug_question_4 = "Is it possible to decode a message without a key? - Yes/No"
    print(welcome_assignment_answers(debug_question_4))

    debug_question_5 = "Is a hashed message supposed to be un-hashed? - Yes/No"
    print(welcome_assignment_answers(debug_question_5))

    debug_question_6 = "What is the SHA256 hashing value to the following message: 'NYU Computer Networking' " \
                     "- Use SHA256 hash generator and use the answer in your code"
    print(welcome_assignment_answers(debug_question_6))

    debug_question_7 = "Is MD5 a secured hashing algorithm? - Yes/No"
    print(welcome_assignment_answers(debug_question_7))

    debug_question_8 = "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an " \
                     "integer number"
    print(welcome_assignment_answers(debug_question_8))

    debug_question_9 = "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an " \
                     "integer number"
    print(welcome_assignment_answers(debug_question_9))


#Questions:
#"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
#"Are encoding and encryption the same? - Yes/No":
#"Is it possible to decrypt a message without a key? - Yes/No":
#"Is it possible to decode a message without a key? - Yes/No":
#"Is a hashed message supposed to be un-hashed? - Yes/No":
#"What is the SHA256 hashing value to the following message: 'NYU Computer Networking' - Use SHA256 hash generator and use the answer in your code":
#"Is MD5 a secured hashing algorithm? - Yes/No":
#"What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
#"What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":