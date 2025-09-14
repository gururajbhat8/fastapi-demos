from fastapi import Body, FastAPI


app = FastAPI()


BOOKS = [
    {'title': 'Title one', 'author':'Author one', 'category':'science'},
    {'title': 'Title two', 'author':'Author two', 'category':'science'},
    {'title': 'Title three', 'author':'Author six', 'category':'history'},
    {'title': 'Title four', 'author':'Author four', 'category':'math'},
    {'title': 'Title five', 'author':'Author five', 'category':'math'},
    {'title': 'Title six', 'author':'Author six', 'category':'math'}
]


@app.get("/books")
async def read_all_books():
    return BOOKS


# @app.get("/books/{dynamic_param}")
# async def read_all_books(dynamic_param : str):
#     return {'dynamic_param': dynamic_param}

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
        
    return books_to_return


@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
            book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return

@app.post("/books/create_book")
async def create_book(new_book = Body()):
    BOOKS.append(new_book)

@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

@app.delete("books/delete_book/{book_title}")
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

'''
Create a new API Endpoint that can fetch all books from a specific author using either Path Parameters or Query Parameters.
'''
@app.get("/books/byauthor/{author}")
async def fetch_books_specific_author(author : str):
    list_of_books = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            list_of_books.append(book)
    
    return list_of_books
