def normalize_text(text):
    return text.lower().strip()

def split_text(text):
    return text.split()  #dy funksione që e kthejnë tekstin në lowercase dhe i heq hapësirat e panevojshme. dhe funksioni tjetër e ndan tekstin në fjalë

book---cipher---core

 main
def create_index(book_text):
    words = book_text.lower().split
    index = {}
    
    for i, word in enumerate(words):
        if word not in index:
            index[word] = []
        index[word].append(i)
        
    return index      #krijon nje dictionary ku çdo fjale e tekstit reference lidhet me listen e pozicioneve te saj ne liber