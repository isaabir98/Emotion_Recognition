// a)
#include <iostream>
using namespace std;
    float calcDiscount(int time, float totAmount)
    {

            float sum;
            if( totAmount >= 5000 && 16 <= time|| time >= 19)
        {
            sum= totAmount*10/100 + totAmount;
                
        }

    else if( totAmount >= 5000 && time >= 20 || time >= 22)
            {

            sum=totAmount*12/100+totAmount;
                
            }


    else if( 5000 > totAmount || totAmount >= 2500  && time <=16 || time >= 19)
            {

            sum=totAmount*7/100+totAmount;
                
            }

    
    else if( 5000 > totAmount || totAmount >= 2500 && time >= 20 || time >= 22)
            {

            sum=totAmount*9/100+totAmount;
                
            }


    else {cout<<("INVALID INPUT");} 
    
    cout<<sum;

    return sum;

    }


    int main()
    {
        int time ;
        float amount;

        cout<<"input time ";
        cin>>time;

        cout<<"\ninput amount ";
        cin>>amount;
        
        calcDiscount(time,amount);
    }