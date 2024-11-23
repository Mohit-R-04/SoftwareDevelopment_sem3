class Page:
    def __init__(self, pg_number: int, contents: str):
        self.pg_number = pg_number
        self.contents = contents

    def get_content(self) -> str:
        return self.contents

class Document:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.pages = []

    def add_page(self, pg_number: int, contents: str) -> None:
        page = Page(pg_number, contents)
        self.pages.append(page)
        print(f"Page {pg_number} added to the document.")

    def remove_page(self, pg_number: int) -> None:
        self.pages = [page for page in self.pages if page.pg_number != pg_number]
        print(f"Page {pg_number} removed from the document.")

    def get_page_contents(self, pg_number: int) -> str:
        for page in self.pages:
            if page.pg_number == pg_number:
                return page.get_content()
        return "Page not found"

# Example usage
doc = Document("My Document", "John Doe")
print(f"Document '{doc.title}' by {doc.author} created.")

# Add pages to the document
doc.add_page(1, "This is the content of page 1.")
doc.add_page(2, "This is the content of page 2.")
doc.add_page(3, "This is the content of page 3.")

# Access content of a specific page
print(f"Contents of Page 1: {doc.get_page_contents(1)}")
print(f"Contents of Page 2: {doc.get_page_contents(2)}")

# Remove a page from the document
doc.remove_page(2)

# Try accessing the removed page
print(f"Contents of Page 2: {doc.get_page_contents(2)}")

# Check remaining pages
print(f"Contents of Page 1: {doc.get_page_contents(1)}")
print(f"Contents of Page 3: {doc.get_page_contents(3)}")
