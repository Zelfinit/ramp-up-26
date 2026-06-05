from fastapi import FastAPI, HTTPException
import schemas
import uvicorn

app = FastAPI()
books = {}


@app.get("/books/")
def getBooks():
    return books


@app.get("/books/{id}")
def getBook(id: int):
    if id in books.keys():
        return books[id]
    else:
        raise HTTPException(404, "Book not found")


@app.post("/books/")
def addBook(book: schemas.CreateBook):
    newBook = schemas.Book(
        id=len(books.keys()) + 1,
        title=book.title,
        year=book.year,
        author=book.author,
    )
    books[newBook.id] = newBook
    return newBook


@app.put("/books/{id}")
def updateBook(id: int, book: schemas.CreateBook):
    if id in books.keys():
        books[id] = schemas.Book(
            id=id, title=book.title, author=book.author, year=book.year
        )
        return books[id]
    else:
        raise HTTPException(404, "Book not found")


@app.delete("/books/{id}")
def deleteBook(id: int):
    if id in books.keys():
        books.pop(id)
        return {}
    else:
        raise HTTPException(404, "Book not found")


if __name__ == "__main__":
    uvicorn.run(app, port=8080)
