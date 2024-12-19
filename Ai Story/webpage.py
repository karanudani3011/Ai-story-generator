import streamlit as st  # Importing the Streamlit library for building the app
import langchain_support as LC  # Importing a custom module for LangChain support
import os  # Importing os module to work with file paths

# Page Configurations
st.set_page_config(
    page_title="AI Versemith",  # Title of the page
    page_icon="✍️",  # Icon displayed in the browser tab
    layout="wide",  # Layout style of the app
    initial_sidebar_state="expanded"  # Sidebar starts expanded
)
# Custom CSS for Better Styling
st.markdown(
    """
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .main-title {
            text-align: center;
            color: #2a85a8;
            font-size: 2.5rem;
            margin-top: 10px;
        }
        .subtitle {
            text-align: center;
            color: #919ca3;
            font-size: 1.2rem;
            margin-bottom: 30px;
        }
        .content-box {
            background-color: #f2f7fc;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            margin: 20px 0;
        }
        .poem-box {
            background-color: #d9dcde;
            padding: 15px;
            border-left: 5px solid #007bff;
            font-style: italic;
            border-radius: 5px;
        }
        hr {
            margin: 30px 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
# Main Title
st.markdown("<h1 class='main-title'>✍️ AI Versemith</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Effortlessly create personalized story using AI!</p>", unsafe_allow_html=True)

# Sidebar Information
st.sidebar.title("📖 About This App")
st.sidebar.info(
    """
   Your thoughts, your story. One or two words is all it takes to tailor an AI-generated verse to your liking.
    """
)
st.sidebar.title("🌟 How to Use")
st.sidebar.markdown(
    """
    1. Enter a **Book Name** or **Topic** in the text box.
    2. Click **Generate Story**.
    3. Read and enjoy your personalized story!
    """
)
# Input Section
st.markdown("### 🎨 Enter Book Name or Topic Below:")
book_name = st.text_input("", placeholder="e.g., A Journey to the Stars")

# Generate Poem Button
if st.button("📝 Generate Story"):
    if book_name.strip():
        with st.spinner("✨ Crafting your personalized Story..."):
            try:
                # Fetch content from LangChain support
                result = LC.get_paagraph_content(book_name)
                chapter_content = result["output"]

                # Display Results
                st.markdown("### 🌟 Your Generated Story:")
                st.markdown(
                    f"<div class='Story-box'>{chapter_content}</div>", unsafe_allow_html=True
                )
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("⚠️ Please enter a valid Book Name or Topic!")

# Example Suggestions Section
with st.expander("💡 Need Inspiration?"):
    st.markdown(
        """
        - **Topics:** Love, Nature, Dreams, Adventure, Hope
        - **Book Names:** *Winds of Change*, *Echoes of Eternity*, *The Silent Forest*
        """
    )

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    """
    <p style='text-align: center; font-size: small; color: #6c757d;'>
    Built with ❤️ using <a href='https://streamlit.io/' target='_blank'>Streamlit</a>.
    </p>
    """,
    unsafe_allow_html=True,
)
