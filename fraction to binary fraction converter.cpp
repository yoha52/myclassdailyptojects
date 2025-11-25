#include <iostream>
using namespace std;
int main()
{
    //this program convertes a decimal fraction to binary fraction
    double i = 0.234; //number for test
    cout<<"0.";
    if (i >= 1)
    {
        cout << i;//this converts numbers only less than 1
    }
    else if(i<1)
    {
        while (i != 0)
        {
            int j=0;
            i = i * 2;
            if (i < 1)
            {
                cout<<0;
            }
            else if (i > 1)
            {
                cout<<1;
                i = i - 1;
            }
            else if(i==1)
            {
                cout<< 1;
                break;
            }
            j++;
        }
    }
}
