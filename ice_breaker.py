from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

def get_details(name: str) -> str:
    linkedin_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(url=linkedin_url)

    template = """
    given the Linkedin information {info} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """
    prompt_template = PromptTemplate(
        input_variables=["information"], template=template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=prompt_template)
    res = chain.invoke(input={"info": linkedin_data})

    print(res)


if __name__ == "__main__":
    load_dotenv()
    get_details(name="Nikeshh")