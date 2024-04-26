# Import required libraries
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai

# Define the prompt for the AI model

prompt = '''
  You are a YouTube video summarizer. Your job is to take the
  transcript text and summarize the entire video in concise
  bullet points within 250 words with a focus on extracting the summary
  and highlighting the videos key moments.
'''

# Define a function to extract transcript from a YouTube URL

def fetch_transcript(youtube_url):
  try:
    v_id = youtube_url.split('v=')[1].split('&')[0]
    transcript = YouTubeTranscriptApi.get_transcript(v_id)
    full_transcript = ' '.join([ i['text']  for i in transcript])
    return full_transcript
  except Exception as e:
    st.error(f'Failed to fetch transcript: {e}')
    return None

# Define a function for summarization using Google Gemini Pro

def generate_video_summary(api_key, full_transcript, prompt):
  # 1. Configure the api key
  genai.configure(api_key = api_key)
  # 2. Set the model to be used
  model = genai.GenerativeModel('gemini-pro')
  # 3. Query the model using the promt and transcript
  summary = model.generate_content(prompt + full_transcript)

  return summary.text

# Define a function for generating blog post

def generate_video_blog(api_key, full_transcript, prompt):
  # Fetch the AI generated summary that will be used to make the blog post
  summary = generate_gemini_content(api_key, full_transcript, prompt)

  # Specify the sections that you want the blog post to have
  blog_post = f'''
  ## Introduction
  Start with an engaging introduction that hooks the reader, providing a brief overview of the video's topic
  and why it's worth reading about.

  ## Participants
  Provide a quick concise introduction of the participants in the video. Make it wiity while remaining polite.

  ## Key Highlights
  - Highlight the most impactful points or insights from the video.
  - Offer quick, bullet-point summaries for readers who want the essence of the video's content.

  ## Main Content
  Give this section an appropriate header that is catchy and engaging and draws the audience to read more.
  {summary}

  ## Conclusion
  Wrap it up by giving a summary of the points discussed, reflecting their importance and also suggest
  similar reading content or action based on the the video.

  '''

  return blog_post

# Build the Streamlit UI App


# Set Title
st.title('Video to text content generation using Google Gemini Pro')

# Instructions to get Google API Key
st.markdown('''
### How to obtain a Google API Key
1. Visit the [Google Cloud Console](https://makersuite.google.com/app/apikey)
2. Create a new project or select an existing one.
3. Navigate to the 'APIs & Services > Credentials' page.
4. Click on 'Create Credentials' and select 'API Key'.
5. Your API key will be displayed; copy and store it in a safe place.
''')


# Get api key
api_key = st.text_input('Enter Google API Key: ', type='password')
# Get YouTube link
youtube_link = st.text_input('Enter YouTube URL: ')

if youtube_link:
  # Display the thumbnail for visual confirmation to the user that correct video has been fetched
  v_id = youtube_link.split('v=')[1].split('&')[0]
  thumbnail_url = f'http://img.youtube.com/vi/{v_id}/0.jpg'
  st.image(thumbnail_url, caption='Video Thumbnail', use_column_width=True)

  # Fetch transcript
  full_transcript = fetch_transcript(youtube_link)

  # Create 2 buttons - for summarization and for generating blog post
  col1, col2 = st.columns(2)
  with col1:
    if st.form_submit_button('Get Summary'):
      if full_transcript:
        summary = generate_video_summary(api_key, full_transcript, prompt)
        st.markdown('## Video Summary:')
        st.write(summary)
  with col2:
    if st.form_submit_button('Get Blog Post'):
      if full_transcript:
        blog_post = generate_video_blog(api_key, full_transcript, prompt)
        st.markdown('## Blog Post:')
          st.write(blog_post)
