#include <TM1637Display.h>
 
const int CLK_A = D0; //Set the CLK pin connection to the display
const int DIO_A = D1; //Set the DIO pin connection to the display

const int CLK_B = D2; //Set the CLK pin connection to the display
const int DIO_B = D3; //Set the DIO pin connection to the display

 
int numCounter = 0;
 
TM1637Display displayA(CLK_A, DIO_A); //set up the 4-Digit Display.
TM1637Display displayB(CLK_B, DIO_B); //set up the 4-Digit Display.

void setup()
{
 displayA.setBrightness(0x0f); //set the diplay to maximum brightness
 displayB.setBrightness(0x0f); //set the diplay to maximum brightness
}

int fib(int n)
{
  if (n < 7)
    return(0);
  else if (n == 7)
    return(1);
  return(fib(n-1)+fib(n-2)+fib(n-3)+fib(n-4)+fib(n-5)+fib(n-6)+fib(n-7));
}


void loop()
{ 
  for(int numCounter = 1; numCounter < 100000000; numCounter++) //Iterate numCounter
  {
    displayA.showNumberDecEx(numCounter); //Display the numCounter value;
    displayB.showNumberDecEx(numCounter + 1); //Display the numCounter value;
    delay(1000);
  }
  displayA.showNumberDecEx(10); //Display the numCounter value;
  displayB.showNumberDecEx(20); //Display the numCounter value;  
}
