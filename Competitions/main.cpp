#include <iostream>
#include <string>
#define ARR_SIZE 100

using namespace std;

void addToShelf(const string& bookTitle, const string& author, const string& isbn, string titles[], string authors[], string isbns[], int index) {
    if(index >= 0) {
        cout << "putting book titled, " << bookTitle << " into bookshelf" << endl;
        titles[index] = bookTitle;
        authors[index] = author;
        isbns[index] = isbn;
    }
}

void removeFromShelf(string bookTitle, string titles[], string authors[], string isbns[]) {
    int removeIndex = 0;

    cout << bookTitle << " removed from bookshelf" << endl;

    for(int i = 0; i < ARR_SIZE; i++) {
        if(titles[i] == bookTitle) {
            removeIndex = i;
            break;
        }
    }

    for(int i = removeIndex; i < ARR_SIZE - 1; i++) {
        titles[i] = titles[i + 1];
        authors[i] = authors[i + 1];
        isbns[i] = isbns[i + 1];
    }
}

void show(int booksInShelf, string titles[], string authors[], string isbns[]) {
    for(int i = 0; i < booksInShelf; i++) {
        cout << "Book Number " << i + 1 << endl;
        cout << "Title: " << titles[i] << endl;
        cout << "Author: " << authors[i] << endl;
        cout << "ISBN: " << isbns[i] << endl;
        
        if(i != booksInShelf-1) {
            cout << endl;
        }
    }
}

int main ()
{
    string title[ARR_SIZE];
    string author[ARR_SIZE];
    string isbn[ARR_SIZE];
    string command;
    string bookTitle;
    string a;
    string isb;
    int pee = 0;
    int booksInShelf = -1;

    int i;
    cin >> i;

    for(int j = -1; j < i; j++) {
        getline(cin, command);

        if(command.find("remove") != string::npos) {  // remove in command
            removeFromShelf(command.erase(0, 7), title, author, isbn);
            booksInShelf--;
        } else if(command == "show") {
            if(booksInShelf > 0) {
                show(booksInShelf, title, author, isbn);
            }
        } else {
            string s = command;
            string delimiter = " ";
            size_t pos = 0;
            string token;

            while ((pos = s.find(delimiter)) != string::npos) {
                token = s.substr(0, pos);
                pee++;
                if(pee == 1) {
                    bookTitle = token;
                } else if (pee == 2) {
                    a = token;
                }

                s.erase(0, pos + delimiter.length());
            }

            isb = s;
            addToShelf(bookTitle, a, isb, title, author, isbn, j);
            booksInShelf++;
            pee = 0;
        }
    }
    
    return 0;
}