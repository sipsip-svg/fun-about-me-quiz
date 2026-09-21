import streamlit as st

st.set_page_config(
    page_title="Fun About Me Quiz",
    page_icon="🎉"
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

st.title("🎉 Fun About Me Quiz")

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

    name = st.session_state.answers["Name"]

    st.balloons()

    st.success(f"👽 Thank you for assisting me, {name}!")

    st.header("🌎 THE TRUTH HAS BEEN REVEALED...")

    st.write(
    f"""
👽 Hello {name}...

I am actually an alien sent to Earth on a secret mission.

My mission was to gather information about humans before
beginning my plan to take over the world. 🌎👽

And thanks to YOU, {name}, I now have everything I need!

🚀 MISSION STATUS: COMPLETE

Thank you for assisting me, {name}. 😚

But I'll let you survive... since I like you so much. 😚👽👾

Don't tell the other aliens! 🤫
"""
        )

    st.divider()

    st.header("💐 A LITTLE GIFT FOR YOU 💐")

    st.write("🌹 🌷 🌸 🌺 🌻 🌼 🌹 🌷 🌸")

    st.markdown(
        f"""
        ### 💐 These flowers are for you, {name}! 💐

        🌹 🌷 🌸 🌺 🌻 🌼 🌹

        From your favourite alien 👽❤️
        """
    )

    st.balloons()
