from fastapi import FastAPI, Body

from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str  
    category: str

books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "category": "Fiction"},
    {"title": "Sapiens", "author": "Yuval Noah Harari", "category": "History"},
    {"title": "The Pragmatic Programmer", "author": "David Thomas", "category": "Technology"},
    {"title": "Becoming", "author": "Michelle Obama", "category": "Biography"},
    {"title": "Dune", "author": "Frank Herbert", "category": "Science Fiction"},
    {"title": "The Silent Patient", "author": "Alex Michaelides", "category": "Mystery"},
    {"title": "Atomic Habits", "author": "James Clear", "category": "Self-Help"},
    {"title": "The Art of War", "author": "Sun Tzu", "category": "Philosophy"},
    {"title": "Gone Girl", "author": "Gillian Flynn", "category": "Thriller"},
    {"title": "A Brief History of Time", "author": "Stephen Hawking", "category": "Science"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "category": "Fiction"},
    {"title": "Educated", "author": "Tara Westover", "category": "Memoir"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "category": "Fantasy"},
    {"title": "Think and Grow Rich", "author": "Napoleon Hill", "category": "Business"},
    {"title": "The Da Vinci Code", "author": "Dan Brown", "category": "Mystery"},
    {"title": "1984", "author": "George Orwell", "category": "Dystopian"},
    {"title": "The Immortal Life of Henrietta Lacks", "author": "Rebecca Skloot", "category": "Science"},
    {"title": "Where the Crawdads Sing", "author": "Delia Owens", "category": "Fiction"},
    {"title": "The 7 Habits of Highly Effective People", "author": "Stephen Covey", "category": "Self-Help"},
    {"title": "The Handmaid's Tale", "author": "Margaret Atwood", "category": "Dystopian"},
    {"title": "Thinking, Fast and Slow", "author": "Daniel Kahneman", "category": "Psychology"},
    {"title": "The Girl with the Dragon Tattoo", "author": "Stieg Larsson", "category": "Crime"},
    {"title": "Born a Crime", "author": "Trevor Noah", "category": "Biography"},
    {"title": "The Lean Startup", "author": "Eric Ries", "category": "Business"},
    {"title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "category": "Fantasy"},
    {"title": "The Power of Now", "author": "Eckhart Tolle", "category": "Spirituality"},
    {"title": "In Cold Blood", "author": "Truman Capote", "category": "True Crime"},
    {"title": "The Alchemist", "author": "Paulo Coelho", "category": "Philosophy"},
    {"title": "Clean Code", "author": "Robert Martin", "category": "Technology"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "category": "Fiction"}
]

app = FastAPI()

# Create a POST 
@app.post('/books/create_book')
async def create_book(new_book: Book=Body()):
    books.append(new_book.dict())
    return {"message": "Book added successfully"}

# Create a GET to get all the values from the book list
@app.get('/books')
async def read_all_books():
    return books

# Get a book from the list of books
@app.get('/books/get_book/{book_title}')
async def get_book(book_title: str):
    book = next((book for book in books if book.get('title').casefold() == book_title.casefold()), None)
    if book:
        return {
            "title": book.get('title'),
            "author": book.get('author'),
            "category": book.get('category')
        }
    return {"error": "Book not found!"}

# To update an entry in the books list -- PUT
@app.put('/books/update_book')
async def update_book(update_book=Body()):
    for i in range(len(books)):
        if books[i].get('title').casefold() == update_book.get('title').casefold():
            books[i] = update_book

# To delete an entry that matches the book with the title the user provided.
@app.delete('/books/delete_book/{book_title}')
async def delete_book(book_title: str):
    for i in range(len(books)):
        if books[i].get('title').casefold() == book_title.casefold():
            books.pop(i)
            break
        return {"message": "Book deleted successfully!"}