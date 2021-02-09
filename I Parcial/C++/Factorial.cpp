#include <iostream>
using namespace std;

int factorial(int n);

int main()
{
    int n;
    int f;
    cout<<"Ingrese un numero entero: ";
    cin>>n;
    f = factorial(n);
    cout<<"El factorial de: " << n << " es: " << f <<endl;
}

int factorial(int n)
{
    if(n<2)
    {
        return 1;
    }
    else if(n>2)
    {
        return n*factorial(n-1);
    }
}
