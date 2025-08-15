// const employee = {
//       calcTax() {
//             console.log('tax rate is 10%');

//       },
// };

// const karanArjun = {
//       salary: 5000,

// };


// karanArjun.__proto__ = employee;
class ToyotaCar{
      start(){
            console.log('Start');
      }
      stop(){
            console.log('stop');
      }
      setBrand(brand) {
            this.brand=brand;
      }
}


let fortuner = new ToyotaCar();
fortuner.setBrand('fortuner');

let lexus = new ToyotaCar();
lexus.setBrand('lexus');


