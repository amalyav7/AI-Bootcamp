import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="ShieldScam",
    page_icon="🛡️",
    layout="centered"
)

# -----------------------------
# CONNECT TO OLLAMA
# -----------------------------

client = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key="f2d45f20df334a219cb9cb3eeb6b05ea.vjKMGFEkQU6TS9zS6kTGLv9m"
)

# -----------------------------
# PAGE STATE
# -----------------------------

if "page" not in st.session_state:
    st.session_state.page = "home"

if "result" not in st.session_state:
    st.session_state.result = ""

if "error" not in st.session_state:
    st.session_state.error = ""


# -----------------------------
# HOME / SCAN PAGE
# -----------------------------

def home_page():

    st.title("🛡️ ShieldScam")
    st.subheader("AI Scam Message Detector")

    st.write(
        "Paste a suspicious email or message below and ShieldScam "
        "will check it for common scam warning signs."
    )

    sender = st.text_input("From Email Address")

    subject = st.text_input("Subject")

    message = st.text_area(
        "Email or Message",
        height=200,
        placeholder="Paste the suspicious message here..."
    )

    attachment = st.checkbox("Does the message include an attachment?")

    if st.button("🔍 Check for Scam", use_container_width=True):

        if message.strip() == "":
            st.warning("Please enter a message before scanning.")
            return

        prompt = f"""
You are an AI scam detector.

Analyze the following message.

Sender:
{sender}

Subject:
{subject}

Message:
{message}

Attachment:
{attachment}

Determine whether the message is:

SAFE
SUSPICIOUS
SCAM

Explain the warning signs in simple language.

Also give the user a recommended action.

Keep the answer short and easy to understand.
"""

        try:

            with st.spinner("ShieldScam is checking the message..."):

                response = client.chat.completions.create(
                    model="gemma3:1b",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0.1
                )

            st.session_state.result = (
                response.choices[0].message.content
            )

            st.session_state.page = "result"

            st.rerun()

        except Exception as e:

            st.session_state.error = str(e)

            st.session_state.page = "error"

            st.rerun()


# -----------------------------
# RESULT PAGE
# -----------------------------

def result_page():

    st.title("🛡️ ShieldScam")

    st.success("✅ Scan Complete")

    st.header("Scan Result")

    st.write(
        "ShieldScam analyzed your message for common scam warning signs."
    )

    st.markdown("---")

    st.subheader("🤖 AI Analysis")

    st.write(st.session_state.result)

    st.markdown("---")

    st.subheader("🛡️ Stay Safe")

    st.info(
        """
        Never send passwords, bank information, Social Security numbers,
        or verification codes through suspicious messages.

        If you are unsure, contact the company using its official website
        or phone number.
        """
    )

    st.markdown("---")

    if st.button(
        "🔍 Scan Another Message",
        use_container_width=True
    ):

        st.session_state.page = "home"
        st.session_state.result = ""

        st.rerun()


# -----------------------------
# ERROR PAGE
# -----------------------------

def error_page():

    st.title("🛡️ ShieldScam")

    st.error("⚠️ Oops! Something went wrong.")

    st.header("We couldn't analyze your message.")

    st.write(
        "ShieldScam was unable to connect to the AI."
    )

    st.markdown("---")

    st.subheader("Possible Reasons")

    st.write("""
    • Ollama may not be running

    • The AI model may not be installed

    • There may be a connection problem

    • The AI service may be temporarily unavailable
    """)

    st.info(
        "Make sure Ollama is running and then try again."
    )

    with st.expander("Technical Details"):
        st.code(st.session_state.error)

    st.markdown("---")

    if st.button(
        "🔄 Try Again",
        use_container_width=True
    ):

        st.session_state.page = "home"
        st.session_state.error = ""

        st.rerun()


# -----------------------------
# DISPLAY CURRENT PAGE
# -----------------------------

if st.session_state.page == "home":
    home_page()

elif st.session_state.page == "result":
    result_page()

elif st.session_state.page == "error":
    error_page()