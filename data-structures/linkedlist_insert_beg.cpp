/* inserting node at begining of the linked list every time */ 
#include <iostream>

using namespace std;

class node
{
    int data;
    node *next;
public:
    void insert(int data);
    void display();

};

node *head;

void node :: insert(int data)
{
    node *temp;
    temp = new node ;
    temp->data = data;
    temp->next = head;
    head = temp;
}
void node :: display()
{
    node *temp;
    temp = head;
    while (temp != NULL)
    {
        cout<<"The data is: "<<temp->data;
        cout<<endl;
        temp = temp->next;

    }
}



int main()
{
    head = NULL;
    int flag = 1,i,data;
    node abc;
    while(flag == 1)
    {
        cout<<"\n1.Enter at the end of the linked list";
        cout<<"\n2.Print the linked list";
        cout<<"\nEnter your choice: ";
        cin>>i;
        switch(i)
        {
            case 1: cout<<"\nEnter the value to be inserted in list: ";
                    cin>>data;
                    abc.insert(data);
                    break;
            case 2: abc.display();
                    break;
        }
        cout<<"\nDo you want to continue(1-yes/0-no): ";
        cin>>flag;
    }
    return 0;
}