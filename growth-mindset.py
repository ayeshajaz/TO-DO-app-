import streamlit as st

st.title("📝 TO-DO List App")

# Initialize tasks list and editing index
if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "editing_index" not in st.session_state:
    st.session_state.editing_index = None

st.sidebar.header("📌 Manage Your Tasks")

new_task = st.sidebar.text_input("➕ Add a new task:", placeholder="Enter your task here")

if st.sidebar.button("Add Task"):
    if new_task.strip():
        st.session_state.tasks.append({"task": new_task, "completed": False})
        st.success("✅ Task added successfully!")
    else:
        st.warning("⚠️ Task cannot be empty!")

st.subheader("📋 Your TO-DO List")

if not st.session_state.tasks:
    st.info("ℹ️ No tasks added yet. Start by adding a task from the sidebar!")
else:
    for index, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([0.7, 0.15, 0.15])

        # Completed checkbox
        completed = col1.checkbox(f"**{task['task']}**", task['completed'], key=f"check_{index}")
        if completed != task['completed']:
            st.session_state.tasks[index]['completed'] = completed

        # Edit mode
        if st.session_state.editing_index == index:
            edited_text = col1.text_input("✍️ Edit task", value=task['task'], key=f"edit_{index}")
            if col2.button("💾 Save", key=f"save_{index}"):
                st.session_state.tasks[index]["task"] = edited_text
                st.session_state.editing_index = None
                st.rerun()
            if col3.button("❌ Cancel", key=f"cancel_{index}"):
                st.session_state.editing_index = None
                st.rerun()
        else:
            if col2.button("✎ Update", key=f"update_button_{index}"):
                st.session_state.editing_index = index
                st.rerun()
            if col3.button("🗑️ Delete", key=f"delete_{index}"):
                del st.session_state.tasks[index]
                st.rerun()

# Clear all tasks
if st.button("🗑️ Clear all tasks"):
    st.session_state.tasks = []
    st.success("🧼 All tasks deleted successfully!")
    st.rerun()

# Footer
st.markdown("---")
st.caption("🎯 Stay Organized with Your TO-DO List App")
