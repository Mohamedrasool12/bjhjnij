import pandas as pd
import streamlit as st

def book_description_section(title):
    st.header(f"Book Description: {title}")
    # Add book description content here
    st.write("This is the book description section.")
    # Add book description content here

def main():
    st.set_page_config(layout='wide', page_title='Address Book', page_icon='📚')
    st.markdown("<h1 style='text-align: center; color: blue;'>📚</h1>", unsafe_allow_html=True)
    st.title("Book Store App")

    data = pd.read_csv("/Users/da-m1-40/Downloads/books1.csv")

    x = 1000 
    while x > 0:  # Adjusted the loop condition to stop at 0
        col1, col2 = st.columns(2)  # Creating two columns
        with col1:
            st.image(data["coverImg"][x], width=200)
            st.header(data["title"][x])
            if st.button(f"checkout_{data['title'][x]}_{x}"):  # Use unique key based on book title and index
                selected_book_index = x  # Update the selected book index
            x -= 1
        with col2:
            st.image(data["coverImg"][x], width=200)
            st.header(data["title"][x])
            if st.button(f"checkout_{data['title'][x]}_{x}"):  # Use unique key based on book title and index
                selected_book_index = x  # Update the selected book index
            x -= 1

    # Display selected book details
    st.header("Selected Book Information")
    selected_book = data.iloc[selected_book_index]
    st.write(f"Title: {selected_book['title']}")
    st.write(f"Description: {selected_book['description']}")
    st.write(f"Rating: {selected_book['ratings']}")
    st.write(f"Genres: {selected_book['genres']}")
    st.write(f"Price: {selected_book['price']}")

if __name__ == "__main__":
    main()
