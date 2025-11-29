from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv
load_dotenv()

class Chatbot:
    def __init__(self, model_name="gemini-2.5-flash"):
        self.model = ChatGoogleGenerativeAI(model=model_name)

    def generate_response(self, query, context):

        # Convert string → list of HumanMessage
        context_messages = [HumanMessage(content=context)]
    
        prompt = [
            SystemMessage(
                "You are an assistant that answers using ONLY the provided context. "
                "If the answer is not in the context, say: 'Given information is not sufficient to answer the question.'"
            ),
            *context_messages,
            HumanMessage(content=query)  # pass actual query, not "{query}"
        ]
    
        response = self.model.invoke(prompt)
        return response.content
