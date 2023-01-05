##Declare class and mention all API end points here

class apiResources():
    getAllEmployees = '/api/v1/employees'
    getEmployeeWithID = '/api/v1/employee/?ID=id'
    createEmployee = '/api/v1/create'
    updateEmployeeWithID = '/api/v1/update/?ID=id'
    deleteEmployeeWithID = '/api/v1/delete/?ID=id'
    # addBook = '/Library/Addbook.php'
    # deleteBook = '/Library/DeleteBook.php'
    # getBookByAuthName = '/Library/GetBook.php?AuthorName=authname'
    # getBookByID = 'Library/GetBook.php?ID=id'