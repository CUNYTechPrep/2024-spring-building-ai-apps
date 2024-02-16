import streamlit as st
from transformers import pipeline

# read about the model here:  https://huggingface.co/SamLowe/roberta-base-go_emotions
model_name = "SamLowe/roberta-base-go_emotions"

# the pipeline can be different things like classification, sentiment, or text-generation, question-answering
pipe = pipeline(
    task="text-classification", 
    model=model_name, 
    top_k=None)

# this is the text input box for the user
input_text = st.text_area('Tell me how your day was and I will guess how you are feeling...')

# if text means, if the variable text is not empty then run below
if input_text:
    out = pipe(input_text)
    st.json(out)

