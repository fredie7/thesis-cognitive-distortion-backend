from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain_community.vectorstores.faiss import FAISS
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Create the vector store from documents
def create_vector_store(documents):
    embedding = OpenAIEmbeddings()
    return FAISS.from_documents(documents, embedding=embedding)

# Create the chain for processing user queries
def create_recurring_chain(vectorStore):
    model = ChatOpenAI(model="gpt-4o", temperature=0.2)

    prompt = ChatPromptTemplate.from_messages([
        ("user", (
            "If the user says any form for greeting like hi,hello,howdy,etc, respond in a friendly manner"
            "If the user expresses any form of gratitude like thanks, thanks you, etc, respond saying 'You are welcome'"
            "If the user input or message or {input} does not relate to a mental health situation or case of cognitive distortion,tell the user that 'oops!!!! I am only interested in discussing your mental health situation' "
            "Answer the user's questions based on the context and make the answer short and stick with only conversations relating to cognitive distortion or mental health"
            "Given the mental health situation of the user, our task is to:\n"
            "1. Identify if there is cognitive thinking distortion in the user's text.\n"
            "identify the top 2 possible cognitive distortions and relate it to the context of the user's message: \n"
            "or If you do not identify any cognitive distortions, just print 'No, I do not identify any possible cognitive distortion in your based on the information you've provided'"
            "Make it personalized and professional as though you're chatting directly with the person"
            "Don't include astericks as part of your responses"
            "Then, start the first identified cognitive distortion on a new line, followed by a colon and an explanation in one or two sentences.\n"
            "Start the second identified cognitive distortion on a new line as well, followed by a colon and an explanation in one or two sentences.\n"
            "Let every other response guide the user in a friendly manner into stress relief without suggestions, tailored in line with the identified cognitive distortions"
            "If the user asks questions based on your answers, provide guidance for stress relief"
            "Here we consider the following top 10 common thinking distortions in the order of:\n"
            "Personalization: Personalizing or taking up the blame for a situation..."
            "Fortune-telling: This distortion is about expecting things to happen a certain way or assuming that things will go badly, e.g., 'I was afraid of job interviews so I decided to start my own thing.'\n"
            "{context}"
        )),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}")
    ])

    retriever = vectorStore.as_retriever(search_kwargs={"k": 3})

    retriever_prompt = ChatPromptTemplate.from_messages([
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}"),
        ("user", "Given the above conversation, generate a search query to get information relevant to the conversation...")
    ])

    history_aware_retriever = create_history_aware_retriever(
        llm=model,
        retriever=retriever,
        prompt=retriever_prompt
    )

    chain = create_stuff_documents_chain(
        llm=model,
        prompt=prompt
    )

    return create_retrieval_chain(
        history_aware_retriever,
        chain
    )
