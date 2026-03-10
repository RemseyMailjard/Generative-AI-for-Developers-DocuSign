'''
Create a Rock Paper Scissors game where the player inputs their choice and plays against a computer
that randomly selects its move with the game showing who won each round.

Add a score counter that tracks player and computer wins, and allow the game
to continue until the player types 'quit'
'''


import random
import streamlit as st

def get_computer_choice():
    return random.choice(["r", "p", "s"])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "r" and computer_choice == "s") or \
         (player_choice == "p" and computer_choice == "r") or \
         (player_choice == "s" and computer_choice == "p"):
        return "player"
    else:
        return "computer"
    

def main():
    st.title("Rock Paper Scissors")
    st.write("Play against the computer. Click a button to make your move!")

    if 'player_score' not in st.session_state:
        st.session_state['player_score'] = 0
    if 'computer_score' not in st.session_state:
        st.session_state['computer_score'] = 0
    if 'result' not in st.session_state:
        st.session_state['result'] = ""
    if 'last_computer_choice' not in st.session_state:
        st.session_state['last_computer_choice'] = ""

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Rock 🪨"):
            play_round('r')
    with col2:
        if st.button("Paper 📄"):
            play_round('p')
    with col3:
        if st.button("Scissors ✂️"):
            play_round('s')

    st.write(f"**Score:** You {st.session_state['player_score']} - Computer {st.session_state['computer_score']}")

    if st.session_state['result']:
        st.write(st.session_state['result'])
        if st.session_state['last_computer_choice']:
            st.write(f"Computer picked: {choice_to_word(st.session_state['last_computer_choice'])}")

    if st.button("Reset Game"):
        st.session_state['player_score'] = 0
        st.session_state['computer_score'] = 0
        st.session_state['result'] = ""
        st.session_state['last_computer_choice'] = ""

def play_round(player_choice):
    computer_choice = get_computer_choice()
    winner = determine_winner(player_choice, computer_choice)
    st.session_state['last_computer_choice'] = computer_choice
    if winner == "tie":
        st.session_state['result'] = "It's a tie!"
    elif winner == "player":
        st.session_state['result'] = "You win!"
        st.session_state['player_score'] += 1
    else:
        st.session_state['result'] = "You lose!"
        st.session_state['computer_score'] += 1

def choice_to_word(choice):
    return {"r": "Rock 🪨", "p": "Paper 📄", "s": "Scissors ✂️"}.get(choice, "?")

if __name__ == "__main__":
    main()