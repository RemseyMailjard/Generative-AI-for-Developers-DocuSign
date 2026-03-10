import streamlit as st
import random

'''
Generate a rock-paper-scissors game using Streamlit. The game should allow the user to select rock, paper, or scissors, and then display the computer's choice and the result of the game (win, lose, or tie). The game should also keep track of the player's score and the computer's score across multiple rounds.
You can use the following code to create a rock-paper-scissors game using Streamlit. This code includes the game logic, user interface, and score tracking.
'''
st.title("Rock Paper Scissors")

if "player_score" not in st.session_state:
    st.session_state.player_score = 0
    st.session_state.computer_score = 0

col1, col2 = st.columns(2)
with col1:
    st.metric("Player Score", st.session_state.player_score)
with col2:
    st.metric("Computer Score", st.session_state.computer_score)

player_choice = st.radio("Choose your move:", ["Rock", "Paper", "Scissors"])

if st.button("Play"):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    
    st.write(f"You chose: {player_choice}")
    st.write(f"Computer chose: {computer_choice}")
    
    if player_choice == computer_choice:
        st.write("It's a tie!")
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        st.write("You win!")
        st.session_state.player_score += 1
    else:
        st.write("Computer wins!")
        st.session_state.computer_score += 1
