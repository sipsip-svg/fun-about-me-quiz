import streamlit as st

st.set_page_config(
    page_title="Fun About Me Quiz",
    page_icon="👽",
    layout="centered"
)

# 🎨 Custom Dark Sci-Fi / Alien Styling
st.markdown(
    """
    <style>
    /* Dark Deep Space Radial Gradient Background */
    .stApp {
        background: radial-gradient(circle at 50% 20%, #1d0f32, #0d061a 60%, #030108 100%);
        color: #e2e8f0;
    }

    /* Titles and Headers */
    h1 {
        color: #d8b4fe !important;
        text-align: center;
        font-family: 'Trebuchet MS', sans-serif;
        font-size: 42px !important;
        text-shadow: 0 0 12px rgba(168, 85, 247, 0.6);
    }
    
    h2, h3 {
        color: #38ef7d !important;
        text-shadow: 0 0 8px rgba(56, 239, 125, 0.4);
    }

    /* Labels and Body Text */
    label, p, .stMarkdown {
        color: #e2e8f0 !important;
        font-size: 16px;
    }

    /* Input Boxes & Selection Controls */
    div[data-baseweb="input"] > div, 
    div[data-baseweb="select"] > div, 
    textarea {
        background-color: #130a24 !important;
        border: 1.5px solid #00f2fe !important;
        border-radius: 8px !important;
        color: #ffffff !important;
        box-shadow: 0 0 8px rgba(0, 242, 254, 0.2);
    }

    /* Focus States for Inputs */
    div[data-baseweb="input"]:focus-within > div,
    textarea:focus {
        border-color: #38ef7d !important;
        box-shadow: 0 0 12px rgba(56, 239, 125, 0.5) !important;
    }

    /* Streamlit Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #11998e, #38ef7d) !important;
        color: #0d061a !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.5rem 1.5rem !important;
        box-shadow: 0 0 12px rgba(56, 239, 125, 0.4);
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        transform: scale(1.03);
        box-shadow: 0 0 18px rgba(56, 239, 125, 0.7);
    }

    /* Divider Lines */
    hr {
        border-color: #a855f7 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Keep answers while moving between pages
if "page" not in st.session_state:
    st.session_state.page = 1

# Store answers
if "answers" not in st.session_state:
    st.session_state.answers = {}

def next_page():
    st.session_state.page += 1

def previous_page():
    st.session_state.page -= 1

st.title("🛸 Fun About Me Quiz 🪐")

st.write(f"### Page {st.session_state.page} of 6")

# ---------------- PAGE 1 ----------------

if st.session_state.page == 1:

    st.header("👤 About You")

    st.session_state.answers["Name"] = st.text_input(
        "What is your name?"
    )

    st.session_state.answers["Age"] = st.number_input(
        "How old are you?",
        min_value=1,
        max_value=120,
        step=1
    )

    st.session_state.answers["Gender"] = st.selectbox(
        "What is your gender?",
        ["Male", "Female", "Other", "Prefer not to say"]
    )

    st.session_state.answers["Country"] = st.text_input(
        "What country are you from?"
    )

    st.session_state.answers["City"] = st.text_input(
        "What city or town do you live in?"
    )

    st.button("NEXT →", on_click=next_page)

# ---------------- PAGE 2 ----------------

elif st.session_state.page == 2:

    st.header("🏀 Outside School")

    st.session_state.answers["Hobbies"] = st.text_area(
        "What do you enjoy doing outside school?"
    )

    st.session_state.answers["After School"] = st.selectbox(
        "What do you normally do after school?",
        [
            "Play sports",
            "Play games",
            "Watch TV",
            "Use social media",
            "Hang out with friends",
            "Listen to music",
            "Relax",
            "Other"
        ]
    )

    st.session_state.answers["Weekend"] = st.selectbox(
        "What do you usually do on weekends?",
        [
            "Hang out with friends",
            "Play sports",
            "Play video games",
            "Watch movies",
            "Go shopping",
            "Spend time with family",
            "Relax at home",
            "Other"
        ]
    )

    st.session_state.answers["Sport"] = st.text_input(
        "What sport do you enjoy?"
    )

    st.session_state.answers["Games"] = st.text_input(
        "What games do you enjoy playing?"
    )

    st.session_state.answers["Perfect Weekend"] = st.text_area(
        "What would your perfect weekend look like?"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.button("← BACK", on_click=previous_page)

    with col2:
        st.button("NEXT →", on_click=next_page)

# ---------------- PAGE 3 ----------------

elif st.session_state.page == 3:

    st.header("⚡ This or That!")

    st.session_state.answers["Pizza or Burgers"] = st.radio(
        "🍕 Pizza or 🍔 Burgers?",
        ["Pizza", "Burgers"]
    )

    st.session_state.answers["Movies or Series"] = st.radio(
        "🎬 Movies or 📺 Series?",
        ["Movies", "Series"]
    )

    st.session_state.answers["Beach or Pool"] = st.radio(
        "🏖️ Beach or 🏊 Pool?",
        ["Beach", "Pool"]
    )

    st.session_state.answers["Gaming or TV"] = st.radio(
        "🎮 Gaming or 📺 Watching TV?",
        ["Gaming", "Watching TV"]
    )

    st.session_state.answers["Summer or Winter"] = st.radio(
        "☀️ Summer or ❄️ Winter?",
        ["Summer", "Winter"]
    )

    st.session_state.answers["Dogs or Cats"] = st.radio(
        "🐶 Dogs or 🐱 Cats?",
        ["Dogs", "Cats"]
    )

    st.session_state.answers["Music or Movies"] = st.radio(
        "🎵 Music or 🎬 Movies?",
        ["Music", "Movies"]
    )

    st.session_state.answers["Singing or Dancing"] = st.radio(
        "🎤 Singing or 💃 Dancing?",
        ["Singing", "Dancing"]
    )

    col1, col2 = st.columns(2)

    with col1:
        st.button("← BACK", on_click=previous_page)

    with col2:
        st.button("NEXT →", on_click=next_page)

# ---------------- PAGE 4 ----------------

elif st.session_state.page == 4:

    st.header("❤️ Your Favourite Things")

    st.session_state.answers["Favourite Food"] = st.text_input(
        "🍕 What is your favourite food?"
    )

    st.session_state.answers["Favourite Music"] = st.text_input(
        "🎵 What type of music do you like?"
    )

    st.session_state.answers["Favourite Movie"] = st.text_input(
        "🎬 What is your favourite movie or TV show?"
    )

    st.session_state.answers["Favourite Colour"] = st.text_input(
        "🎨 What is your favourite colour?"
    )

    st.session_state.answers["Favourite Place"] = st.text_input(
        "📍 What is your favourite place to go?"
    )

    st.session_state.answers["Social Media"] = st.selectbox(
        "📱 Which social media app do you use the most?",
        [
            "TikTok",
            "Instagram",
            "YouTube",
            "WhatsApp",
            "Snapchat",
            "Facebook",
            "Other"
        ]
    )

    col1, col2 = st.columns(2)

    with col1:
        st.button("← BACK", on_click=previous_page)

    with col2:
        st.button("NEXT →", on_click=next_page)

# ---------------- PAGE 5 ----------------

elif st.session_state.page == 5:

    st.header("😎 Your Personality")

    st.session_state.answers["Personality"] = st.selectbox(
        "How would you describe yourself?",
        [
            "Very outgoing",
            "Friendly and social",
            "A bit of both",
            "Quiet and calm",
            "Very quiet"
        ]
    )

    st.session_state.answers["Adventure"] = st.selectbox(
        "How adventurous are you?",
        [
            "I love trying new things!",
            "I sometimes try new things",
            "I prefer familiar things",
            "I don't like trying new things"
        ]
    )

    st.session_state.answers["Happy"] = st.text_input(
        "😊 What is something that always makes you happy?"
    )

    st.session_state.answers["Friends"] = st.selectbox(
        "How important are your friends to you?",
        [
            "Not very important",
            "A little important",
            "Important",
            "Very important",
            "Extremely important"
        ]
    )

    col1, col2 = st.columns(2)

    with col1:
        st.button("← BACK", on_click=previous_page)

    with col2:
        st.button("NEXT →", on_click=next_page)

# ---------------- PAGE 6 ----------------

elif st.session_state.page == 6:

    st.header("🚀 Random & Future Questions")

    st.session_state.answers["Dream Job"] = st.text_input(
        "What is your dream job?"
    )

    st.session_state.answers["Dream Destination"] = st.text_input(
        "✈️ Where would you love to travel?"
    )

    st.session_state.answers["Superpower"] = st.selectbox(
        "🦸 What superpower would you choose?",
        [
            "Flying",
            "Invisibility",
            "Reading minds",
            "Teleportation",
            "Super strength",
            "Time travel"
        ]
    )

    st.session_state.answers["Rich or Famous"] = st.radio(
        "💰 Would you rather be rich or famous?",
        ["Rich", "Famous"]
    )

    st.session_state.answers["Past or Future"] = st.radio(
        "⏰ Would you rather visit the past or the future?",
        ["Past", "Future"]
    )

    st.session_state.answers["One Word"] = st.text_input(
        "✨ Describe yourself in ONE word."
    )

    st.session_state.answers["Interesting Fact"] = st.text_area(
        "🤣 Tell us something interesting or funny about yourself."
    )

    st.button("← BACK", on_click=previous_page)

    st.divider()

    if st.button("🚀 COMPLETE THE MISSION"):
        name = st.session_state.answers.get("Name", "").strip() or "Earthling"

        st.balloons()

        st.success(f"Thank you for assisting me, {name}! 😚")

        st.header("🌎 THE TRUTH HAS BEEN REVEALED...")

        st.write(f"Hello {name}... 👽")
        st.write("I am actually an alien sent to Earth on a secret mission. 👾")
        st.write("My mission was to gather information about humans before beginning my plan to take over the world. 🌎👽")
        st.write(f"And thanks to YOU, {name}, I now have everything I need!")
        st.write("🚀 MISSION STATUS: COMPLETE")
        st.write(f"Thank you for assisting me, {name}. 😚")
        st.write("But I'll let you survive... since I like you so much. 😚👽👾")
        st.write("Don't tell the other aliens! 🤫")

        st.divider()

        st.header("🧸 A LITTLE GIFT FOR YOU 🧸")
        st.write("From your favourite alien 👽❤️")
        
        # Clean SVG HTML block without raw comments or string escaping issues
        alien_svg = """
        <div style="text-align: center; margin-top: 20px;">
            <svg width="280" height="340" viewBox="0 0 300 360" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="150" cy="100" r="65" fill="#a855f7" opacity="0.2" filter="blur(20px)" />
                <ellipse cx="150" cy="100" rx="50" ry="60" fill="#8b5cf6" stroke="#c084fc" stroke-width="3" />
                <ellipse cx="130" cy="95" rx="16" ry="22" fill="#030108" transform="rotate(-15 130 95)" />
                <ellipse cx="170" cy="95" rx="16" ry="22" fill="#030108" transform="rotate(15 170 95)" />
                <circle cx="126" cy="88" r="4" fill="#00f2fe" />
                <circle cx="166" cy="88" r="4" fill="#00f2fe" />
                <path d="M 142 135 Q 150 145 158 135" stroke="#38ef7d" stroke-width="3" stroke-linecap="round" fill="none" />
                <path d="M 128 155 L 110 270 L 190 270 L 172 155 Z" fill="#6d28d9" stroke="#a855f7" stroke-width="3" />
                <path d="M 118 170 Q 130 220 135 220" stroke="#8b5cf6" stroke-width="8" stroke-linecap="round" fill="none" />
                <path d="M 182 170 Q 170 220 165 220" stroke="#8b5cf6" stroke-width="8" stroke-linecap="round" fill="none" />
                <circle cx="150" cy="225" r="45" fill="#fbbf24" opacity="0.25" filter="blur(15px)" />
                <circle cx="125" cy="185" r="14" fill="#b45309" stroke="#78350f" stroke-width="2" />
                <circle cx="125" cy="185" r="8" fill="#fde68a" />
                <circle cx="175" cy="185" r="14" fill="#b45309" stroke="#78350f" stroke-width="2" />
                <circle cx="175" cy="185" r="8" fill="#fde68a" />
                <ellipse cx="150" cy="235" rx="28" ry="32" fill="#d97706" stroke="#78350f" stroke-width="2" />
                <ellipse cx="130" cy="262" rx="10" ry="8" fill="#b45309" />
                <ellipse cx="170" cy="262" rx="10" ry="8" fill="#b45309" />
                <circle cx="150" cy="202" r="26" fill="#d97706" stroke="#78350f" stroke-width="2" />
                <ellipse cx="150" cy="208" rx="11" ry="9" fill="#fde68a" />
                <ellipse cx="150" cy="204" rx="4" ry="3" fill="#451a03" />
                <path d="M 150 207 L 150 211 M 147 212 Q 150 215 153 212" stroke="#451a03" stroke-width="1.5" stroke-linecap="round" fill="none" />
                <circle cx="140" cy="198" r="3" fill="#1e1b4b" />
                <circle cx="160" cy="198" r="3" fill="#1e1b4b" />
                <circle cx="141" cy="197" r="1" fill="#ffffff" />
                <circle cx="161" cy="197" r="1" fill="#ffffff" />
                <ellipse cx="150" cy="238" rx="16" ry="18" fill="#fde68a" />
                <path d="M 143 218 L 150 222 L 143 226 Z M 157 218 L 150 222 L 157 226 Z" fill="#f43f5e" />
                <circle cx="150" cy="222" r="2" fill="#9f1239" />
                <path d="M 95 120 L 97 125 L 102 127 L 97 129 L 95 134 L 93 129 L 88 127 L 93 125 Z" fill="#38ef7d" />
                <path d="M 205 130 L 207 135 L 212 137 L 207 139 L 205 144 L 203 139 L 198 137 L 203 135 Z" fill="#00f2fe" />
                <path d="M 105 240 L 106 243 L 109 244 L 106 245 L 105 248 L 104 245 L 101 244 L 104 243 Z" fill="#fef08a" />
            </svg>
        </div>
        """
        
        st.markdown(alien_svg, unsafe_allow_html=True)
        
        st.markdown(
            f"""
            <p style="text-align: center; color: #38ef7d !important; font-weight: bold; font-size: 18px; margin-top: 10px;">
                🧸 This teddy bear is for you, {name}! 🧸
            </p>
            """,
            unsafe_allow_html=True
        )

        st.balloons()

