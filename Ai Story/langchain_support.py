import os
from langchain_groq import ChatGroq
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain_core.prompts import PromptTemplate
'''
1 - Creating AT model

2 - Making templet(PromptTemplate) for chapter name
3 - Making a object form LLMChain using chapter name templet

4 - Making templet(PromptTemplate) for chapter paragraph 
5 - Making a object from LLMChain using paragraph templet

6 - Creating a Simple Sequential chains (SimpleSequentialChain) using both chain object created above
'''  
   
# 1 - Creating AT model
os.environ['GROQ_API_KEY'] = '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'
model = ChatGroq(model='llama3-8b-8192')

def get_paagraph_content(book_name):
    # 2 - Making templet (PromptTemplate) for generating a short story for the book name
    book_name_templet = PromptTemplate(
        input_variables=['book_name'],
        template='If the user provides "{book_name}" as the name of a book, create a short, captivating story that aligns with the book title and themes implied by it.'
    )

    # 3 - Making an object form LLMChain using the book name template
    book_name_LLMChain = LLMChain(llm=model, prompt=book_name_templet)

    # 4 - Making templet (PromptTemplate) for chapter paragraph (poems)
    content_patagraph_chapter_one_template = PromptTemplate(
        input_variables=['chapter_name'],
        template='Generate a short story for the given chapter "{chapter_name}". Ensure the story is thematically connected to the book title and chapter name.'
    )

    # 5 - Making an object from LLMChain using the paragraph template
    content_patagraph_chapter_one_LLMChain = LLMChain(
        llm=model,
        prompt=content_patagraph_chapter_one_template
    )

    final_chain = SimpleSequentialChain(chains=[book_name_LLMChain, content_patagraph_chapter_one_LLMChain],
                                        verbose=True)

    result = final_chain.invoke(book_name)

    return result

# if __name__=="__main__":
#get_paagraph_content('A great day')jkm