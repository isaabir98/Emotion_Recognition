#include<iostream>
using namespace std;



void insertionSort1(int n, int arr[]) {
        
        for( int step=1; step< n; step++)
        {
            int key= arr[step];
            int j= step-1;
            
            while (key < arr[j] && j >=0)
            {
                arr[j+1]=arr[j];
                
                --j;
            }
        arr[j+1]=key;
            
        }

        for(int i=0; i< 5 ; i++)
        {
            cout<<arr[i];
        }
        
    
}


int main()
{
    int ar[5]={10,8,1,3,2};

    insertionSort1(5,ar);

    cout<<"jo";
}