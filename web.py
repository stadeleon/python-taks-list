import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is subheader for the app")
st.write("This app is to increase our productivity and python knowledge")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a task here", placeholder="Enter a task here",
              on_change=add_todo, key='new_todo')

st.session_state
