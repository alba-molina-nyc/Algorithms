/*
* Recursion - a function that calls itself and in turn, it makes the problem smaller and smaller because it performs the SAME task with DIFF inputs(based on the previous task)
* (can also be solved by iterations)

* You need a BASE CONDITION in order to stop and avoid the infinite loop
* either you found your answer OR the answer does not exist


function name(parameter1, parameter2, parameter3) {
    // code to be executed
  }

  if (hour < 18) {
  greeting = "Good day";
}
*/



function openRussianDoll(doll) {
    if(doll=1){
        console.log('All dolls are open')
    }else{
        openRussianDoll(doll-1)
    }
  }
openRussianDoll(10);
