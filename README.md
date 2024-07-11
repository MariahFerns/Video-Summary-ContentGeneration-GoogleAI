# [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mariahferns-video-summary-contentgeneration-googleai-app-jmbu9u.streamlit.app/)

### Overview
This is an innovative application designed to transform YouTube videos into detailed blog posts. Utilizing Google's generative AI technology and the YouTube Transcript API, this application extracts transcripts from videos and intelligently generates summaries and structured blog content. It's an invaluable tool for content creators, marketers, educators, and anyone looking to repurpose video content into written form.

### Features
- Automated Summary Generation: Quickly generate summaries from YouTube videos by simply providing the video link.
- Structured Blog Post Creation: Convert summaries into comprehensive blog posts with sections for Introduction, Key Takeaways, Main Content, and Conclusion.
- Streamlit Web Interface: Offers an easy-to-use Streamlit web interface for seamless user interaction.

### Setup
#### Prerequisites
- Python 3.6 or later
- Pip package manager

#### Installation Instructions
1. Clone the GitHub repository:
```bash
git clone https://github.com/yourusername/youtube-blog-post-generator.git
cd youtube-blog-post-generator
```
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```
3. Obtain a Google API Key (for generative AI features):

- The application's UI provides guidance on obtaining this key.

#### How to Run the Application
1.Start the app with Streamlit by running the following command in your terminal:
```bash
streamlit run app.py
```
2. Navigate to the provided local URL in your web browser to access the app.

### How to Use
1. Input Your Google API Key: For security, enter your Google API key into the designated field within the app.
2. Enter a YouTube Video Link: Paste the URL of the YouTube video you want to convert into a blog post.
3. Choose Your Action: Select whether to generate a video summary or convert the video directly into a structured blog post.


