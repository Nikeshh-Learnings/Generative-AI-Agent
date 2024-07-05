from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    load_dotenv()

    template = """
    given the Linkedin data {data} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    prompt_template = PromptTemplate(
        input_variables=["data"], template=template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=prompt_template)
    data = scrape_linkedin_profile(
        url="https://www.linkedin.com/in/nikeshh/",
        mock=True,
    )
    response = chain.invoke(input={"data": data})

    print(response)