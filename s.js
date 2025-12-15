// num=10;
// if(num%2==0){
//     console.log("even number")
// }
// else{
//     console.log("not even")
// }

let day=prompt("enter a numbver between 1 to 7");
switch(day)
{
    case 1:day=Monday;
    break;

     case 2:day=Tuesday;
    break;

     case 3:day=Wednesday;
    break;

     case 4:day=Thursday;
    break;
     case 5:day=Friday;
    break;

     case 6:day=Saturday;
    break;
     case 7:day=Sunday;
    break;
}
console.log("today is ",day)