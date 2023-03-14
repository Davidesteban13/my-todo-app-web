import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    print("ADD TODO FUNCTION")
    if st.session_state['new_todo'] != '':
        print("addin a new todo")
        new_todo = st.session_state['new_todo']
        todos.append(new_todo + "\n")
        functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        print("to erase: ", index, todo)
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="todo:", placeholder="Add a new todo",
              on_change=add_todo, key='new_todo', value='')

#st.session_state