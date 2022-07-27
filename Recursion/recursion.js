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
    if(doll==1){
        console.log('All dolls are open')
    }else{
        openRussianDoll(doll-1)
    }
  }
// openRussianDoll(10);


// ------------------------------------------------------------------------------------------------------------------------------
/*
HOW recursion works --> 2 conditions
1. method calls itself
2. exit from inifite loop

function recursionMethod(parameter) {
    if(exist from condition satisfied) {
        return some value
    } else {
        recursionMethod(modified paramenter)
    }
}

recursionMethod();

*/

function firstMethod() {
    secondMethod()
    console.log("i am the first method")

}
   

function secondMethod(){
    thirdMethod()
    console.log("i am the second method")
}


function thirdMethod() {
    fourthMethod()
    console.log("i am the third method")
}

function fourthMethod() {
    console.log("i am the fourth method")
    firstMethod();

}

firstMethod();

/*

STEPS
1- identify the RECURSIVE CASE (where the function keeps calling itself)
2- identify BASE CASE - the STOP criteria
3- Unintentional case - the CONSTRAINT (while at the top)
*/