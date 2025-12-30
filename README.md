# Library Management System

A simple, Object-Oriented Programming (OOP) based Library Management System built with Python and Streamlit. This application allows for managing books, members, and borrowing operations through a user-friendly web interface.

## Features

*   **Dashboard**: View real-time statistics about the library's collection, including total books, total members, and currently borrowed books.
*   **Book Management**:
    *   **View Books**: Browse the entire collection of books.
    *   **Filter**: Filter books by their availability status (Available/Borrowed).
    *   **Add Books**: (Admin) Add new books to the library with details like Title, Author, ISBN, and Genre.
*   **Member Management**:
    *   **Register Member**: Sign up new members with their Name, Email, and a unique Member ID.
    *   **View Members**: List all registered members.
*   ** borrowing Operations**:
    *   **Borrow Book**: Allow members to borrow available books using their Member ID and the Book's ISBN.
    *   **Return Book**: Process book returns and update inventory availability.
*   **Data Persistence**: All data (books and members) is saved persistently in JSON files, ensuring data is not lost between sessions.

## Tech Stack

*   **Language**: Python 3.x
*   **Frontend Framework**: Streamlit
*   **Data Handling**: Pandas, JSON (for local storage)
*   **Concepts**: Object-Oriented Programming (Classes, Inheritance, Encapsulation)

## Project Structure

```
├── app.py              # Main Streamlit application file containing the UI logic
├── models.py           # Python classes defining the data models (Library, Book, Member, Person)
├── data/               # Directory for storing persistent data
│   ├── books.json      # JSON file storing book records
│   └── members.json    # JSON file storing member records
└── README.md           # Project documentation
```

## Setup & Installation

1.  **Clone the repository** (if applicable) or copy the project files to your local machine.

2.  **Install Dependencies**:
    Make sure you have Python installed. Then, install the required libraries:
    ```bash
    pip install streamlit pandas
    ```

3.  **Run the Application**:
    Navigate to the project directory in your terminal and run:
    ```bash
    streamlit run app.py
    ```

4.  **Access the App**:
    The application will automatically open in your default web browser (usually at `http://localhost:8501`).

## Usage Guide

1.  **Dashboard**: Start here to see an overview of the library system.
2.  **Admin**: Use the Admin tab to populate the library with some initial books.
3.  **Members**: Register a new member to enable borrowing.
4.  **Borrow/Return**: Use the respective tabs to simulate the lending process.

## OOP Concepts Used

*   **Classes & Objects**: Core entities like `Book`, `Member`, and `Library` are encapsulated as classes.
*   **Inheritance**: The `Member` class inherits from a base `Person` class.
*   **Encapsulation**: Data and methods acting on that data are bundled together within classes.

## Developer

Developed by: **Varun Bothra**
Class: **2X15**
Dept: **Computer Science(OOPS Project)**
