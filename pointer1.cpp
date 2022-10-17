#include<iostream>
using namespace std;

int main()
{
//     int a = 5;
//     cout<< a << endl;
//     cout<< &a << endl;

// // * : derefference operator
// // & : address of operator
//     int *p = &a;
//     cout<< *p << endl;
//     cout<< sizeof(p) << endl;

//     double d1 = 23.4;
//     double *p0 = &d1;
//     cout<< sizeof(p0) << endl;

    int *p1 = 0; //null pointer
    cout<< *p1 <<endl; // segmentation fault: as no such memory exist where pointer is pointing

    int b = 3;
    p1 = &b;
    cout<< (*p1)++ << endl;
    cout<< *p1++ << endl;
    cout<< p1 << endl;
    cout<< p1++ << endl;
    
    return 0;
}