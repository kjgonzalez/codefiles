/* 
This is the very first attempt to properly learn javascript. 

process for installing / enabling node.js (2024-06-01: v20 via package manager / fnm): https://nodejs.org/en/download/package-manager

you can step through code when working in vscode, including setting breakpoints and seeing output in real time.

misc topics: 
numpy-like/cpp-like performance in javascript:
https://stackoverflow.com/questions/31412537/is-there-a-numpy-like-package-for-node-js-and-if-not-why-not

declaring const / var variables: 
https://stackoverflow.com/questions/76010295/when-should-you-use-var-let-or-const-in-javascript-code



todo: 
done hello world
done function
done logic/binary operators
done math operators
done whileloop
done if/elseif/else
done variable
???? forloop
???? make a class
???? iterate through a list
???? strings
???? save to file
???? read from file
???? take user input?
???? nullish coalescing operator (??)
???? ternary operator (and operator)
???? import a library


future topics:
  interacting with foundry
  running code in a browser
  some kinda hooks / events?


*/

// basic printing / hello world: 
console.log("hello world")

// function
function pyt(a,b){
    return (a*a+b*b)**0.5
}
console.log(pyt(3,4))

// logic operators
function print(expr){ // convenience function, because console.log is very tedious
    console.log(expr)
}
print('logic')
print(1==1)
print(1<2)
print(2<3)
print(3<=3.2)
print(true==false)
print(true||false)
print(!false)
print('binary operator')
print(1|2)  // 3 (0b0011)
print(2<<2) // 8

print('math operators')
print(10%3) // 1, modulo
print(3**2) // power

// several ways to define a variable: 
a = 1
var b = 2 // original method to declare a variable
let c = 3 // only exists within a block (e.g. {})
const d=4 // value cannot be reassigned

// logic operator
if(a==2){print('option 1')}
else if(a==b) print('option 2') // may be possible to assign value in else-if statement ...
else print('option 3')

let e = (a<10)? 5:6 // if(a<10), e=5, else e=6

// there are both while and do-while loops in js: 
while(a<10){
    print(a)
    a+=1
}
print('do loop:')
do{
    a+=1
    print(a)
}while(a<4)

// forloops take on multiple forms (todo)


// eof
