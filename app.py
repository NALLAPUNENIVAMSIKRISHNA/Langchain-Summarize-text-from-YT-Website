import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from pytube.exceptions import RegexMatchError, VideoUnavailable, PytubeError

# Streamlit app
st.set_page_config(page_title="Langchain Summarize text from YT Or Website",page_icon="🦜")
st.title("🦜 Langchain Summarize text from YT Or Website")
st.subheader("Summarize URL")

# Get the groq api key and url (YT or website) to be summarized.
with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", value="", type="password")

generic_url = st.text_input('URL', label_visibility="collapsed")

# Llama3 using groq api
llm = ChatGroq(model="Llama3-8b-8192", groq_api_key=groq_api_key)

prompt_template = """Provide a summary of the following content in 300 words
Content : {text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=['text'])

if st.button("Summarize the content from YT Or Website"):
    # Validate all the inputs
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please fill all the fields")
    elif not validators.url(generic_url):
        st.error("Please enter valid URL. It can may be a YT video URL or Website URL")
    else:
        try:
            with st.spinner("waiting..."):
                # Load the website or yt video data
                if "youtube.com" in generic_url:
                    try:
                        loader = YoutubeLoader.from_youtube_url(generic_url) #removed add_video_info
                        docs = loader.load()
                    except (RegexMatchError, VideoUnavailable, PytubeError) as e:
                        st.error(f"Error loading YouTube video: {e}")
                        st.stop()
                else:
                    loader = UnstructuredURLLoader(urls=[generic_url], ssl_verify=False,
                                                    headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                    docs = loader.load()

                # Chain for summarization
                chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                output_summary = chain.invoke(input={"input_documents":docs})["output_text"]

                st.success(output_summary)
        except Exception as e:
            st.exception(f"Exception : {e}")