#!/usr/bin/env python
# coding: utf-8

# In[41]:


from ctypes import alignment
from tkinter import CENTER
import cohere 
co = cohere.Client('hfNbS9V7g3ObRHd2LgWy5IyM4VTymZkLazHV3obr') # This is your trial API key


# In[42]:


def write_post(topic):
    response = co.generate(
      model='command-xlarge-nightly',
      prompt=f'write a blog post on the topic of \"{topic}\"',
      max_tokens=300,
      temperature=0.75,
      k=0,
      p=0.75,
      frequency_penalty=0.7,
      presence_penalty=0.1,
      stop_sequences=[],
      return_likelihoods='NONE')
    return response.generations[0].text

def write_poem(topic):
    response = co.generate(
      model='command-xlarge-nightly',
      prompt=f'write a poem on the topic of \"{topic}\"',
      max_tokens=202,
      temperature=0.9,
      k=0,
      p=0.75,
      frequency_penalty=0.7,
      presence_penalty=0.1,
      stop_sequences=[],
      return_likelihoods='NONE')
    return response.generations[0].text

def write_story(topic):
    response = co.generate(
      model='command-xlarge-nightly',
      prompt=f'write a short story on the topic of \"{topic}\"',
      max_tokens=500,
      temperature=0.9,
      k=0,
      p=0.75,
      frequency_penalty=0.7,
      presence_penalty=0.1,
      stop_sequences=[],
      return_likelihoods='NONE')
    return response.generations[0].text    


# In[44]:


import streamlit as st
# def main():
#     st.sidebar.title("Navigation")
#     selection = st.sidebar.radio("Select a function", ["Write a Blog Post", "Write a Poem", "Write a Short Story"])

#     topic = st.text_input("Enter a topic")
#     if st.button("Generate"):
#         if selection == "Write a Blog Post":
#             result = write_post(topic)
#         elif selection == "Write a Poem":
#             result = write_poem(topic)
#         else:
#             result = write_story(topic)
#         st.success(result)

# if __name__ == '__main__':
#     main()
def main():
    st.sidebar.image("logo.jpg", width= 300)
    st.sidebar.title("What do you want to generate")
    app_mode = st.sidebar.selectbox("Choose one", ["Blog Post", "Poem", "Story"])

    if app_mode == "Blog Post":
        st.title("Blog Post Generator")
        topic = st.text_input("Enter topic:")
        if st.button("Generate Blog Post"):
            blog_post = write_post(topic)
            st.write("Generated Blog Post:", blog_post)

    elif app_mode == "Poem":
        st.title("Poem Generator")
        topic = st.text_input("Enter topic:")
        if st.button("Generate Poem"):
            poem = write_poem(topic)
            st.write("Generated Poem:", poem)

    elif app_mode == "Story":
        st.title("Story Generator")
        topic = st.text_input("Enter topic:")
        if st.button("Generate Story"):
            story = write_story(topic)
            st.write("Generated Story:", story)

if __name__ == '__main__':
    main()

