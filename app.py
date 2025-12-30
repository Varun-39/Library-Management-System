import streamlit as st
import pandas as pd
from models import Library, Book, Member

# Initialize Library
if 'library' not in st.session_state:
    st.session_state.library = Library()

lib = st.session_state.library

st.set_page_config(page_title="Library Management System", layout="wide")

# Custom CSS for a "Student Project" feel but clean
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
    }
    .stSidebar {
        background-color: #e8eaf6;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Library Management System")
st.markdown("### OOP Project - Computer Science Dept")

# Sidebar Navigation
menu = ["Dashboard", "View Books", "Members", "Borrow Book", "Return Book", "Admin"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Dashboard":
    st.subheader("Dashboard")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Total Books", value=len(lib.books))
    
    with col2:
        st.metric(label="Total Members", value=len(lib.members))
    
    with col3:
        borrowed_count = sum(1 for book in lib.books if not book.is_available)
        st.metric(label="Books Borrowed", value=borrowed_count)

    st.image("https://img.freepik.com/free-vector/library-interior-empty-room-reading-with-books-wooden-shelves_33099-1722.jpg", caption="Welcome to our Library")

elif choice == "View Books":
    st.subheader("All Books")
    
    if not lib.books:
        st.info("No books in the library yet.")
    else:
        # Convert to DataFrame for better display
        books_data = [b.to_dict() for b in lib.books]
        df = pd.DataFrame(books_data)
        
        # Add a status column for better readability
        df['Status'] = df['is_available'].apply(lambda x: 'Available' if x else 'Borrowed')
        
        # Filter options
        filter_status = st.radio("Filter by Status", ["All", "Available", "Borrowed"], horizontal=True)
        
        if filter_status == "Available":
            df = df[df['is_available'] == True]
        elif filter_status == "Borrowed":
            df = df[df['is_available'] == False]
            
        st.dataframe(df[['title', 'author', 'genre', 'isbn', 'Status']], use_container_width=True)

elif choice == "Members":
    st.subheader("Member Management")
    
    tab1, tab2 = st.tabs(["View Members", "Register New Member"])
    
    with tab1:
        if not lib.members:
            st.info("No members registered yet.")
        else:
            members_data = [m.to_dict() for m in lib.members]
            df = pd.DataFrame(members_data)
            st.dataframe(df[['name', 'email', 'member_id']], use_container_width=True)
            
    with tab2:
        with st.form("register_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            member_id = st.text_input("Member ID (Unique)")
            
            submitted = st.form_submit_button("Register")
            if submitted:
                if lib.find_member(member_id):
                    st.error("Member ID already exists!")
                elif name and email and member_id:
                    new_member = Member(name, email, member_id)
                    lib.register_member(new_member)
                    st.success(f"Member {name} registered successfully!")
                else:
                    st.warning("Please fill all fields.")

elif choice == "Borrow Book":
    st.subheader("Borrow a Book")
    
    col1, col2 = st.columns(2)
    
    with col1:
        member_id = st.text_input("Enter Member ID")
    
    with col2:
        isbn = st.text_input("Enter Book ISBN")
        
    if st.button("Borrow"):
        if member_id and isbn:
            success, message = lib.borrow_book(member_id, isbn)
            if success:
                st.success(message)
            else:
                st.error(message)
        else:
            st.warning("Please enter both Member ID and ISBN.")

elif choice == "Return Book":
    st.subheader("Return a Book")
    
    col1, col2 = st.columns(2)
    
    with col1:
        member_id = st.text_input("Enter Member ID")
    
    with col2:
        isbn = st.text_input("Enter Book ISBN")
        
    if st.button("Return"):
        if member_id and isbn:
            success, message = lib.return_book(member_id, isbn)
            if success:
                st.success(message)
            else:
                st.error(message)
        else:
            st.warning("Please enter both Member ID and ISBN.")

elif choice == "Admin":
    st.subheader("Admin Area - Add Books")
    
    with st.form("add_book_form"):
        title = st.text_input("Book Title")
        author = st.text_input("Author")
        isbn = st.text_input("ISBN")
        genre = st.selectbox("Genre", ["Fiction", "Non-Fiction", "Sci-Fi", "Mystery", "Biography", "Textbook"])
        
        submitted = st.form_submit_button("Add Book")
        if submitted:
            if lib.find_book(isbn):
                st.error("Book with this ISBN already exists!")
            elif title and author and isbn:
                new_book = Book(title, author, isbn, genre)
                lib.add_book(new_book)
                st.success(f"Book '{title}' added successfully!")
            else:
                st.warning("Please fill all fields.")

st.sidebar.markdown("---")
st.sidebar.info("Developed by: Varun Bothra \n Class: 2X15")
