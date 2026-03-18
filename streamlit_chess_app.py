import streamlit as st
import chess
import chess.svg
from streamlit.components.v1 import html

st.set_page_config(page_title="Chess Explorer ♟️")

st.title("♟️ Chess Explorer")
st.write("Play moves and watch the board update!")

# Initialize board in session state
if "board" not in st.session_state:
    st.session_state.board = chess.Board()

board = st.session_state.board

# Display board
board_svg = chess.svg.board(board=board, size=500)
html(board_svg, height=520)

# Move input
move_input = st.text_input("Enter your move (e.g., e4, Nf3, Qh5):")

if st.button("Play Move"):
    try:
        move = board.parse_san(move_input)
        board.push(move)
        st.success(f"Move played: {move_input}")
    except:
        st.error("Invalid move! Try again.")

# Reset button
if st.button("Reset Game"):
    st.session_state.board = chess.Board()
    st.experimental_rerun()

# Show move history
st.subheader("📜 Move History")
st.write(board.move_stack)
