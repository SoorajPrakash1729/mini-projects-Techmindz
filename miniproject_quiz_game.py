def newgame():#FUNCTION FOR HOW THE GAME WORKS
    your_ans_list=[]
    scores_of_ans=0
    quest_no=1
    print("welcome to the quiz..all the best..!!")
    for key in questions:
        print('-------------------------------------------------------')
        print(key)
        for i in options[quest_no-1]:
            print(i)
        your_ans=input('enter (A , B , C or D):')
        your_ans=your_ans.upper()
        your_ans_list.append(your_ans)
        scores_of_ans+=check_ans(questions.get(key),your_ans)#COMPARING THE CORRECT OPTION (VALUES OF THE DICTIONARY) AND THE OPTION YOU GIVE and Storing it in Correct Ans
        quest_no+=1
    displayscore(scores_of_ans,your_ans_list)

def check_ans(answer,your_ans):#FUNCTION FOR CHECKING OPTIONS--THAT ACTUAL OPE
    if answer==your_ans:
        print('CORRECT!!')
        return 1# WE NEED RETURN VALUES O AND 1 INORDER TO COUNT THE MARKS
    else:
        print("WRONG!!, the answer is:",answer)
        return 0
def displayscore(scores_of_ans,your_ans_list):
    print('-------------------------------------------------------')
    print('RESULTS..!!')
    print("Actual answers: ",end=" ")
    for i in questions:
        print(questions.get(i),end=' ')
    print()
    print("  Your answers: ",end=' ')
    for i in your_ans_list:
        print(i,end=' ')
    score=int((scores_of_ans/len(questions))*100)
    print()
    print(' Your score is: ',score,'%')

def play_again():
    reply=input("Do you want to play again? (yes or no): ")
    reply=reply.upper()
    if reply=='YES':
        return True
    else:
        return False
    
questions = {
    "What is the capital of France?": "C",
    "Which planet is known as the Red Planet?": "A",
    "Who wrote 'Romeo and Juliet'?": "A",
    "What is the largest ocean on Earth?": "C",
    "In which year did World War II end?": "C",
    "Who is the author of 'To Kill a Mockingbird'?": "B",
    "What is the currency of Japan?": "B",
    "Which country is known as the Land of the Rising Sun?": "C",
    "Who painted the Mona Lisa?": "B",
    "What is the square root of 144?": "A",
    "Which is the largest mammal in the world?": "B",
    "In which year did Christopher Columbus reach the Americas?": "A",
    "What is the main component of the Earth's atmosphere?": "A",
    "Who is known as the 'Father of Computers'?": "B",
    "Which famous scientist developed the theory of general relativity?": "B",
    "How many continents are there in the world?": "C",
    "Which element has the chemical symbol 'O'?": "B",
    "Who was the first woman to win a Nobel Prize?": "A",
    "What is the capital of Australia?": "C",
    "In which year did India gain independence?": "B"
                                                      }

options = [
    ["A. London", "B. Berlin", "C. Paris", "D. Rome"],
    ["A. Mars", "B. Jupiter", "C. Venus", "D. Saturn"],
    ["A. William Shakespeare", "B. Jane Austen", "C. Charles Dickens", "D. Mark Twain"],
    ["A. Atlantic Ocean", "B. Indian Ocean", "C. Pacific Ocean", "D. Arctic Ocean"],
    ["A. 1943", "B. 1944", "C. 1945", "D. 1946"],
    ["A. J.K. Rowling", "B. Harper Lee", "C. George Orwell", "D. J.R.R. Tolkien"],
    ["A. Won", "B. Yen", "C. Euro", "D. Dollar"],
    ["A. China", "B. South Korea", "C. Japan", "D. Vietnam"],
    ["A. Michelangelo", "B. Leonardo da Vinci", "C. Vincent van Gogh", "D. Pablo Picasso"],
    ["A. 12", "B. 14", "C. 16", "D. 18"],
    ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. African Elephant"],
    ["A. 1492", "B. 1498", "C. 1500", "D. 1505"],
    ["A. Nitrogen", "B. Oxygen", "C. Carbon Dioxide", "D. Hydrogen"],
    ["A. Alan Turing", "B. Charles Babbage", "C. Ada Lovelace", "D. Bill Gates"],
    ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Nikola Tesla"],
    ["A. 5", "B. 6", "C. 7", "D. 8"],
    ["A. Gold", "B. Oxygen", "C. Iron", "D. Silver"],
    ["A. Marie Curie", "B. Rosalind Franklin", "C. Dorothy Crowfoot Hodgkin", "D. Mother Teresa"],
    ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Perth"],
    ["A. 1945", "B. 1947", "C. 1948", "D. 1950"]
]

newgame()
while play_again():
    newgame()
print('see you next time..bye..!')


